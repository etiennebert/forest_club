# Step 3: GTAP-AEZ simulation within the game theory

---

## 1. Generating Deforestation Coefficients
The first step is is to **calculate the deforestation coefficient**, as explained in **Equation 11** of the main manuscript.

### Alteryx Workflows
Navigate to the folder:1_Data\3. GTAPAEZ_Deforestation_coefficient
and run both Alteryx workflows:
```bash
A_GTAPAEZ_deforestation_coefficients_Dec_2024_def_ctl.yxmd
B_GTAPAEZ_deforestation_coefficients_Dec_2024.yxmd
```

Output Files

These scripts generate five Excel files:

- A-1_Database_Forest_Intensity_GTAPAEZ_shocks_Deforestation.xlsx
  - HILDA+ deforestation measured per AEZ, per country, per sector, and year.
- A-2_Database_Forest_Intensity_GTAPAEZ_shocks_Land_Change_ctl.xlsx
  - HILDA+ land cover data measured per AEZ and year for the cattle sector.
- B-1_Database_Forest_Intensity_GTAPAEZ_shocks_Land_Change_agri.xlsx
  - HILDA+ land cover data measured per AEZ and year for other agricultural sectors (excluding cattle).
- A-3_Database_Forest_Intensity_GTAPAEZ_shocks_LU_ctl.xlsx
  - Annual incremental HILDA+ land cover data per AEZ and year for the cattle sector.
- B-2_Database_Forest_Intensity_GTAPAEZ_shocks_LU_agri.xlsx
  - Annual incremental HILDA+ land cover data per AEZ and year for other agricultural sectors (excluding cattle).

These results are consolidated into an Excel file within the same folder: Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx

### Calculating the Deforestation Coefficient
Inside Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx, you will find two key tabs:

- Additional_LU_and_deforestation
- Land_Cover
Using these tabs, you can calculate the deforestation coefficient as described in the main manuscript (Equation 11).
(Those coefficents represent the fraction of agricultural land expansion attributable to deforestation in each AEZ for each crop. They are used to guide land-use decisions in the CGE model, see SI 5.2 for additional details).

The calcualtion of those coefficents is perfomred tab **Additional_LU_and_deforestation**, column G

**Sheet 3** in this workbook summarizes the computed deforestation coefficients.
**Sheet 4** applies those GTAP coefficients to the initial GTAP land areas to calculate deforestation intensity by country and sector (columns BM to BU).

### Computing Tariffs for Deforestation-Linked Exports
As described in SI, Section 6.2, tariffs are first computed to reduce each producer country’s exports by the share of production linked to deforestation:
The shocks and swap used for those tariffs are computed in the file Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx, tab Shocks_GlobalTarf_qxw. 
This file is used in further computations, producing Shocks_tmf_f and other relevant shock results.
Then, the calcuation of the tariffs is done via a GTAP AEZ simulation done via the folder: 
3. runGTAP375\5. Tariff_SIM\NATFEB\SaveSims
The parameter of this simualtion can be foun in the folder Savesims. 
simulation is available in the SI and can be recomputed using the “\5. Tariff_SIM” folder (name of the experiment: qxwGlobT “aggregate shock on qxw for global tariffs”), which yields the average tariff required to curtail each export flow in proportion to its deforestation footprint
And the value found in the file qxwGlobT.cmf are the same than the ones in the file. 

Teh results are in the file qxwGlobT.sl4 and stored in the file Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx, tab SShocks_tmf_f

## Final Shock Files
The three shocks files (deforestation coefficients + tariff adjustments) are ultimately stored in:

3. runGTAP375\Game_theory_2024\0_External_data
These files include:

qo_values.xlsx
qoes_values.xlsx
qxw_values.xlsx
They are then utilized in the CGE model to capture the impact of deforestation on land expansion, trade flows, and corresponding policy interventions.

## Running the Simulation. 
The coefficents have been calcuated. 
The Parameters located Table S6 of the SI are stored in the sub folder located at: C:\runGTAP375\Game_theory_2024\0_External_data

To run the simuation, it first necessary to unzip the 2_Model folder, then to run R script located at 1_Code. 
This will generate different output for qoes, qo, and qxw for each of the scenario considered. 
The program is defined to stop after a phase of 25 similar oscialltion but this can be extensede. 

The simulaiton time can vary significantly between scenario as it can be between 1 min and 1 hour per iteration. 

LAst, Some of the resutls are stored in the 4_DB folder. 
By running the two last ALteryx Workflow: 
- Database_GTAPAEZ_all_results_2024_agg_pivot.yxmd
- DB_GTAPAEZ_all

all the results can be calcualted. 


Summary
Deforestation Coefficients are generated and consolidated through Alteryx scripts, stored in Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx.
Tariffs related to deforestation-linked production are computed and used in subsequent CGE simulations.
The final shock files (qo_values.xlsx, qoes_values.xlsx, qxw_values.xlsx) are placed in 3. runGTAP375\Game_theory_2024\0_External_data, ready for input into the CGE model.
For any additional details or references, please consult the main manuscript (Equation 11, SI 5.2, SI 6.2) or the corresponding Alteryx workflows.





