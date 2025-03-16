# Data Usage Guide

## First step, working with HILDA+ data

### Downloading HILDA+ (Version 2.1)
This project utilizes the HILDA+ Global Land Use Change dataset (1960–2019) from Winkler et al., 2020.

The latest version (2.1) can be downloaded from:
https://bwsyncandshare.kit.edu/s/H2iQG6nMPTaxpqR/download

### Required Files
To ensure proper functionality, please download the following NetCDF files:

- hildaplus_GLOB-2-1-crop_states.nc
- hildaplus_GLOB-2-1-crop_transitions.nc

These contain the global crop states and transitions needed for the analysis.

### Usage Instructions
Place the downloaded files in the appropriate directory (e.g., 1_Data/1. HILDA data/1. Extracting_ntcdf_data/1. HILDA_NTCDF_data).
Install the dependencies required to read NetCDF files (e.g., netCDF4, numpy, pandas).
Load the data in your workflow using Python or any other tool that handles NetCDF.

#### 1. Python Environment
Install Python and the required libraries:
```bash
conda install numpy pandas netCDF4
# or
pip install numpy pandas netCDF4
```

#### 2. Run the HILDA Extraction Script
Open the terminal
Navigate to the folder:
...\1_Data\1. HILDA data\1. Extracting_ntcdf_data\1. HILDA_NTCDF_data

Run the Python script:
```bash
python 1_HILDA+_code_extraction.py
```
This will generate extracted data in subfolders under:
1_Data\1. HILDA data\1. Extracting_ntcdf_data

The script takes approximately half an hour to run.
It creates the dedicated sub-folders and generates 72 csv files (size from 30 to 300Mo) with the relevant HILDA+ data encoded in csv files.

#### 3. Alteryx Workflow Steps
Open Alteryx Designer.

Run:
```bash
1_Country_mapping_HILDA-csv.yxmd
```
The script takes app. two hours to run, depending of the configuration of your laptop.
This produced four different yxdb databases (States and Transition, 2 with the geographical coordinates and 2 without). 
Those databases are stored into the designated output folder (\1_Data\1. HILDA data\2. Aggregating_data).
- HILDA_V_2_1_Transition_Tagged_data_Alteryx_DB_centroid.yxdb (2.6 Go)
- HILDA_V_2_1_Transition_data_Alteryx_DB_limited.yxdb  (1.1 Go)
- HILDA_V_2_1_State_data_Alteryx_DB_limited.yxdb (0.8 Go)
- HILDA_V_2_1_State_Tagged_data_Alteryx_DB_centroid.yxdb (0.4 Go)

Your HILDA+ data are now prepared to be merged with the FAO data (see Second Step below). 

#### 4. Splitting HILDA+ data per AgroEcologicalZone

The HILDA data needs to be split per agroecological zone regarding the CGE modelling. 

Go to the folder: 
1_Data\1. HILDA data\3. Split_AEZ
The agroecological zone from the FAO website are stored in the folder: GAEZ_from_FAO_data  (cf. SI document for further information about them). 

They have been prepared with ArcGIS and the shapes are stored in the database: A-4_aez_global_grid_polygons.yxdb
(This can be controlled via the tableau Figure_S4.twb Figure S4 in the same folder).

Then, run the following Alteryx file:
```bash
B-1_Spatial-match_HILDA_AEZ.yxmd
```
The script takes app. two hours to run, depending of the configuration of your laptop.

These create the following databases:
- C-2_HILDA_V_2_1_State_GTAP_AEZ_Centroid.yxdb (1.0 Go)
- C-2_HILDA_V_2_1_State_GTAP_AEZ_limited.yxdb (300 Mo)
- C-2_HILDA_V_2_1_Transition_GTAP_AEZ_limited.yxdb (300 Mo)
- C-2_HILDA_V_2_1_Transition_GTAP_AEZ_Centroid.yxdb (1.0 Go)

The HILDA data are now prepared for the CGE part also.

## Second step, preparing FAO data

Unzip the file named: 'Production_Crops_Livestock_E_All_Data_(Normalized).zip' located in the folder ...\1_Data\2. FAO data\1. Production_Crops_Livestock_E_All_Data_(Normalized)
Copy the unzipped file from '\1_Data\2. FAO data\1. Production_Crops_Livestock_E_All_Data_(Normalized)\Production_Crops_Livestock_E_All_Data_(Normalized)' to '\1_Data\2. FAO data\1. Production_Crops_Livestock_E_All_Data_(Normalized)'

*Remark: If necessary this file can be dowloaded from FAO dataset*:  
Go to FAO Crops and livestock products: https://www.fao.org/faostat/en/#data/QCL  
Download the serie called: All data Normalized: https://bulks-faostat.fao.org/production/Production_Crops_Livestock_E_All_Data_(Normalized).zip  
Unzip the downnload into the folder: 1_Data/2. FAO data/

Run the following Alteryx scripts:
```bash
A_FAO_annual_evolution_per_GLORIA_sector.yxmd
```
This finishes preparing the forest area evolution per GLORIA MRIO sector with a particular focus on the incremental positive changes.  
The results are stored into the file: 'A-3_Output_FAO_annual_evolution_per_sector_October_2024_GLORIA.xlsx' with the different columns: 
- A: Area Code (UN official M49 area code https://unstats.un.org/unsd/methodology/m49/)
- B: Area Name
- C: Year (all years between 2000 and 2020)
- D: Simple Moving Average (SMA). See Suplementary Information for further information.
- F: Positive area annual evolution
- G: MRIO econmic sector


## Third step, preparing MRIO data
In the same folder, 1. Data\2. FAO data

Run the following Alteryx scripts:
```bash
B_GLORIA_Satellite_data.yxmd

```
This finishes preparing all MRIO-related inputs, calcuting the deforestation per country, sector, and year.
They are all stored in the following folder: 
2. MRIO\GLORIA\commodity\HILDA\V_2_1

## Contact & Support
For HILDA+ dataset questions: refer to the official documentation or contact the dataset authors.
For Python/Alteryx code questions: email etber@mit.edu.

## References
Winkler, Karina; Fuchs, Richard; Rounsevell, Mark D A; Herold, Martin (2020): HILDA+ Global Land Use Change between 1960 and 2019 [dataset].
PANGAEA. https://doi.org/10.1594/PANGAEA.921846
