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
Inside the file Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx, using the following tabs:

- Additional_LU_and_deforestation
- Land_Cover

It is possbile to calculate the deforestation coefficient as described in the main manuscript (Equation 11).

*(Reminder: this coefficient represents the fraction of agricultural land expansion attributable to deforestation in each AEZ for each crop, see SI 5.2 for additional details)*.

The calcualtion of those deforestation coefficents is perfomred tab **Additional_LU_and_deforestation**, column G

**Sheet 3** in this workbook summarizes the computed deforestation coefficients.
**Sheet 4** applies those deforestation coefficients to the initial GTAP land areas to calculate deforestation intensity by country and sector (columns BM to BU of this tab).

### Computing Tariffs for Deforestation-Linked Exports
As described in SI, Section 6.2, initial tariffs are first computed to reduce each producer country’s exports by the share of production linked to deforestation.

The shocks and swap used for those tariffs are calcuated in the Excel file Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx, tab Shocks_GlobalTarf_qxw. 
Then, the evaluation of those tariffs is done via a GTAP AEZ simulation located within the folder: 3. runGTAP375\5. Tariff_SIM\NATFEB\
The parameters of this specific simualtion can be found in the sub-folder 3. runGTAP375\5. Tariff_SIM\NATFEB\Savesims, file qxwGlobT.cmf (with the same swap and shocks values than the ones in the Excel file Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx, tab Shocks_GlobalTarf_qxw).

The results of this specific simulation can be found 3. runGTAP375\5. Tariff_SIM\NATFEB\Savesims, file qxwGlobT.sl4 and have been copied and stored stored in the file Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx, tab SShocks_tmf_f

## 2. Final Shock Files
The tariffs calcuated at the previous step are used to scale the decrease of:
- The national output of commodities produced through deforestation.
- The national exports of commodities derived from deforestation (as in the example above).

Last, the decreases the AEZ‐level output of deforestation‐linked commodities is done via the results in Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx, tab sheet4 

As such, those different files are stored in: 3. runGTAP375\Game_theory_2024\0_External_data
These files include:
- qo_values.xlsx (values from the tariffs) 
- qoes_values.xlsx (values from the file Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx, tab sheet4, column BM-BU) 
- qxw_values.xlsx (values from the tariffs)
- tms_f_initial_shocks.xlsx (values from the tariffs) 
Those file are then used in the CGE model simulation to capture the impact of deforestation on land expansion, trade flows, and corresponding policy interventions.

## 3. Running the Simulation

The coefficients and their corresponding shocks and swaps have been calculated (see above). 
Those coefficients as well as the parameter values (Table S6 in the SI) are stored in the subfolders under: C:\runGTAP375\Game_theory_2024\0_External_data

### 3.1 Unzipping the Model Folder
1. **Unzip the `2_Model` folder**. This folder contains:
   - The **GTAP-AEZ executable** used during all iterations,
   - Necessary configuration files,
   - Other files required to run the GEMPACK simulation.
2. **Check `defaut.prm`** for updated elasticity parameters (see SI 5.1). The relevant parameter is `ETRAEL1` (elasticity of transformation between Forestry and Agriculture), based on Miranda et al.

### 3.2 Updating Paths in `NATDEF.cmf`
Within the `NATDEF.cmf` file, **lines 40 and 41** must reflect your chosen file path:
40 Solution file = C:\runGTAP375\Game_theory_2024\2_Model\NATDEF.sl4;
41 Updated file gtapDATA = C:\runGTAP375\Game_theory_2024\2_Model\gdata.upd;
Update these lines as needed.

### 3.3 Running the R Script
- Navigate to the `1_Code` folder and **run the R script**.
- This generates outputs such as `qoes`, `qo`, and `qxw` for each scenario.
- **Oscillation Handling**: The program stops after 25 repeated oscillations, but this limit can be changed.  
- **Simulation Time**: Varies by scenario, typically **1 minute to 1 hour** per iteration.

### 3.4 Consolidating Results
- All outputs are stored in the `4_DB` folder.
- To create a single, consolidated database, **run the two final Alteryx workflows**: 
  - Database_GTAPAEZ_all_results_2024_agg_pivot.yxmd
  - DB_GTAPAEZ_all

- These workflows produce a comprehensive database of results for further analysis or visualization.

## Summary
Deforestation Coefficients are generated and consolidated through Alteryx scripts, stored in Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx.
Tariffs related to deforestation-linked production are computed and used in subsequent CGE simulations.
The final shock files (qo_values.xlsx, qoes_values.xlsx, qxw_values.xlsx) are placed in 3. runGTAP375\Game_theory_2024\0_External_data, ready for input into the CGE model.
For any additional details or references, please consult the main manuscript (Equation 11, SI 5.2, SI 6.2) or the corresponding Alteryx workflows.

