# Forest Club – Supplementary Information

This repository provides supplementary information, data workflows, and scripts for the study:

A trade-based Forest Club as a path to halting Tropical deforestation  
Etienne Berthet(1,2,3)*, Ilaria Fusacchia(4), Alessandro Antimiani(5), Jennifer Morris(1), and Alexis Laurent(2,3)

(1) MIT Center for Sustainability Science and Strategy, Massachusetts Institute of Technology; Cambridge, MA 02139, USA  
(2) Department of Environmental and Resource Engineering, Technical University of Denmark; Kongens Lyngby, 2800, Denmark  
(3) Center for Absolute Sustainability, Technical University of Denmark; Kongens Lyngby, 2800, Denmark  
(4) Department for Humanistic, Scientific, and Social Innovation, University of Basilicata; Potenza, 85100, Italy  
(5) Directorate-General for Trade, European Commission; Brussels, 1000, Belgium

Corresponding author: etber@mit.edu

---

## Overview

This repository accompanies the manuscript’s Supplementary Information (SI) and outlines the methodologies, data workflows, and computational steps used to:
- Quantify tropical deforestation driven by agricultural production and trade (using HILDA+ and FAO data).
- Assign deforestation hotspots to specific crops and livestock (via FAO’s area-harvested and livestock data).
- Estimate consumption- and throughflow-based deforestation footprints in a Multi-Regional Input-Output (MRIO) framework (GLORIA dataset).
- Implement and assess a Computable General Equilibrium (CGE) model (GTAP–AEZ) for counterfactual simulations of the so-called “Forest Club.”

The aim of this README is to navigate the folder structure, replicate the analyses, and locate important scripts and data files.
The current files provides an overview. The detailed execution of the worklow is mentionned in each specific folder. 

---

## Project Directory Structure

```text
├── 1. Data
│   ├── 1. HILDA data
│   │   ├── 1. Extracting_ntcdf_data
│   │   ├── 2. Aggregating_data
│   │   └── 3. Split_AEZ
│   ├── 2. FAO data
│   │   └── 1. Production_Crops_Livestock_E_All_Data_(Normalized)
│   ├── 3. GTAPAEZ_Deforestation_coefficient
│   │   └── 1. GTAPAEZ_Data
│   ├── 4. Suitability
│   └── **README_DATA.md <-- Step 1**
│
├── 2. MRIO
│   ├── GLORIA
│   │   ├── commodity
│   │   ├── output
│   │   │   ├── CBA
│   │   │   └── TBA
│   │   └── (additional files)
│   ├── visualizations
│   │   └── (additional files)
│   └── **README_MRIO.md <-- Step 2**
│
├── 3. CGE
│   ├── Game_Theory_2024
│   │   ├── 0_External_data
│   │   ├── 1_Code
│   │   ├── B_GLORIA_Satellite_data.yxmd
│   │   ├── 3_Output
│   │   ├── DB_GTAPAEZ_all.yxmd
│   │   ├── DB_GTAPAEZ_aggregate.yxmd
│   │   └── (experiment files, .prm parameter files, etc.)
│   └── **README_CGE.md <-- Step 3**
│
└── README.md  <-- You are here!
```

## Key Directories

- **`1. Data`**  
  Raw and processed input data:  
  - **HILDA+**: netCDFs, CSV extractions, and shapefiles.  
  - **FAO**: area/production/livestock files.

- **`2. MRIO`**   
  - Code to compute the CBA/TBA results.

- **`3. CGE`**  
  CGE model files, parameter sets, and results for the Forest Club simulations.
---

## Getting Started

