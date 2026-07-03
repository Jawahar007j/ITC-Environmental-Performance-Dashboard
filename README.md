# ITC Environmental Performance Dashboard

*A Python ETL Pipeline and Interactive Excel Dashboard for ESG Analysis*

**Repository:** ITC-Environmental-Performance-Dashboard | **Author:** Jawahar

---

Python-based ETL pipeline and interactive Excel dashboard for analyzing ITC Limited's environmental ESG performance using annual report data. This project extracts, cleans, and structures environmental KPI data from ITC's Report and Accounts 2026 (BRSR / Sustainability disclosures), transforming unstructured PDF tables into a clean, analysis-ready dataset, then visualizes it through a single-page interactive Excel dashboard comparing FY2024-25 against FY2025-26 performance.

![Dashboard Preview](DASHBOARDS/ITC%20DASHBOARD.png)
*Figure 1: Final ESG environmental performance dashboard (FY2024-25 vs FY2025-26)*

## 1. Project Objectives

- Convert unstructured PDF disclosures from a 300+ page corporate annual report into a structured, analysis-ready dataset.
- Isolate and validate environmental KPIs (Air Emissions, Energy, GHG, Waste, Water, Packaging, ESG Ratings) relevant to BRSR reporting.
- Build a reproducible Python ETL pipeline covering extraction, classification, verification, and transformation.
- Deliver a decision-ready, interactive Excel dashboard comparing year-over-year environmental performance.
- Demonstrate applied ESG analytics capability as part of a professional sustainability analytics portfolio.

## 2. Dashboard Highlights

- **Air Emissions**: SOx, NOx, Particulate Matter, and Hazardous Air Pollutants.
- **Energy Management**: Total, renewable, and non-renewable energy consumption.
- **GHG Emissions**: Scope 1, 2, and 3 emissions with intensity ratios (per revenue, PPP, PSPD, FBD).
- **Water Management**: Consumption, withdrawal, and intensity.
- **Waste Management**: Battery, e-waste, bio-medical, construction & demolition, and other hazardous waste.
- **ESG Ratings**: CDP Climate/Water/Forest, MSCI ESG Rating, and Dow Jones Sustainability Index inclusion.

## 3. Repository Structure

| Folder / File | Contents | Purpose |
|---|---|---|
| `DASHBOARDS/` | `ITC DASHBOARD.pdf`, `ITC DASHBOARD.png` | Final dashboard exports for quick viewing |
| `DATA/` | `Dashboard_Data.xlsx`, `ITC_Environmental_Master_Clean.xlsx` | Cleaned, analysis-ready datasets |
| `scripts/` | `01_extract_tables.py` → `06_create_dashboard_data.py` | Six-step ETL pipeline (PDF to dashboard-ready data) |
| `README.md` | — | Project documentation |

## 4. Data Source

Data is manually extracted and verified from ITC Limited's publicly available Report and Accounts 2026, specifically the Business Responsibility and Sustainability Report (BRSR) and Sustainability Report sections (pages 367–395), covering environmental disclosures for FY2024-25 and FY2025-26. The source PDF is not included in this repository due to file size and licensing considerations; it can be downloaded from ITC Limited's official investor relations page.

## 5. ETL Pipeline Workflow

| Step | Script | Purpose |
|---|---|---|
| 1 | `01_extract_tables.py` | Extracts every table from the annual report PDF using `pdfplumber`, saving each as an individual CSV. |
| 2 | `02_filter_environmental_tables.py` | Keyword-matches tables against ESG terms and classifies them into Environmental, Social, Governance, or Financial categories. |
| 3 | `03_extract_kpis.py` | Scans environmental tables row-by-row to compile candidate KPI rows. |
| 4 | `04_build_master_dataset.py` | Appends manually verified KPI values into the master dataset, cross-checked against source pages. |
| 5 | `05_clean_environment_dataset.py` | Removes placeholder and duplicate KPIs; sorts by category for consistency. |
| 6 | `06_create_dashboard_data.py` | Melts the wide-format dataset into long format for pivot tables and charts. |

## 6. Datasets

- **`DATA/ITC_Environmental_Master_Clean.xlsx`**: Wide-format master dataset with 37 KPIs across 7 categories (Air Emissions, Energy, ESG Ratings, GHG, Packaging, Waste, Water), each with FY2024-25 and FY2025-26 values, units, and source page references.
- **`DATA/Dashboard_Data.xlsx`**: Long-format version (70 rows) of the same data, restructured with one row per KPI per year, used to drive the dashboard's pivot tables and charts.

Both datasets share a consistent schema:

| Column | Description |
|---|---|
| KPI Category | Top-level ESG category (e.g., Energy, GHG, Waste) |
| Sub Category | Category subdivision (e.g., Scope 1, Renewable) |
| KPI | Specific metric name |
| Unit | Unit of measurement (TJ, Tonnes, kL, tCO₂e, etc.) |
| Source Page | Page number in the source report |
| Year *(long format only)* | FY2024-25 or FY2025-26 |
| Value | Metric value |

## 7. Key Year-over-Year Findings

- SOx emissions decreased 25.7%; NOx emissions decreased 2.8%.
- Total energy consumption decreased 6.85%, with a near-even renewable/non-renewable split maintained.
- Scope 1 emissions decreased 5.09%, but Scope 3 emissions rose sharply from 1,062 to 1,442 ktCO₂e.
- Total water consumption increased 4.76%, while withdrawal and intensity both improved.
- ESG ratings held steady: MSCI AA, CDP Climate A-, and inclusion on both CDP Water and CDP Forest A Lists.

## 8. Tech Stack

- **Python**: `pdfplumber`, `pandas`, `openpyxl`
- **Excel**: Pivot tables, slicers, and charts — a native Excel dashboard with no external BI tool required.

## 9. How to Reproduce

```bash
pip install pdfplumber pandas openpyxl
```

From inside `scripts/`, run the six pipeline scripts in numerical order (01 through 06). Each script expects the source PDF and prior-step outputs in the paths configured at the top of the file, so update these paths for your local setup before running. Final datasets are written to `DATA/`, and the finished dashboard exports can be viewed in `DASHBOARDS/`.


## 10. About the Author

Built by **Jawahar**, an MBA and MSc graduate focused on ESG Analyst and Data/Business Analyst roles. This dashboard was built voluntarily using ITC Limited's publicly available report data, as part of a hands-on portfolio project demonstrating applied ESG analytics capability.

## 11. License

This project is for educational and portfolio purposes. Underlying data belongs to ITC Limited and is sourced from their publicly filed Report and Accounts 2026.
