import pandas as pd
import os

# ==========================================
# PATHS
# ==========================================

INPUT = r"../FINAL_DATA/ITC_Environmental_Master_Clean.xlsx"
OUTPUT = r"../FINAL_DATA/Dashboard_Data.xlsx"

# ==========================================
# READ DATA
# ==========================================

df = pd.read_excel(INPUT)

# ==========================================
# CONVERT TO LONG FORMAT
# ==========================================

dashboard_df = pd.melt(
    df,
    id_vars=[
        "KPI Category",
        "Sub Category",
        "KPI",
        "Unit",
        "Source Page"
    ],
    value_vars=["FY2025-26", "FY2024-25"],
    var_name="Year",
    value_name="Value"
)

# Remove empty values
dashboard_df = dashboard_df.dropna(subset=["Value"])

# ==========================================
# SAVE
# ==========================================

dashboard_df.to_excel(OUTPUT, index=False)

print("=" * 60)
print("Dashboard Dataset Created Successfully")
print("Rows :", len(dashboard_df))
print("Saved :", OUTPUT)
print("=" * 60)