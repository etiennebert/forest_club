# Step 2: CBA and TBA Analysis with MRIO GLORIA

Thanks to the previous data preparation, **your prepared CSV files of Step 1** should be in the folder: 2. MRIO\GLORIA\commodity\HILDA\V_2_1

Before running the MRIO Python code, the raw **GLORIA data** must also be stored in the folder 2_MRIO\GLORIA\data to ensure smooth integration of the workflow.

---

## GLORIA Data Usage Guide

### Dataset Reference
The **GLORIA (Global Resource Input-Output Assessment)** database is a Multi-Regional Input-Output (MRIO) database developed using the IELab infrastructure by the University of Sydney for the UN International Resource Panel (UN IRP). It was created to update material footprint accounts within the UN IRP Material Flows Database. 

### Request Link
**GLORIA Data**:  
[https://ielab.info/labs/ielab-gloria](https://ielab.info/labs/ielab-gloria)
(The creation of an account is requested to have access to the data) 

### Technical Documentation
Additionally to the raw data, the GLORIA technical documentation outlines:

- The construction methodology of the MRIO table  
- The source datasets used  
- Quality checks performed  
- Method- and data-specific details  

It includes **material footprint** calculations and a wide range of environmental, economic, and social indicators.

> **Note**: GLORIA data **cannot be used for commercial purposes** without a valid license from FootprintLab.

---

## Required Data Files
For calculations covering **2012–2019**, you will need:

1. **Transactions Matrix (T-Results)**  
20240111_120secMother_AllCountries_002_T-Results_xxxx_059_Markup001(full).csv (app. 6.2 Go per year)

2. **Final Demand Matrix (Y-Results)**  
20240111_120secMother_AllCountries_002_Y-Results_xxxx_059_Markup001(full).csv (app. 226 Mo per year)

---

## Usage Instructions

1. **Download** the required datasets from the link provided above.  
2. **Ensure** you have following Python library: scipy, os and gc 
3. **Load and calculate** it integrates the transactions (T-Results) and final demand (Y-Results) matrices into your workflow and perform the calcuations.

**Remark**:  
- The first time you run the script, these large CSV files (over 10 GB) are converted into NumPy (`.npy`) format for faster subsequent data loading.  
- Afterwards, loading the data becomes much quicker.

---

## Running the Scripts

### 1. CBA & TBA for the EU27
This concerns only the deforestation consumed in the EU27 and going "through" the EU27 (cf. main manuscript). 
Run the script:
'''
CBA_TBA_scriptEU27.py
'''
This performs **Consumption-Based Accounting (CBA)** and **Trade-Based Accounting (TBA)** for the EU27 only. It iterates over **11 producer countries**, and **each year** (2012–2019) can take about **2 to 3 hours** per year to process.

### 2. Global CBA & TBA
This concerns only the deforestation consumed in the EU27 and going "through" the EU27 (cf. main manuscript). 

Next, run:
'''
CBA_TBA_scriptglobal.py
'''
- This script is set to run on **3 producer countries** (see SI for details) due to high computational demands.
- Even on a HPC (High-Performance Computing) system, it can take about **1 day** per country.

**All results** are automatically stored in the `output` folder.

---

## Consolidating Results in Alteryx
Once the MRIO scripts are finished:

1. Go to the Alteryx folder:
full_database

2. Run the relevant Alteryx workflow(s) to consolidate all generated results into a single database.

---

## Visualization
Finally, visualize the consolidated database in the `visualisation` folder via a **straightforward** process (details may vary depending on your visualization tool).

---

## Contact & Support
- **GLORIA Technical Details**: Refer to the documentation or contact the University of Sydney IELab team for further support.  
- **MRIO/Script Queries**: Email [etber@mit.edu](mailto:etber@mit.edu).
