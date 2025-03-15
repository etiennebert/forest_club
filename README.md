# A trade-based Forest Club as a path to halting Tropical deforestation – Code and data

This repository provides supplementary information, data workflows, and scripts for the study:

A trade-based Forest Club as a path to halting Tropical deforestation  
Etienne Berthet<sup>1,2,3,*</sup>, Ilaria Fusacchia<sup>4</sup>, Alessandro Antimiani<sup>5</sup>, Jennifer Morris<sup>1</sup>, and Alexis Laurent<sup>2,3</sup>

<sup>1</sup> MIT Center for Sustainability Science and Strategy, Massachusetts Institute of Technology; Cambridge, MA 02139, USA  
<sup>2</sup> Department of Environmental and Resource Engineering, Technical University of Denmark; Kongens Lyngby, 2800, Denmark  
<sup>3</sup> Center for Absolute Sustainability, Technical University of Denmark; Kongens Lyngby, 2800, Denmark  
<sup>4</sup> Department for Humanistic, Scientific, and Social Innovation, University of Basilicata; Potenza, 85100, Italy  
<sup>5</sup> Directorate-General for Trade, European Commission; Brussels, 1000, Belgium

*Corresponding author: etber@mit.edu

---

## Overview

This repository accompanies the manuscript’s Supplementary Information (SI) and outlines the methodologies, data workflows, and computational steps used to:
- Quantify tropical deforestation driven by agricultural production and trade (using HILDA+ and FAO data).
- Quantify consumption- and throughflow-based deforestation footprints thanks to a Multi-Regional Input-Output (MRIO) framework (GLORIA dataset).
- Implement and assess a Computable General Equilibrium (CGE) model (GTAP–AEZ) for counterfactual simulations of the so-called “Forest Club.”

The aim of this README is to navigate the folder structure, replicate the analyses, and locate important scripts and data files.
The current files provide an overview. The detailed execution of the workflow is mentioned in each specific folder. 

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
│   ├── Visualizations
│   │   └── (additional files)
│   └── **README_MRIO.md <-- Step 2**
│
├── 3. CGE
│   ├── Game_Theory_2024
│   │   ├── 0_External_data
│   │   ├── 1_Code
│   │   ├── 2_Model.zip (experiment files, .prm parameter files, etc.)
│   │   ├── 3_Output
│   │   ├── 4_DB
│   │   └── 5_Visualisation
│   ├── 5. Tariff_SIM
│   └── **README_CGE.md <-- Step 3**
│
└── README.md  <-- You are here!
```

## Key Directories

- **`1. Data`**  
  Raw and processed input data:  
  - **HILDA+**: netCDFs, CSV extractions, and shapefiles.  
  - **FAO**: agro ecological zone/agricultural production/livestock production.

- **`2. MRIO`**   
  - Code to compute the CBA/TBA results within the MRIO GLORIA.

- **`3. CGE`**  
  CGE model files, parameter sets, and results for the Forest Club simulations.
---

## Getting Started

### 1. Clone or Download
Clone the repository directly onto your C:\ drive to avoid issues with file paths containing spaces. For example:
```text
cd C:\
git clone https://github.com/etiennebert/forest_club.git
```

Note: Do not install it under a path like C:\Users\YourName\Documents if that includes spaces (e.g., My Documents)—this can lead to inconsistent runs or file-not-found errors.

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

## Step 1: Data Preparation

Main Goals: 

1. **Extract HILDA+**  
   - Acquire **HILDA+ v2.1** data (`.nc` files).  
   - Python code `1_HILDA_code_extraction.py` to filter tropical regions of interest and relevant LULC codes.  
   - Convert to CSV or geographical format via Alteryx format for further analysis.

2. **Process FAO**  
   - Raw FAO files about production.  
   - `A_FAO_annual_evolution_per_GLORIA_sector.yxmd` (Alteryx) aggregates yearly incremental changes and smooths fluctuations.  
   - Merge with HILDA+ results to get sector-level deforestation intensities.

3. **Prepare the HILDA+ and FAO data processed**
   - Prepare the processed data for the MRIO GLORIA 

The various steps of this stage are detailed in the document **README_DATA.md <-- Step 1**

---

## Step 2: Running the MRIO analysis

1. **Consumption-Based Accounting (CBA)**  
   - `CBA_TBA_script.py` builds the Leontief inverse and multiplies by deforestation intensities and Final Demand.  
   - Outputs stored in `./2. MRIO/GLORIA/output/CBA`.

2. **Throughflow-Based Accounting (TBA)**  
   - Also handled by `CBA_TBA_script.py`, calculate the "throughflow" of deforestation for the different territories, using the Hypothetical Extraction Method.  
   - Results in `./2. MRIO/GLORIA/output/TBA`.

3. **Visualizations**  
   - Alteryx workflow `1_HILDA_v2-1_CBA results.yxmd` merges final CBA results.  
   - `CBA_Visualisation.twb` (Tableau) or other tools for charts and maps.

The different steps of this stage are detailed in the document **README_MRIO.md <-- Step 2**

---

## Step 3: GTAP–AEZ Counterfactual Analysis

1. **Deforestation coefficients**  
   - Represents the fraction of agricultural land expansion attributable to deforestation in each AEZ for each crop. It is used to guide land-use decisions in the CGE model (see SI 5.2 for additional details).
  
2. **Tariff Simulation**  
   - Find tariffs needed to reduce exports (or output) by the share of deforestation (See SI 6.1).  

3. **Forest Club Iterations**  
   - The game-theory logic is in `CGE_Game_Theory_GTAPAEZ.R`.
   - The R script runs with GEMPACK, then parse `.har` results with `HARr` in R.
   - Possibility to adjust the thresholds in `Thresholds_GTAPAEZ_Game_theory.xlsx` (See SI table S6)   
   - Each iteration re-runs the CGE with updated membership decisions and outputs new `.har` result files.

4. **Aggregating Results**  
   - Use Alteryx workflows `DB_GTAPAEZ_all.yxmd` and `DB_GTAPAEZ_aggregate.yxmd` to combine iteration-by-iteration data.  
   - Key outputs include:
     - `DB_GTAPAEZ_Forest_2024.csv` (forest area changes)
     - `DB_GTAPAEZ_EV_2024.csv` (welfare changes)
     - `DB_GTAPAEZ_all_results_2024_agg.csv` (aggregate iteration results).

The various steps of this stage are detailed in the document **README_CGE.md <-- Step 3**

---

## License

Unless stated otherwise, this project is under the MIT License.  
Check **HILDA+**, **FAO**, **GEMPACK**, **Alteryx**, **Tableau** and **GTAP** license terms for their specific policies.

---

## Contact

For questions, please contact the corresponding author: **etber@mit.edu**

Or open an issue on GitHub if you encounter any problems or have suggestions.

**Enjoy exploring the data and replicating our Forest Club analysis!**
