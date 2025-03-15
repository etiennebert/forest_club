README data
HILDA+ Data Usage Guide
Dataset Reference
This project utilizes the HILDA+ Global Land Use Change dataset, which provides global land-use change data from 1960 to 2019. The dataset is referenced as follows:

Citation:
Winkler, Karina; Fuchs, Richard; Rounsevell, Mark D A; Herold, Martin (2020): HILDA+ Global Land Use Change between 1960 and 2019 [dataset]. PANGAEA.
🔗 https://doi.org/10.1594/PANGAEA.921846

Downloading HILDA+ Version 2.1
The latest version 2.1 of the dataset can be downloaded from:
🔗 https://bwsyncandshare.kit.edu/s/H2iQG6nMPTaxpqR/download

Required Files
To ensure proper functionality, please download the following NetCDF files:

- hildaplus_GLOB-2-1-crop_states.nc
- hildaplus_GLOB-2-1-crop_transitions.nc
These files contain the global crop states and transitions necessary for the analysis.

Usage Instructions
Place the downloaded files in the appropriate directory.
Ensure you have the necessary dependencies installed to read NetCDF files (e.g., xarray, netCDF4 in Python).
Load the data into your workflow using the relevant tools for your analysis.

Contact & Support
For any questions or assistance regarding the dataset, please refer to the official HILDA+ documentation or reach out to the dataset authors via PANGAEA.
For any question regarding the Python code, please refer to etber@mit.edu

Instruction to run the results of the study: 
HILDA+ Data Usage Guide
Dataset Reference
This project utilizes the HILDA+ Global Land Use Change dataset, which provides global land-use change data from 1960 to 2019. The dataset is referenced as follows:

Citation:
Winkler, Karina; Fuchs, Richard; Rounsevell, Mark D A; Herold, Martin (2020): HILDA+ Global Land Use Change between 1960 and 2019 [dataset]. PANGAEA.
🔗 https://doi.org/10.1594/PANGAEA.921846

Downloading HILDA+ Version 2.1
The latest version 2.1 of the dataset can be downloaded from:
🔗 https://bwsyncandshare.kit.edu/s/H2iQG6nMPTaxpqR/download

Required Files
To ensure proper functionality, please download the following NetCDF files:

- hildaplus_GLOB-2-1-crop_states.nc
- hildaplus_GLOB-2-1-crop_transitions.nc
These files contain the global crop states and transitions necessary for the analysis.

Usage Instructions
Place the downloaded files in the appropriate directory.
Ensure you have the necessary dependencies installed to read NetCDF files (e.g., xarray, netCDF4 in Python).
Load the data into your workflow using the relevant tools for your analysis.

Contact & Support
For any questions or assistance regarding the dataset, please refer to the official HILDA+ documentation or reach out to the dataset authors via PANGAEA.
For any question regarding the Python code, please refer to etber@mit.edu

Within Python, install the following enviromets: 
import numpy as np
import pandas as pd
import netCDF4
Run the script 
1_HILDA+_code_extraction.py inside the folder 1_Data\1. HILDA data\1. Extracting_ntcdf_data\1. HILDA_NTCDF_data
This will prepare the data into the folders: 
1_Data\1. HILDA data\1. Extracting_ntcdf_data


In your command file: load the environemtn with the approapriate libraby (ex: 
Then simply run: Python 1_HILDA+_code_extraction.py

Then, in that order run: 

Set the working directory on the same path as the Python script. 
Run the full script. 
Now run the Alteryx Script 1_Country_mapping_HILDA-csv.yxmd
This store the data in your folder 
Then run the following script in that specific order: 
A-1_Alteryx_AEZ_Marked_Country.yxmd
A-4_aez_global_grid_polygons.yxdb
B-1_Spatial-match_HILDA_AEZ.yxmd
This will generate: 
-C-2_HILDA_V_2_1_State_GTAP_AEZ_limited.yxdb 
C-2_HILDA_V_2_1_Transition_GTAP_AEZ_limited
Your HILDA data are now prepared. 
For the FAO data, download the data at: 
Stored the unzip file in: 
run the scpt: 
A_FAO_annual_evolution_per_GLORIA_sector.yxmd 
B_GLORIA_Sattelite_data.yxmd
A_GTAPAEZ_deforestation_coefficients_Dec_2024_def_ctl.yxmd
B_GTAPAEZ_deforestation_coefficients_Dec_2024.yxmd
The data are now prepared. 
MRIO data 

