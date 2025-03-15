# Step 2: CBA and TBA Analysis with MRIO GLORIA

Thanks to the previous data preparation, **your prepared CSV files from Step 1** should be located in: 2. MRIO\GLORIA\commodity\HILDA\V_2_1

Before running the MRIO Python code, **the raw GLORIA data** must also be stored in: 2_MRIO\GLORIA\data to ensure smooth integration of the workflow.

---

## GLORIA Data Usage Guide

### Dataset Reference
The **GLORIA (Global Resource Input-Output Assessment)** database is a Multi-Regional Input-Output (MRIO) database developed using the IELab infrastructure by the University of Sydney for the UN International Resource Panel (UN IRP) to update material footprint accounts within the UN IRP Material Flows Database.

### Request Link
**GLORIA Data**: [https://ielab.info/labs/ielab-gloria](https://ielab.info/labs/ielab-gloria)  
_(A user account is required to access the data.)_

### Technical Documentation
In addition to the raw data, the link contains the GLORIA technical documentation, which covers:
- Construction methodology of the MRIO table  
- Source datasets used  
- Quality checks performed  
- Method- and data-specific details

> **Note**: GLORIA data **cannot be used for commercial purposes** without a valid license from FootprintLab.

---

## Required Data Files
For calculations from **2012–2019**, you will need:

1. **Transactions Matries (T-Results)**  
   `20240111_120secMother_AllCountries_002_T-Results_xxxx_059_Markup001(full).csv` (~6.2 GB/year)

2. **Final Demand Matries (Y-Results)**  
   `20240111_120secMother_AllCountries_002_Y-Results_xxxx_059_Markup001(full).csv` (~226 MB/year)

---

## Usage Instructions

1. **Download** the required datasets from the link above.  
2. **Install** Python libraries, including `numpy`, `scipy`, `os`, `gc`, etc.  
3. **Run** the script, which loads the transactions (`T-Results`) and final demand (`Y-Results`) matrices into your workflow and runs the calculations.

**Performance Tip**:  
- The first time you run the script, these large CSV files (>10 GB) are converted into `.npy` format for faster subsequent data loading.  
- Future script runs will be much quicker.

---

## Running the Scripts

### 1. CBA & TBA for the EU27
Run:

```bash
python CBA_TBA_scriptEU27.py
```

This performs **Consumption-Based Accounting (CBA)** and **Trade-Based Accounting (TBA)** for the EU27 only. It iterates over **11 producer countries**, and **each year** (2012–2019) can take about **2 to 3 hours** per year to process.

### 2. Global CBA & TBA
This concerns the deforestation consumed and going "through" each country around the world (mainting the EU27 as a block to avoid to count several time intra-EU27 trade, see main manuscript). 

Run:
```bash
CBA_TBA_scriptglobal.py
```

- This script is set to run on **3 producer countries** (see SI for details) due to high computational demands.
- Even on a HPC (High-Performance Computing) system, it can take about **1 day** per country.

**All results** are automatically stored in the `output` folder.

---

## Consolidating Results in Alteryx
Once the MRIO scripts are finished:

1. Go to the Alteryx folder:
full_database

2. Run the relevant Alteryx workflow(s) to consolidate all generated results into a single database.
The CBA results are aggregated via the script: 
```bash
1_HILDA_v2-1_CBA results.yxmd
```
This creates the file CBA_Results_Full.csv in the folder 2. MRIO\Visualisation\1. CBA_TBA

The TBA results for the EU only are aggregated via the script: 
```bash
2_HILDA_v2-1_TBA_results_EU27only.yxmd
```
This creates the file Deforestation_Transiting_EU27_2012-2019.xlsx in the folder 2. MRIO\Visualisation\1. CBA_TBA

The TBA results for all the different countires around the world for Brazilian deforestation are aggregated via the script: 
```bash
HILDA_Aggregation_CBA-and-TBA_detailed_per_commodity_BRA.yxmd
```

This creates the file HILDA_V_2_1_Sankey_Prepared_05102024_BRA.xlsx in the folder 2.MRIO\Visualisation\2. Sankeys\1_TBA files prepared
Remark: The script must be slightly adapted to obtain the results for IDN and COD. 

---

## Visualization
Finally, visualize the consolidated database in the `visualisation` folder via a **straightforward** process (details may vary depending on your visualization tool).
For the Sankey visualisation, the process is slightly more complex. 
The coordinates used for each country are stored in the folder: 2. \2_MRIO\Visualisation\2. Sankeys\2_Sankey_coordinates
Then the Full figure is prepared via the file : 
Sankey_Figure_1_02052024.yxmd
And plot via the Jupyter script: Figure_1_Sankey_Diagram_2.ipynb 


---

## Contact & Support
- **GLORIA Technical Details**: Refer to the documentation or contact the University of Sydney IELab team for further support.  
- **MRIO/Script Queries**: Email [etber@mit.edu](mailto:etber@mit.edu).
