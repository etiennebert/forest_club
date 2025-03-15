# Step 3: CGE Calculation

The first step in the CGE analysis is to **calculate the deforestation coefficient**, as explained in **Equation 11** of the main manuscript.

---

## 1. Generating Deforestation Coefficients

### Alteryx Workflows
Navigate to the folder:1_Data\3. GTAPAEZ_Deforestation_coefficient
and run both Alteryx workflows:
```bash
A_GTAPAEZ_deforestation_coefficients_Dec_2024_def_ctl.yxmd
B_GTAPAEZ_deforestation_coefficients_Dec_2024.yxmd
'''

Output Files
These scripts generate five Excel files:

A-1_Database_Forest_Intensity_GTAPAEZ_shocks_Deforestation.xlsx

HILDA+ deforestation measured per AEZ, per country, per sector, and year.
A-2_Database_Forest_Intensity_GTAPAEZ_shocks_Land_Change_ctl.xlsx

HILDA+ land cover data measured per AEZ and year for the cattle sector.
B-1_Database_Forest_Intensity_GTAPAEZ_shocks_Land_Change_agri.xlsx

HILDA+ land cover data measured per AEZ and year for other agricultural sectors (excluding cattle).
A-3_Database_Forest_Intensity_GTAPAEZ_shocks_LU_ctl.xlsx

Annual incremental HILDA+ land cover data per AEZ and year for the cattle sector.
B-2_Database_Forest_Intensity_GTAPAEZ_shocks_LU_agri.xlsx

Annual incremental HILDA+ land cover data per AEZ and year for other agricultural sectors (excluding cattle).
These files are consolidated into:

Copier
Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx
2. Calculating the Deforestation Coefficient
Inside Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx, you will find two key tabs:

Additional_LU_and_deforestation
Land_Cover
Using these tabs, you can calculate the deforestation coefficient as described in the main manuscript (Equation 11).

Sheet 3 in this workbook summarizes the computed deforestation coefficients.
Sheet 4 applies those GTAP coefficients to the initial GTAP land areas to calculate deforestation intensity by country and sector (columns BM to BU).
Deforestation Coefficient
Represents the fraction of agricultural land expansion attributable to deforestation in each AEZ for each crop. It is used to guide land-use decisions in the CGE model (see SI 5.2 for additional details).

3. Computing Tariffs for Deforestation-Linked Exports
As described in SI, Section 6.2, tariffs are computed to reduce each producer country’s exports by the share of production linked to deforestation:

These tariffs are computed in the Shocks_GlobalTarf_qxw tab.
They are then integrated into the simulation workflows located in:
php-template
Copier
<Specify folder or filename if applicable>
The resulting data can be found in:
lua
Copier
<Specify the corresponding output file>
The country-level coefficients for these tariffs are defined in Shock_Global_Tarf_qw.
This file is used in further computations, producing Shocks_tmf_f and other relevant shock results.

4. Final Shock Files
The three shocks files (deforestation coefficients + tariff adjustments) are ultimately stored in:

markdown
Copier
3. runGTAP375\Game_theory_2024\0_External_data
These files include:

qo_values.xlsx
qoes_values.xlsx
qxw_values.xlsx
They are then utilized in the CGE model to capture the impact of deforestation on land expansion, trade flows, and corresponding policy interventions.

Summary
Deforestation Coefficients are generated and consolidated through Alteryx scripts, stored in Database_Forest_Intensity_GTAPAEZ_shocks_final.xlsx.
Tariffs related to deforestation-linked production are computed and used in subsequent CGE simulations.
The final shock files (qo_values.xlsx, qoes_values.xlsx, qxw_values.xlsx) are placed in 3. runGTAP375\Game_theory_2024\0_External_data, ready for input into the CGE model.
For any additional details or references, please consult the main manuscript (Equation 11, SI 5.2, SI 6.2) or the corresponding Alteryx workflows.

Copier




