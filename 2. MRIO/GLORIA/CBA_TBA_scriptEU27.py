# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 11:50:16 2022

@author: etber
"""

import numpy as np
import pandas as pd
from scipy.linalg import lu_factor, lu_solve, inv
import os
import gc  # For garbage collection

#Defining the MRIO: GLORIA, Eora or Exiobase
MRIO = 'GLORIA'

source_path = "D:/Deforestation_Nature/Forest_Club_SI/2. MRIO"

MRIO_path = os.path.join(source_path, MRIO,'data')
commodity_path = os.path.join(source_path, MRIO,'commodity')
index_path = os.path.join(source_path, MRIO,'indexes')
output_path = os.path.join(source_path,MRIO,'output')
script_path = os.path.join(source_path,'Scripts','tba_sdg')

# choose among: EXIOBASE, EU27, OECD, G7, G20):
geo_agg_list = ['EU27']

# Selection of the externality
externality = 'HILDA'
 
#Defining the version of the externality to use in case of several versions
update='V_2_1'

#Defining the sectors to keep at the end of the analysis
sector_list = [
    'Growing wheat industry',
    'Growing maize industry',
    'Growing cereals n.e.c industry',
    'Growing leguminous crops and oil seeds industry',
    'Growing rice industry',
    'Growing vegetables, roots, tubers industry',
    'Growing sugar beet and cane industry',
    'Growing tobacco industry',
    'Growing fibre crops industry',
    'Growing crops n.e.c. industry',
    'Growing grapes industry',
    'Growing fruits and nuts industry',
    'Growing beverage crops (coffee, tea etc) industry',
    'Growing spices, aromatic, drug and pharmaceutical crops industry',
    'Seeds and plant propagation industry',
    'Raising of cattle industry'
    ]

#Defining the EXIOBASE countries to keep in the TBA calcualtion (outside of the EU TBA)
list_year =  ['2012','2013','2014','2015','2016','2017','2018','2019']

#Definining the level of aggregation of the results
list_producer = ['ARG','AGO','BRA','CIV','COD','COL','GHA','IDN','MYS','PER','PRY']

def load_z (year):
    '''
    Loads the raw MRIO matrices for the targeted year(s) and processes them into intermediate transaction 
    and final consumption matrices. The function supports different MRIO databases (Exiobase, EORA, GLORIA).
    
    Parameters
    ----------
    year : int
        The target year for which the EXIOBASE matrices will be loaded (e.g., 2012-2019).

    Returns
    -------
    z : np.ndarray
        A NumPy array representing the intermediate transaction matrix (Z), where rows and columns correspond 
        to sectors and countries in the MRIO model.
    y : np.ndarray
        A 2D NumPy array representing the final consumption matrix (Y), showing the distribution of final 
        demand across sectors and regions.
    num_lines : int
        The total number of rows (sectors * countries) in the intermediate transaction matrix.
    '''
    if MRIO == "Exiobase":
        z = pd.read_csv(os.path.join(MRIO_path,'Z_'+str(year)+'.txt'),delimiter='\t', low_memory=False)
        del z["region"]
        del z["Unnamed: 1"]
        z = z.drop(z.index[0:2])
        z = z.to_numpy(float)
    if MRIO == "EORA":
        z = pd.read_csv(os.path.join(MRIO_path,'T-Results_'+str(year)+'.csv'), delimiter=',', low_memory=False, header= None)
        z = z.to_numpy(float)
    else: 
        z = pd.read_table(os.path.join(MRIO_path,'20240111_120secMother_AllCountries_002_T-Results_'+str(year)+'_059_Markup001(full).csv'), dtype=float, delimiter=',', low_memory=False, header= None)
        z = z.to_numpy().astype(float)
    return z

def load_y (year):
    '''
    Loads the raw MRIO matrices for the targeted year(s) and processes them into intermediate transaction 
    and final consumption matrices. The function supports different MRIO databases (Exiobase, EORA, GLORIA).
    
    Parameters
    ----------
    year : int
        The target year for which the EXIOBASE matrices will be loaded (e.g., 2012-2019).

    Returns
    -------
    z : np.ndarray
        A NumPy array representing the intermediate transaction matrix (Z), where rows and columns correspond 
        to sectors and countries in the MRIO model.
    y : np.ndarray
        A 2D NumPy array representing the final consumption matrix (Y), showing the distribution of final 
        demand across sectors and regions.
    num_lines : int
        The total number of rows (sectors * countries) in the intermediate transaction matrix.
    '''
    if MRIO == "Exiobase":
        y = pd.read_csv(os.path.join(MRIO_path,'Y_'+str(year)+'.txt'),delimiter='\t', low_memory=False)
        del y["region"]
        del y["Unnamed: 1"]
        # Y matrix, summing all the FD per country and to numpy 
        y = y.drop(y.index[0:2])
        y = y.to_numpy(float)
        y = y.reshape(391363, 7)
        y = y.sum(axis =1)
        y = y.reshape(7987, 49)   
    if MRIO == "EORA":
        y = pd.read_csv(os.path.join(MRIO_path,'Y-Results_'+str(year)+'.csv'), delimiter=',', low_memory=False , header= None )
        y = y.to_numpy(float)
        y = y.reshape(14839, 190, 6).sum(axis=2)
    else: 
        y = pd.read_csv(os.path.join(MRIO_path,'20240111_120secMother_AllCountries_002_Y-Results_'+str(year)+'_059_Markup001(full).csv'), delimiter=',', low_memory=False , header= None )
        y = y.to_numpy().astype(float)
        
        # Number of different FD
        block_size = 6
        # Number of columns
        num_columns = y.shape[1]  
        num_lines = y.shape[0]

        y = y.reshape(num_lines * (num_columns//block_size), block_size)
        y = y.sum(axis =1)
        y = y.reshape(num_lines,num_columns//block_size)
        
    return y,num_lines

def label_input (geo_agg):
    '''
    Loads and returns the label indexes for intermediate transactions (Z) and final consumption (Y) matrices. 
    The labels include the MRIO country names, sector names, and aggregated geographical areas (e.g., EU, G7).
    
    Parameters
    ----------
    geo_agg : str
        The level of geographical aggregation to apply ('Original', 'EU', 'G7', 'G20', 'OECD').

    Returns
    -------
    la : pd.DataFrame
        DataFrame containing labels for the intermediate transaction matrix (Z), with columns for region names 
        and sector names, merged with the geographical zone information.
    lb : pd.DataFrame
        DataFrame containing labels for the final demand matrix (Y), with columns for region names and geographical 
        zones.
    '''
    
    la = pd.read_excel(os.path.join(index_path,'Indexes.xlsx'), sheet_name='Inter-Industry')
    la = la[['Region_Name','Sector_Name']]
    lf = pd.read_excel(os.path.join(index_path,'Indexes.xlsx'), sheet_name='Final-Demand')
    lb = lf[['Region_Name']].drop_duplicates(keep='first')
    lb.reset_index(drop=True, inplace=True)
    lc = pd.read_excel(os.path.join(index_path,'Indexes.xlsx'), sheet_name='Zone_'+str(geo_agg))
    la = pd.merge(la, lc, on=['Region_Name'])
    lb = pd.merge(lb, lc, on=['Region_Name'])
    return la, lb

def leontief(z, y, num_lines, year):
    '''
    Calculates and saves the Leontief inverse matrix, technical coefficient matrix, 
    and total output per sector. Reuses saved matrices if available.

    Parameters
    ----------
    z : np.ndarray
        Intermediate transaction matrix (Z).
    y : np.ndarray
        Final consumption matrix (Y).
    num_lines : int
        The total number of sectors and countries (rows) in the Z matrix.
    year : int
        Year for which the Leontief inverse is being calculated.

    Returns
    -------
    l : np.ndarray
        The Leontief inverse matrix (I - A)^-1.
    lines_tot_d : np.ndarray
        Total output per sector.
    a : np.ndarray
        The technical coefficient matrix (A).
    '''
    # Define file paths for cached matrices
    lines_tot_file = os.path.join(MRIO_path, f'Sum_lines_{year}.npy')
    a_file = os.path.join(MRIO_path, f'Technical_matrix_{year}.npy')
    l_file = os.path.join(MRIO_path, f'Leontief_inverse_{year}.npy')

    # Step 1: Load or calculate `lines_tot` and `lines_tot_d`
    if os.path.exists(lines_tot_file):
        lines_tot = np.load(lines_tot_file)
        lines_tot_d = lines_tot.copy()
        lines_tot_d[lines_tot_d == 0] = 1
    else:
        lines_tot = z.sum(axis=1) + y.sum(axis=1)
        np.save(lines_tot_file, lines_tot)
        lines_tot_d = lines_tot.copy()
        lines_tot_d[lines_tot_d == 0] = 1
    lines_tot_d = lines_tot_d.reshape(1, num_lines)

    # Step 2: Load or calculate the technical coefficient matrix `a`
    if os.path.exists(a_file):
        a = np.load(a_file)
    else:
        a = z / lines_tot_d
        np.save(a_file, a)

    # Step 3: Load or calculate the Leontief inverse matrix `l`
    if os.path.exists(l_file):
        l = np.load(l_file)
    else:
        i = np.identity(z.shape[0])  # Identity matrix
        lu, piv = lu_factor(i - a)
        l = lu_solve((lu, piv), i)
        np.save(l_file, l)

    # Optional garbage collection
    del z, y
    gc.collect()

    return l, lines_tot_d, a

def commodity (lines_tot_d, l, update, year, num_lines, producer):
    '''
    Loads the satellite account data (externalities) for the selected year and producer, and calculates the 
    direct and indirect environmental impacts using the Leontief inverse and technical coefficient matrices.
    
    Parameters
    ----------
    lines_tot_d : np.ndarray
        Total output per sector for normalization of environmental impacts.
    i : np.ndarray
        Identity matrix used for Leontief calculations.
    l : np.ndarray
        Leontief inverse matrix (I - A)^-1.
    update : str
        Version of the externality dataset to use (e.g., 'V_1').
    year : int
        Target year for loading the commodity data.
    num_lines : int
        Number of rows in the intermediate transaction matrix (sectors * countries).
    producer : str
        Code of the country (or region) acting as the producer of the commodity under analysis (e.g., 'BRA' for Brazil).

    Returns
    -------
    m : np.ndarray
        Matrix of indirect environmental impacts for the commodity.
    e : np.ndarray
        Diagonal matrix of direct environmental impacts for the selected externality.
    '''
    q_file_path = os.path.join(commodity_path, externality, update, 'Satellites_' + str(year) + '_' + str(producer) +'.csv')
    q = pd.read_csv(q_file_path,delimiter=',', header=None)
    
    q = q.to_numpy(float)
    
    s = len(q)
    
    q = q.reshape(1, num_lines)
    
    e = q/lines_tot_d
    i = np.identity(s)
    e = i*e
    m = np.matmul(e,l)
    
    del i 
    gc.collect()
    
    return m,e

def cba_calc (m, yl, geo_agg, lb):
    '''
    Performs Consumption-Based Accounting (CBA) by calculating the environmental impact associated with the 
    consumption of goods and services for each region in the MRIO model.

    Parameters
    ----------
    m : np.ndarray
        Matrix of indirect environmental impacts from the commodity function.
    yl : pd.DataFrame
        Labeled final demand matrix (Y) with multi-index for country and sector.
    geo_agg : str
        Geographical aggregation level for the analysis (e.g., 'EU27', 'G7').
    lb : pd.DataFrame
        Labels for the final demand matrix (Y), showing regional zone information.

    Returns
    -------
    cba : np.ndarray
        Consumption-Based Accounting matrix, representing the environmental impact by country and sector of 
        final consumption.
    '''
    m = np.array(m)
    
    if geo_agg in ['EXIOBASE', 'GLORIA', 'EORA']:
        ytl = yl.copy()
    else:
        ytl = yl.copy()
        ld = lb.query (f'Zone == "{geo_agg}"')["Region_Name"]
        list_country = ld.values.tolist()
        idx = pd.IndexSlice
        ytl.loc[idx[:, :, geo_agg], idx[:, geo_agg]] = 0 
        for country in list_country:
            ytl.loc[idx[country, :, :], idx[country, :]] = yl.loc[idx[country, :, :], idx[country, :]].copy()
    
    y = np.array(ytl)
    cba = np.matmul(m,y)
    
    return cba

def labelling (la,lb,y,a):
    '''
    Converts the intermediate transaction (Z), final consumption (Y), and technical coefficient (A) matrices 
    into labeled DataFrames using the provided labels (la and lb). These DataFrames are easier to interpret 
    and allow for querying based on country, sector, and geographical area.
    
    Parameters
    ----------
    la : pd.DataFrame
        Labels for the intermediate transaction matrix (Z), showing sector and region names.
    lb : pd.DataFrame
        Labels for the final consumption matrix (Y), showing region names.
    y : np.ndarray
        Final consumption matrix (Y).
    a : np.ndarray
        Technical coefficient matrix (A), derived from the Z matrix.

    Returns
    -------
    yl : pd.DataFrame
        Labeled final consumption matrix (Y), indexed by country and sector.
    al : pd.DataFrame
        Labeled technical coefficient matrix (A), indexed by country and sector.
    '''
    index = pd.MultiIndex.from_frame(la, names=['Country_L', 'Sector_L', 'Area_L'])
    index2 = pd.MultiIndex.from_frame(la, names=['Country_C', 'Sector_C', 'Area_C'])
    index3 = pd.MultiIndex.from_frame(lb, names=['Country_FD', 'Area_FD'])
    yl = pd.DataFrame(y, index = index, columns=index3)
    #zl = pd.DataFrame(z, index = index, columns=index2)
    al = pd.DataFrame(a, index = index, columns=index2)
    #el = pd.DataFrame(e, index = index, columns=index2)
    #return yl, zl, al, el
    return yl, al

def labelling_e (la,e):
    '''
    Converts the direct environmental impact matrix (E) into a labeled DataFrame using the provided labels (la). 
    The resulting DataFrame includes country and sector names, making it easier to interpret the results.

    Parameters
    ----------
    la : pd.DataFrame
        Labels for the intermediate transaction matrix (Z), showing sector and region names.
    e : np.ndarray
        Direct environmental impact matrix (E) for a given externality.

    Returns
    -------
    el : pd.DataFrame
        Labeled direct environmental impact matrix, indexed by country and sector.
    '''
    index = pd.MultiIndex.from_frame(la, names=['Country_L', 'Sector_L', 'Area_L'])
    index2 = pd.MultiIndex.from_frame(la, names=['Country_C', 'Sector_C', 'Area_C'])
    el = pd.DataFrame(e, index = index, columns=index2)
    #return yl, zl, al, el
    return el

def cba_labelling (la,lb,cba):
    ''''
    Labels the Consumption-Based Accounting (CBA) matrix using the provided labels for sectors and regions. 
    The CBA matrix is converted into a labeled DataFrame for easy interpretation.

    Parameters
    ----------
    la : pd.DataFrame
        Labels for the intermediate transaction matrix (Z), showing sector and region names.
    lb : pd.DataFrame
        Labels for the final consumption matrix (Y), showing region names.
    cba : np.ndarray
        The consumption-based accounting matrix.

    Returns
    -------
    cba_l : pd.DataFrame
        Labeled CBA matrix, indexed by country, sector, and area, for easier interpretation and querying.
    '''
    index = pd.MultiIndex.from_frame(la, names=['Country', 'Sector', 'Area'])
    index2 = pd.MultiIndex.from_frame(lb, names=['Country', 'Area'])
    cba_l = pd.DataFrame(cba, index = index, columns=index2)
    return cba_l

def TBA (zone,l,al,el,yl):
    '''
    Calculates Throughflow-Based Accounting (TBA) by computing the environmental impact of intermediate 
    transactions flowing through a specified country or zone. This method isolates the contribution of the 
    transition country within global supply chains.
    
    Parameters
    ----------
    zone : str
        The country or region for which the throughflow is being calculated (e.g., 'BRA' for Brazil).
    l : np.ndarray
        Leontief inverse matrix (I - A)^-1.
    al : pd.DataFrame
        Labeled technical coefficient matrix (A).
    el : pd.DataFrame
        Labeled environmental impact matrix (E).
    yl : pd.DataFrame
        Labeled final consumption matrix (Y).

    Returns
    -------
    t : np.ndarray
        The throughflow-based accounting matrix, representing the environmental impact attributable to the 
        intermediate transactions involving the specified zone.
    '''
    # At techical matrix in abscence of the country
    at = al.copy()
    idx = pd.IndexSlice
    at.loc[idx[:, :, zone], idx[:,:,:]] = 0
    at.loc[idx[:, :, :], idx[:,:,zone]] = 0
    at = at.to_numpy()
    s = len(at)
    i = np.identity(s)
   
    #lt = inv(i-at)
    
    # Step 1: LU Decomposition (this is only done once)
    lu, piv = lu_factor(i-at)
    # Step 2: Solve for all columns of the identity matrix simultaneously
    lt = lu_solve((lu, piv), i)
    
    del i
    del at
    l_tba = l - lt
    # Env. Matrix in the abscence of the country
    e_dt = el.copy()
    e_dt.loc[idx[:, :, zone], idx[:,:,:]] = 0
    e_dt = e_dt.to_numpy()
    mt = np.matmul(e_dt,l_tba)
    del e_dt
    del l_tba
    # FD in the abscence of the country
    yt = yl.copy()
    yt.loc[idx[:, :, :], idx[:,zone]] = 0
    yt = yt.to_numpy()
    t = np.matmul(mt,yt)
    return t


def main_CBA():
    '''
    Main function to execute the Consumption-Based Accounting (CBA) analysis. Iterates over the selected 
    years and geographical aggregations, calculating and saving the CBA results for each combination. 
    Results are stored as labeled CSV files.
    '''
    for geo_agg in geo_agg_list:
        df_list = []
        for year in list_year:
            l_file = os.path.join(MRIO_path, f'Leontief_inverse_{year}.npy')
            if os.path.exists(l_file):
                z = None
            else : 
                z = load_z(year)
            y,num_lines = load_y(year)
            l,lines_tot_d,a = leontief (z=z, y=y, num_lines=num_lines, year=year)
            la,lb = label_input (geo_agg)
            yl, al = labelling (la, lb, y, a) 
            for producer in list_producer:
                m,e = commodity (lines_tot_d, l, update, year, num_lines, producer)
                cba = cba_calc (m, yl, geo_agg, lb) # Calculating the Consumption Based Accounting (CBA)
                cba_l = cba_labelling(la, lb, cba) # Labelling the Consumption Based Accounting (CBA)
                cba_r = cba_l.loc[cba_l.index.get_level_values(0) == producer]
                cba_r = cba_r.stack(level=[0, 1], future_stack=True)
                cba_df = cba_r.to_frame(name="Value")
                cba_df.index.set_names(
                    ["Country_orig", "Sector", "Area_orig", 
                     "Country_dest", "Area_dest"], 
                    inplace=True
                )
                cba_df = cba_df.reset_index()
                cba_df = cba_df[cba_df['Sector'].isin(sector_list)]
                cba_df['Year'] = year

                df_list.append(cba_df)
                
            # Free up memory by deleting large variables
            del z, y, l, lines_tot_d, a, m, e, la, lb, yl, al, cba, cba_l, cba_r
            gc.collect()  # Force garbage collection to free memory  
                
        result_df = pd.concat(df_list)
        result_df.to_csv(os.path.join(output_path, 'CBA', f'CBA_{min(list_year)}-{max(list_year)}_{geo_agg}_{externality}_{update}_2.csv'))           

def main_TBA():
    '''
    Main function to execute the Throughflow-Based Accounting (TBA) analysis. Iterates over the selected 
    years, producers, and zones to compute and save the TBA results for each combination. Results are 
    stored as labeled CSV files.
    '''
    for geo_agg in geo_agg_list:
        for year in list_year:
            
            l_file = os.path.join(MRIO_path, f'Leontief_inverse_{year}.npy')
            if os.path.exists(l_file):
                z = None
            else : 
                z = load_z(year)
            y,num_lines = load_y(year)
            
            print(f"Data loaded for year {year}.")
            print(f"Calculating Leontief matrix for year {year}...")
            l,lines_tot_d,a = leontief (z=z, y=y, num_lines=num_lines, year=year)
            print(f"Leontief matrix calculated for year {year}.")
            del z  # Free memory by deleting Z and Y after they are no longer needed
            gc.collect()  # Force garbage collection
            
            la,lb = label_input (geo_agg)
            yl, al = labelling (la, lb, y, a) 
            
            del y,a  # Free memory by deleting Z and Y after they are no longer needed
            gc.collect() 
            
            for producer in list_producer:
                
                print(f"Processing commodity data for year {year} and producer {producer}...")

                m,e = commodity (lines_tot_d, l, update, year, num_lines,  producer)
                el = labelling_e (la,e)
                
                # Delete unneeded matrices after they are used
                del e # Free memory for these large matrices after commodity data is processed
                gc.collect()  # Force garbage collection                
                                
                ld = lb["Zone"]
                list_ld = ld.values.tolist()
                list_area = []
                list_area = list(dict.fromkeys(list_ld))
                list_area= ['EU27']
                
                for zone in list_area : # Calculating the Throughflow Based Accounting (TBA)
                    print(f"Calculating TBA for zone {zone} in year {year} and producer {producer}...")
                    t = TBA(zone,l,al,el,yl)
                    print(f"TBA calculation completed for zone {zone} in year {year} and producer {producer}.")
                    
                    index = pd.MultiIndex.from_frame(la, names=['Country_L', 'Sector_L', 'Area_L'])
                    index2 = pd.MultiIndex.from_frame(lb, names=['Country_C', 'Area_C'])
                    
                    t = pd.DataFrame(t, index = index, columns = index2)
                    t = t[t.index.get_level_values('Sector_L').isin(sector_list)]
                
                    t_r = t.loc[t.index.get_level_values(0) == producer]
                    t_r = t_r.reset_index()
                    t_r.columns = t_r.columns.droplevel(1)
                    
                    T_unpivot = pd.melt(t_r, id_vars= ['Country_L','Sector_L','Area_L'])
                    T_unpivot.rename({'Country_L':'Origin_country','Sector_L':'Origin_Sector','Area_L':'Origin_area','Country_C':'Destination_country','Area_C':'Destination_area'},
                    axis="columns", inplace = True)
                    T_unpivot['Transition_country'] = zone
                    T_unpivot['Year'] = year
                    T_unpivot = T_unpivot.drop(['Origin_area'], axis=1)
                    T_unpivot.to_csv(os.path.join(output_path,'TBA','TBA_'+str(year)+'_traversing-'+str(zone)+'_'+str(externality)+'_'+str(update)+'_'+str(producer)+'.csv')) 

                    # Delete T variables after each zone is processed to free memory
                    del t, t_r, T_unpivot
                    gc.collect()  # Force garbage collection after each zone
                    
            # Delete any remaining large variables after processing the year
            del la, lb, yl, al, el  # These are no longer needed after the year is processed
            gc.collect()  # Force garbage collection after each year                    
       
#main_CBA()
main_TBA()