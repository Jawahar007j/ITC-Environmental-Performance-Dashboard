# ITC-Environmental-Performance-Dashboard
Python-based ETL pipeline and interactive Excel dashboard for analyzing ITC's environmental ESG performance using annual report data.
ITC Environmental Performance Dashboard
Python-based ETL pipeline and interactive Excel dashboard for analyzing ITC’s environmental ESG performance using annual report data.
 
Dashboard Preview
Overview
This project extracts, cleans, and structures environmental KPI data from ITC Limited’s Report and Accounts 2026 (BRSR/Sustainability disclosures), transforming unstructured PDF tables into a clean, analysis-ready dataset — then visualizes it through an interactive Excel dashboard comparing FY2024-25 vs FY2025-26 performance.
The pipeline covers the full journey from raw PDF extraction to a decision-ready dashboard: table extraction → ESG relevance filtering → categorical classification → KPI extraction → master dataset assembly → cleaning/deduplication → dashboard-ready long-format data.
Dashboard Highlights
•	Air Emissions: SOx, NOx, Particulate Matter, Hazardous Air Pollutants
•	Energy Management: Total, renewable, and non-renewable energy consumption
•	GHG Emissions: Scope 1, 2, and 3 emissions with intensity ratios (per revenue, PPP, PSPD, FBD)
•	Water Management: Consumption, withdrawal, and intensity
•	Waste Management: Battery, e-waste, bio-medical, construction & demolition, and other hazardous waste
•	ESG Ratings: CDP Climate/Water/Forest, MSCI ESG Rating, Dow Jones Sustainability Index inclusion
Key year-over-year findings: - SOx emissions down 25.7%; NOx emissions down 2.8% - Total energy consumption down 6.85%, with a near-even renewable/non-renewable split maintained - Scope 1 emissions down 5.09%, but Scope 3 emissions rose sharply (1,062 → 1,442 ktCO₂e) - Total water consumption up 4.76%, while withdrawal and intensity both improved
Repository Structure
ITC-Environmental-Performance-Dashboard/
│
├── DASHBOARDS/
│   ├── ITC DASHBOARD.pdf                   # Dashboard exported as PDF
│   └── ITC DASHBOARD.png                   # Dashboard screenshot
│
├── DATA/
│   ├── Dashboard_Data.xlsx                 # Long-format dataset powering the dashboard (70 rows)
│   └── ITC_Environmental_Master_Clean.xlsx # Cleaned master dataset (wide format, 37 KPIs)
│
├── scripts/
│   ├── 01_extract_tables.py                # Extracts all tables from the PDF into CSVs
│   ├── 02_filter_environmental_tables.py   # Filters/classifies tables by ESG keyword relevance
│   ├── 03_extract_kpis.py                  # Extracts KPI-relevant rows from environmental tables
│   ├── 04_build_master_dataset.py          # Assembles verified KPIs into the master dataset
│   ├── 05_clean_environment_dataset.py     # Removes duplicates/placeholders, sorts and standardizes
│   └── 06_create_dashboard_data.py         # Reshapes master data into long format for the dashboard
│
└── README.md
Note: the scripts reference intermediate working folders (raw_tables, cleaned_tables, output, final_data, etc.) used during local development to stage data between pipeline steps. These are not part of this repository — only the final scripts, datasets, and dashboard exports are included here.
Data Source
Data is manually extracted and verified from ITC Limited’s publicly available Report and Accounts 2026, specifically the Business Responsibility and Sustainability Report (BRSR) and Sustainability Report sections (pages 367-395), covering environmental disclosures for FY2024-25 and FY2025-26.
The source PDF is not included in this repository due to file size/licensing. It can be downloaded from ITC Limited’s official investor relations page.
Pipeline (ETL) Workflow
Step	Script	Purpose
1	01_extract_tables.py	Uses pdfplumber to extract every table from the annual report PDF, saving each as an individual CSV
2	02_filter_environmental_tables.py	Keyword-matches extracted tables against ESG terms (carbon, GHG, energy, water, waste, etc.) and classifies them into Environmental / Social / Governance / Financial categories
3	03_extract_kpis.py	Scans environmental tables row-by-row for KPI-relevant content and compiles raw candidate KPI rows
4	04_build_master_dataset.py	Appends manually verified KPI values (cross-checked against source pages) into the master dataset, covering Energy, GHG, Waste, Packaging, and ESG Ratings
5	05_clean_environment_dataset.py	Removes placeholder/incomplete KPIs and duplicates, sorts by category for consistency
6	06_create_dashboard_data.py	Melts the wide-format master dataset (FY2024-25 / FY2025-26 columns) into long format (Year, Value) for pivot-table and chart consumption
Datasets
DATA/ITC_Environmental_Master_Clean.xlsx — Wide-format master dataset, 37 KPIs across 7 categories (Air Emissions, Energy, ESG Ratings, GHG, Packaging, Waste, Water), each with FY2024-25 and FY2025-26 values, units, and source page references.
DATA/Dashboard_Data.xlsx — Long-format version (70 rows) of the same data, restructured with one row per KPI per year, used to drive the dashboard’s pivot tables and charts.
Both datasets share a consistent schema:
Column	Description
KPI Category	Top-level ESG category (e.g., Energy, GHG, Waste)
Sub Category	Category subdivision (e.g., Scope 1, Renewable)
KPI	Specific metric name
Unit	Unit of measurement (TJ, Tonnes, kL, tCO₂e, etc.)
Source Page	Page number in the source report
Year (long format only)	FY2024-25 or FY2025-26
Value	Metric value
Dashboard
The final deliverable is an interactive Excel dashboard (exported here as DASHBOARDS/ITC DASHBOARD.pdf and DASHBOARDS/ITC DASHBOARD.png), featuring: - KPI scorecards with YoY % change indicators - A year slicer to toggle between FY2024-25 and FY2025-26 - Bar, donut, and comparison charts across all six environmental categories - A key-insights panel summarizing YoY trends
Tech Stack
•	Python: pdfplumber, pandas, openpyxl
•	Excel: Pivot tables, slicers, charts (native Excel dashboard, no external BI tool)
How to Reproduce
pip install pdfplumber pandas openpyxl
Run the scripts in order from inside scripts/ (each expects the source PDF and prior-step outputs in the paths configured at the top of the script — update these paths for your local setup before running):
cd scripts
python 01_extract_tables.py
python 02_filter_environmental_tables.py
python 03_extract_kpis.py
python 04_build_master_dataset.py
python 05_clean_environment_dataset.py
python 06_create_dashboard_data.py
Final datasets land in DATA/; open the dashboard exports in DASHBOARDS/ to view the finished result.
About the Author
Built by Jawahar as part of an ESG/Sustainability analytics portfolio, applying a forestry and environmental science background (MSc Forestry, TNAU) to corporate sustainability data analysis.
License
This project is for educational and portfolio purposes. Underlying data belongs to ITC Limited and is sourced from their publicly filed Report and Accounts 2026.
