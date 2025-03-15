# Step 3: GTAP-AEZ Simulation within a Game-Theoretic Framework

---

## 1. Generating Deforestation Coefficients
The first step is to **calculate the deforestation coefficient**, as explained in **Equation 11** of the main manuscript.

### Alteryx Workflows
1. Navigate to the folder: 1_Data\3. GTAPAEZ_Deforestation_coefficient
2. Run both Alteryx workflows:
```bash
A_GTAPAEZ_deforestation_coefficients_Dec_2024_def_ctl.yxmd
B_GTAPAEZ_deforestation_coefficients_Dec_2024.yxmd
```

Output Files

These scripts generate five Excel files:

- `A-1_Database_Forest_Intensity_GTAPAEZ_shocks_Deforestation.xlsx`
  - HILDA+ deforestation measured per AEZ, per country, per sector, and year.
- `A-2_Database_Forest_Intensity_GTAPAEZ_shocks_Land_Change_ctl.xlsx`
  - HILDA+ land cover data measured per AEZ and year for the cattle sector.
- `B-1_Database_Forest_Intensity_GTAPAEZ_shocks_Land_Change_agri.xlsx`
  - HILDA+ land cover data measured per AEZ and year for other agricultural sectors (excluding cattle).
- `A-3_Database_Forest_Intensity_GTAPAEZ_shocks_LU_ctl.xlsx`
  - Annual incremental HILDA+ land cover data per AEZ and year for the cattle sector.
- `B-2_Database_Forest_Intensity_GTAPAEZ_shocks_LU_agri.xlsx`
  - Annual incremental HILDA+ land cover data per AEZ and year for other agricultural sectors (excluding cattle).

These outputs are consolidated into:
```bash
Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx
```

### Calculating the Deforestation Coefficient
Within `Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx`, the following tabs:

- **Additional_LU_and_deforestation**
- **Land_Cover**

are used to calculate the deforestation coefficient as described in the main manuscript (Equation 11).  
*(Note: this coefficient represents the fraction of agricultural land expansion attributable to deforestation in each AEZ for each crop, see SI 5.2 for additional details)*.

The calculation itself is performed in `Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx,` tab **Additional_LU_and_deforestation**, column G.  
Last:
- **Sheet 3** in this workbook summarizes the computed deforestation coefficients.  
- **Sheet 4** applies those deforestation coefficients to the initial GTAP land areas to calculate deforestation intensity by country and sector (columns BM to BU of this tab).

### Computing Tariffs for Deforestation-Linked Exports
As described in SI, Section 6.2, initial tariffs are first computed to reduce each producer country’s exports by the share of production linked to deforestation.

- The shocks and swaps used for those tariffs are calcuated in the Excel file `Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx`, tab Shocks_GlobalTarf_qxw.  
- An initial GTAP-AEZ simulation (in '3. runGTAP375\5. Tariff_SIM\NATFEB\') then evaluates these tariffs. Its parameters are stored in: file qxwGlobT.cmf (These swaps and shock values align with the Shocks_GlobalTarf_qxw tab of the same Excel file above.)
- The output of this simulation is '3. runGTAP375\5. Tariff_SIM\NATFEB\Savesims, file qxwGlobT.sl4' and has been copied into 'Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx', tab Shocks_tmf_f

## 2. Final Shock Files
Following the approach in the SI, we aim to reduce:
1. The national output of commodities produced through deforestation.
2. The national exports of commodities derived from deforestation.
3. The AEZ‐level output of deforestation‐linked commodities.

To operationalize these goals, we use the following files (stored in '3. runGTAP375\Game_theory_2024\0_External_data'):
- qo_values.xlsx (values from the tariffs) 
- qoes_values.xlsx (values from the file 'Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx', tab sheet4, column BM-BU) 
- qxw_values.xlsx (values from the tariffs)

These files are used in the CGE simulation to capture deforestation’s impact on land expansion, trade flows, and related policy interventions.

## 3. Running the Simulation

The necessary coefficients, shocks, and swaps are now in place. The key parameters (Table S6 in the SI) are located in: 'C:\runGTAP375\Game_theory_2024\0_External_data'

### 3.1 Unzipping the Model Folder
1. **Unzip the `2_Model` folder**. This folder contains:
   - The **GTAP-AEZ executable** used during all iterations,
   - Necessary configuration files,
   - Other files required to run the GEMPACK simulation.
2. **Check `default.prm`** if you aim to update elasticity parameters (see SI 5.1). The relevant variable is `ETRAEL1` (elasticity of transformation between Forestry and Agriculture), updated from Miranda et al.

### 3.2 Updating Paths in `NATDEF.cmf`
Within the `NATDEF.cmf` file, **lines 40 and 41** must reflect your chosen file path:
40 Solution file = C:\runGTAP375\Game_theory_2024\2_Model\NATDEF.sl4;
41 Updated file gtapDATA = C:\runGTAP375\Game_theory_2024\2_Model\gdata.upd;
Adjust these paths as necessary.

### 3.3 Running the R Script
- Navigate to the `1_Code` folder and **run the R script**.
- This generates outputs such as `qoes`, `qo`, and `qxw` for each scenario.
- **Oscillation Handling**: The program stops after 25 repeated oscillations, but this limit can be changed.  
- **Simulation Time**: Each iteration takes anywhere from 1 minute to 1 hour, depending on the scenario.

### 3.4 Consolidating Results
- Simulation results are stored in the '4_DB' folder.
- To compile all output into a single, consolidated database, **run the two final Alteryx workflows**:
```bash
  - Database_GTAPAEZ_all_results_2024_agg_pivot.yxmd
  - DB_GTAPAEZ_all
```

## Summary
- Deforestation Coefficients are generated and consolidated through Alteryx scripts, stored in 'Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx'.
- Tariffs related to deforestation-linked production are computed and used in subsequent CGE simulations.
- Shock files (qo_values.xlsx, qoes_values.xlsx, qxw_values.xlsx) are placed in '3. runGTAP375\Game_theory_2024\0_External_data', ready for input into the CGE model.
- For any additional details or references, please consult the main manuscript (Equation 11, SI 5.2, SI 6.2) or the corresponding Alteryx workflows.

## References
Miranda, J., Britz, W. & Börner, J. Impacts of commodity prices and governance on the expansion of tropical agricultural frontiers. Scientific Reports 1–13 (2024) doi:10.1038/s41598-024-59446-0 
