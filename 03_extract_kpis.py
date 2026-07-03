import os
import pandas as pd

# ---------------------------------------
# Paths
# ---------------------------------------

ENV_FOLDER = r"../BRSR_TABLES/Environmental"
OUTPUT_FOLDER = r"../OUTPUT"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Keywords that identify Environmental KPI tables
kpi_keywords = [
    "energy",
    "ghg",
    "scope",
    "emission",
    "water",
    "waste",
    "plastic",
    "recycle",
    "renewable",
    "biodiversity",
    "forest",
    "carbon"
]

records = []

print("=" * 60)
print("Extracting Environmental KPIs...")
print("=" * 60)

for file in os.listdir(ENV_FOLDER):

    if not file.endswith(".csv"):
        continue

    filepath = os.path.join(ENV_FOLDER, file)

    try:

        df = pd.read_csv(filepath, dtype=str).fillna("")

        page = file.split("_")[1]

        for r in range(df.shape[0]):

            row_text = " | ".join(df.iloc[r].astype(str))

            lower = row_text.lower()

            if any(word in lower for word in kpi_keywords):

                records.append({
                    "Page": page,
                    "Source_File": file,
                    "Raw_KPI_Row": row_text
                })

    except Exception as e:
        print(f"Skipped {file}: {e}")

# ---------------------------------------
# Save
# ---------------------------------------

result = pd.DataFrame(records)

output_file = os.path.join(
    OUTPUT_FOLDER,
    "Environmental_KPIs_Raw.xlsx"
)

result.to_excel(output_file, index=False)

print("\nExtraction Complete!")
print(f"Rows Extracted : {len(result)}")
print(f"Saved to : {output_file}")

import os
import re
import pandas as pd
from openpyxl import load_workbook

# ==========================================
# PATHS
# ==========================================

SOURCE_FOLDER = r"../OUTPUT"
DATASET_FILE = r"../DATASET/ITC_ESG_Dataset_2026.xlsx"

# ==========================================
# Find Excel files exported from BRSR pages
# ==========================================

files = []

for file in os.listdir(SOURCE_FOLDER):

    if file.startswith("page_") and file.endswith(".xlsx"):
        files.append(file)

print(f"Found {len(files)} page tables")

records = []

# ==========================================
# Read every table
# ==========================================

for file in files:

    filepath = os.path.join(SOURCE_FOLDER, file)

    try:

        df = pd.read_excel(filepath, dtype=str).fillna("")

        page = re.findall(r"page_(\d+)", file)[0]

        for _, row in df.iterrows():

            values = [str(x).strip() for x in row.tolist()]

            text = " | ".join(values)

            # Ignore empty rows
            if len(text.replace("|", "").strip()) < 5:
                continue

            records.append({

                "KPI Category": "Environmental",

                "KPI": values[0],

                "FY2025-26": values[1] if len(values) > 1 else "",

                "FY2024-25": values[2] if len(values) > 2 else "",

                "Unit": "",

                "Source Page": page,

                "Source Table": file

            })

    except Exception as e:

        print(file, e)

print(f"Rows Parsed : {len(records)}")

# ==========================================
# Append into Excel
# ==========================================

wb = load_workbook(DATASET_FILE)

ws = wb["Environmental_KPIs"]

for r in records:

    ws.append(list(r.values()))

wb.save(DATASET_FILE)

print("\nDone!")
print("Environmental KPIs added successfully.")
