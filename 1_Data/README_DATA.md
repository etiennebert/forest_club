# Data Usage Guide

## First step, working with HILDA+ data

### Downloading HILDA+ (Version 2.1)
This project utilizes the HILDA+ Global Land Use Change dataset (1960–2019). 
Winkler, Karina; Fuchs, Richard; Rounsevell, Mark D A; Herold, Martin (2020):
HILDA+ Global Land Use Change between 1960 and 2019 [dataset].
PANGAEA. https://doi.org/10.1594/PANGAEA.921846

The latest version (2.1) can be downloaded from:
https://bwsyncandshare.kit.edu/s/H2iQG6nMPTaxpqR/download

### Required Files
To ensure proper functionality, please download the following NetCDF files:

- hildaplus_GLOB-2-1-crop_states.nc
- hildaplus_GLOB-2-1-crop_transitions.nc

These contain the global crop states and transitions needed for the analysis.

### Usage Instructions
Place the downloaded files in the appropriate directory (e.g., 1_Data/1. HILDA data/1. Extracting_ntcdf_data/1. HILDA_NTCDF_data).
Install any dependencies required to read NetCDF files (for example, netCDF4, numpy, pandas).
Load the data in your workflow using Python or any other tool that handles NetCDF.

#### 1. Python Environment
Install Pyton and the required libraries:
```bash
conda install numpy pandas netCDF4 os
# or
pip install numpy pandas netCDF4 os
```

#### 2. Run the HILDA Extraction Script
Open the terminal
Navigate to the folder:
1_Data\1. HILDA data\1. Extracting_ntcdf_data\1. HILDA_NTCDF_data

Run the Python script:
```bash
python 1_HILDA+_code_extraction.py
```
This will generate extracted data in subfolders under:
1_Data\1. HILDA data\1. Extracting_ntcdf_data

(The script takes approximately half and hour to run).

#### 3. Alteryx Workflow Steps
Open Alteryx Designer.

Run:
```bash
1_Country_mapping_HILDA-csv.yxmd
```
This stores data in the designated output folder (2. Aggregating_data).

Then run in this specific order:
```bash
A-1_Alteryx_AEZ_Marked_Country.yxmd
A-4_aez_global_grid_polygons.yxdb
B-1_Spatial-match_HILDA_AEZ.yxmd
```

These create the following databases:
- C-2_HILDA_V_2_1_State_GTAP_AEZ_limited.yxdb
- C-2_HILDA_V_2_1_Transition_GTAP_AEZ_limited.yxdb

Your HILDA data is now prepared.

## Second step, preparing FAO data

Download the FAO dataset:  

Unzip it to 1_Data/2. FAO data/ (or a similar folder).

Run the following Alteryx scripts:
```bash
A_FAO_annual_evolution_per_GLORIA_sector.yxmd
B_GLORIA_Sattelite_data.yxmd
A_GTAPAEZ_deforestation_coefficients_Dec_2024_def_ctl.yxmd
B_GTAPAEZ_deforestation_coefficients_Dec_2024.yxmd
```
This prepares all FAO-related inputs.


## Third step, preparing FAO data
(Include any MRIO data processing steps here, if needed.)

## Contact & Support
For HILDA+ dataset questions: refer to the official documentation or contact the dataset authors.
For Python/Alteryx code questions: email etber@mit.edu.

