import pandas as pd
import os

# ==========================================
# FILE PATH
# ==========================================

INPUT_FILE = r"../FINAL_DATA/ITC_Environmental_Master.xlsx"
OUTPUT_FILE = r"../FINAL_DATA/ITC_Environmental_Master_Clean.xlsx"

# ==========================================
# READ DATA
# ==========================================

df = pd.read_excel(INPUT_FILE)

print("=" * 60)
print("Original Rows :", len(df))
print("=" * 60)

# ==========================================
# REMOVE PLACEHOLDER KPIs
# ==========================================

remove_kpis = [

    "Purchased Goods & Services",
    "Capital Goods",
    "Fuel & Energy Related Activities",
    "Upstream Transportation",
    "Waste Generated in Operations",
    "Business Travel",
    "Employee Commuting",
    "Downstream Transportation"

]

df = df[~df["KPI"].isin(remove_kpis)]

# ==========================================
# REMOVE DUPLICATES
# ==========================================

df = df.drop_duplicates(subset=["KPI"])

# ==========================================
# SORT
# ==========================================

category_order = {
    "Air Emissions": 1,
    "Energy": 2,
    "ESG Ratings": 3,
    "GHG": 4,
    "Packaging": 5,
    "Waste": 6,
    "Water": 7
}

df["Sort"] = df["KPI Category"].map(category_order)

df = df.sort_values(["Sort", "Sub Category", "KPI"])

df = df.drop(columns="Sort")

# ==========================================
# SAVE
# ==========================================

df.to_excel(OUTPUT_FILE, index=False)

print("=" * 60)
print("Environmental Dataset Cleaned Successfully")
print("Final Rows :", len(df))
print("Saved As :", OUTPUT_FILE)
print("=" * 60)