### 1. Clone or Download
git clone https://github.com/YourUserName/Forest_Club_Supplementary_Information.git
(You need to clone this folder in a place directly located in your C:\
(Avoid any path such as: "C:\\xxx\documents\My doc \ etc" any space in the path would create inconsistent run

### 2. Software Requirements
- **Python (3.8+)**  
  For scripts like `1_HILDA_code_extraction.py`, `CBA_TBA_script.py`, etc.  
  Install commonly used libraries: `xarray`, `numpy`, `pandas`, `scipy`.

- **Alteryx Designer** https://www.alteryx.com/products/alteryx-designer
  (optional if you replicate the data pipelines differently)  
  Required to run `.yxmd` workflows.

- **GEMPACK** https://www.copsmodels.com/gempack.htm
  (with Fortran compiler)  
  Necessary to run the **GTAP–AEZ** model for the counterfactual simulations.

- **R** (4.0+)  
  - Some analysis (game-theory logic) is in R scripts.  
  - **HARr** package to parse `.har` outputs from GEMPACK.

- **Tableau** https://www.tableau.com/
 (optional)  
  We used `.twb` workbooks for certain visualizations.

---

### Data Preparation

Main Goals: 

1. **Extract HILDA+**  
   - Acquire **HILDA+ v2.1** data (`.nc` files).  
   - Run `1_HILDA_code_extraction.py` to filter tropical regions and relevant LULC codes.  
   - Convert to CSV or Alteryx format for further analysis.

2. **Process FAO**  
   - Raw files go in `1. Data/2. FAO data/1. Production_Crops_Livestock_E_All_Data_(Normalized)`.  
   - `A_FAO_annual_evolution_per_GLORIA_sector.yxmd` (Alteryx) aggregates yearly data and smooths fluctuations.  
   - Merge with HILDA+ expansions to get sector-level deforestation intensities.

3. **Prepare the HILDA+ and FAO data processed**
   - Prepare the processeded data for the MRIO GLORIA 

The differents steps of this stage are detailed in the document **README_DATA.md <-- Step 1**

---

## Running the MRIO and TBA

1. **Consumption-Based Accounting (CBA)**  
   - `CBA_TBA_script.py` builds the Leontief inverse and multiplies by deforestation intensities.  
   - Outputs stored in `./2. MRIO/GLORIA/output/CBA`.

2. **Throughflow-Based Accounting (TBA)**  
   - Also handled by `CBA_TBA_script.py` using the Hypothetical Extraction Method.  
   - Results in `./2. MRIO/GLORIA/output/TBA`.

3. **Visualizations**  
   - Alteryx workflow `1_HILDA_v2-1_CBA results.yxmd` merges final CBA results.  
   - `CBA_Visualisation.twb` (Tableau) or other tools for charts and maps.

The differents steps of this stage are detailed in the document **README_MRIO.md <-- Step 2**

---

## GTAP–AEZ Counterfactual Analysis

1. **Tariff Simulation**  
   - **`5. Tariff_SIM`** folder contains `.prm` files to find tariffs needed to reduce exports (or output) by the share of deforestation.  
   - Run with GEMPACK, then parse `.har` results with `HARr` in R.

2. **Forest Club Iterations**  
   - The game-theory logic is in `CGE_Game_Theory_GTAPAEZ.R`.  
   - Adjust thresholds in `Thresholds_GTAPAEZ_Game_theory.xlsx`.  
   - Each iteration re-runs the CGE with updated membership decisions and outputs new `.har` result files.

3. **Aggregating Results**  
   - Use Alteryx workflows `DB_GTAPAEZ_all.yxmd` and `DB_GTAPAEZ_aggregate.yxmd` to combine iteration-by-iteration data.  
   - Key outputs include:
     - `DB_GTAPAEZ_Forest_2024.csv` (forest area changes)
     - `DB_GTAPAEZ_EV_2024.csv` (welfare changes)
     - `DB_GTAPAEZ_all_results_2024_agg.csv` (aggregate iteration results).

The differents steps of this stage are detailed in the document **README_MRIO.md <-- Step 2**

---

## Key Outputs

- **`Deforestation_Transiting_EU27_2012-2019.xlsx`**  
  TBA-based re-export deforestation data.  

- **`CBA_Results_Full.csv`**  
  Final consumption-based deforestation footprints.  

- **`DB_GTAPAEZ_Forest_2024.csv`**  
  Net forest area changes at the AEZ level, post-tariff or membership scenario.  

- **`DB_GTAPAEZ_EV_2024.csv`**  
  Welfare (Equivalent Variation) changes.  

- **`DB_Main_Figure_areas_Global_Results.xlsx`**  
  Summaries of net vs. gross forest changes under varied scenarios.  

---

## References

1. Winkler, K., Fuchs, R., Rounsevell, M. & Herold, M. (2021). Global land use changes are four times greater than previously estimated. *Nature Communications* **12**, 2501.  
2. Pendrill, F. et al. (2019). Agricultural and forestry trade drives large share of tropical deforestation emissions. *Global Environmental Change* **56**, 1–10.  
(Additional references in the Supplementary Information file.)

---

## License

Unless stated otherwise, this project is under the MIT License.  
Check **HILDA+**, **FAO**, and **GTAP** license terms for their specific policies.

---

## Contact

For questions, please contact the corresponding author:

**etber@mit.edu**

Or open an issue on GitHub if you encounter any problems or have suggestions.

**Enjoy exploring the data and replicating our Forest Club analysis!**
