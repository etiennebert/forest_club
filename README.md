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

Use this README to navigate the folder structure, replicate the analyses, and locate important scripts and data files.

---

## Repository Structure

Suggested folder layout (modify as needed):



### Key Directories

- **`1. Data`**  
  Raw and processed input data:  
  - **HILDA+**: netCDFs, CSV extractions, and shapefiles.  
  - **FAO**: area/production/livestock files.

- **`2. MRIO/GLORIA`**  
  - **commodity**: FAO-to-GLORIA sector mapping.  
  - **output**: final and intermediate CBA/TBA results.

- **`3. GTAP-AEZ`**  
  CGE model files, parameter sets, AEZ shapefiles, and results for the Forest Club simulations.

- **`4. Scripts`**  
  Python or Alteryx workflows to extract HILDA+, map deforestation to commodities, and run TBA or CBA.

- **`5. Tariff_SIM`**  
  GTAP experiment setup for deriving tariffs proportional to deforestation footprints.

- **`output`**  
  Aggregated results, figures, and summary tables.

---

## Getting Started

### 1. Clone or Download

