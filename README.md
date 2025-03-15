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

---

## Repository Structure

.  
├── 1. Data  
│   ├── 1. HILDA data  
│   │   ├── 1. Extracting_ntcdf_data  
│   │   ├── 2. Aggregating_data  
│   │   └── 3. Split_AEZ  
│   ├── 2. FAO data  
│   │   └── 1. Production_Crops_Livestock_E_All_Data_(Normalized)
│   ├── 3. GTAPAEZ_Deforestation_coefficient  
│   │   └── 1. GTAPAEZ_Data
│   └── 4. Suitability  
│
├── 2. MRIO  
│   ├── GLORIA  
│   │   ├── commodity  
│   │   ├── output  
│   │   │    ├── CBA  
│   │   │    └── TBA 
│	│	├── output 
│	│	└── (additional files)  
│   └── visualizations
│		└── (additional files)  
├── 3. CGE  
│   └── Game_Theory_2024 
│	    ├── 0_External_data 
│	    ├── 1_Code
│	    ├── B_GLORIA_Satellite_data.yxmd  
│	    ├── 3_Output
│	    ├── DB_GTAPAEZ_all.yxmd  
│	    ├── DB_GTAPAEZ_aggregate.yxmd  
│       └── (experiment files, .prm parameter files, etc.)
└── README.md  <-- You are here!


├── 5. Tariff_SIM  
│   └── (experiment files, .prm parameter files, etc.)  
├── output  
│   ├── DB_GTAPAEZ_all_results_2024.csv  
│   ├── Deforestation_Transiting_EU27_2012-2019.xlsx  
│   └── (additional outputs)  




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


### 2. Software Requirements
- **Python (3.8+)**  
  For scripts like `1_HILDA_code_extraction.py`, `CBA_TBA_script.py`, etc.  
  Install commonly used libraries: `xarray`, `numpy`, `pandas`, `scipy`.

- **Alteryx Designer** (optional if you replicate the data pipelines differently)  
  Required to run `.yxmd` workflows.

- **GEMPACK** (with Fortran compiler)  
  Necessary to run the **GTAP–AEZ** model for the counterfactual simulations.

- **R** (4.0+)  
  - Some analysis (game-theory logic) is in R scripts.  
  - **HARr** package to parse `.har` outputs from GEMPACK.

- **Tableau** (optional)  
  We used `.twb` workbooks for certain visualizations.

---

### Data Preparation

1. **Extract HILDA+**  
   - Acquire **HILDA+ v2.1** data (`.nc` files).  
   - Run `1_HILDA_code_extraction.py` to filter tropical regions and relevant LULC codes.  
   - Convert to CSV or Alteryx format for further analysis.

2. **Process FAO**  
   - Raw files go in `1. Data/2. FAO data/1. Production_Crops_Livestock_E_All_Data_(Normalized)`.  
   - `A_FAO_annual_evolution_per_GLORIA_sector.yxmd` (Alteryx) aggregates yearly data and smooths fluctuations.  
   - Merge with HILDA+ expansions to get sector-level deforestation intensities.


## Detailed Instructions to prepare the data


### 1.1 Dataset Reference
We utilize the **HILDA+ Global Land Use Change** dataset (1960–2019).  
**Citation**  
Winkler, Karina; Fuchs, Richard; Rounsevell, Mark D A; Herold, Martin (2020):  
*HILDA+ Global Land Use Change between 1960 and 2019 [dataset]*.  
PANGAEA. [DOI: 10.1594/PANGAEA.921846](https://doi.org/10.1594/PANGAEA.921846)

### 1.2 Required Files
- **hildaplus_GLOB-2-1-crop_states.nc**  
- **hildaplus_GLOB-2-1-crop_transitions.nc**

### 1.3 Usage Instructions
1. **Place** the NetCDF files under: 1_Data/1. HILDA data/1. Extracting_ntcdf_data/1. HILDA_NTCDF_data

2. **Install** netCDF support (as above).
3. **Load** or process data in Python, Alteryx, or R, etc.

### 1.4 Contact & Support
- HILDA+ dataset: official documentation / authors.  
- Python code: **etber@mit.edu**.

---

## 2. Running HILDA+ Extraction & Spatial Processing

1. **Set Working Directory** to:1_Data/1. HILDA data/1. Extracting_ntcdf_data/1. HILDA_NTCDF_data

1_Data/1. HILDA data/1. Extracting_ntcdf_data

markdown
Copier
Modifier
3. **Run in Alteryx**:
1_Country_mapping_HILDA-csv.yxmd

markdown
Copier
Modifier
to attach country metadata to CSVs.

### 2.1 Spatial Matching with AEZ
Now run in Alteryx, in order:
1. **A-1_Alteryx_AEZ_Marked_Country.yxmd**
2. **A-4_aez_global_grid_polygons.yxdb**
3. **B-1_Spatial-match_HILDA_AEZ.yxmd**

These generate:
C-2_HILDA_V_2_1_State_GTAP_AEZ_limited.yxdb C-2_HILDA_V_2_1_Transition_GTAP_AEZ_limited.yxdb

yaml
Copier
Modifier
Your HILDA+ data is fully prepared at this point.

---

## 3. Detailed FAO Steps (Recap)

1. Place raw FAO files in:
1_Data/2. FAO data/1. Production_Crops_Livestock_E_All_Data_(Normalized)

yaml
Copier
Modifier
2. Run in Alteryx:
- `A_FAO_annual_evolution_per_GLORIA_sector.yxmd`
- `B_GLORIA_Sattelite_data.yxmd`
- For GTAP-AEZ deforestation coefficients:
  - `A_GTAPAEZ_deforestation_coefficients_Dec_2024_def_ctl.yxmd`
  - `B_GTAPAEZ_deforestation_coefficients_Dec_2024.yxmd`

---

## 4. MRIO Data Integration

After both HILDA+ and FAO data are processed:

1. **Load** MRIO (GLORIA) or a similar dataset:

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

## Citation

If you use this code or data, please cite the original paper:

Berthet, E. et al. (20XX). *A trade-based Forest Club as a path to halting Tropical deforestation*.

And reference the GitHub repository:


---

## Contact

For questions, please contact the corresponding author:

**etber@mit.edu**

Or open an issue on GitHub if you encounter any problems or have suggestions.

**Enjoy exploring the data and replicating our Forest Club analysis!**
