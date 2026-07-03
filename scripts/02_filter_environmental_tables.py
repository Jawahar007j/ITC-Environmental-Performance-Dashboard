import os
import shutil
import pandas as pd

# -----------------------------
# Folder Paths
# -----------------------------
RAW_FOLDER = r"../RAW_TABLES"
CLEAN_FOLDER = r"../CLEANED_TABLES"

os.makedirs(CLEAN_FOLDER, exist_ok=True)

# -----------------------------
# ESG Keywords
# -----------------------------
keywords = [
    "carbon", "ghg", "scope", "emission",
    "energy", "renewable", "electricity",
    "water", "waste", "plastic",
    "climate", "biodiversity", "forest",
    "farmer", "environment", "recycle",
    "sustainability", "esg", "csr",
    "employee", "board", "governance",
    "ethics", "safety"
]

total_tables = 0
matched_tables = 0

print("="*60)
print("Filtering ESG Tables")
print("="*60)

for file in os.listdir(RAW_FOLDER):

    if file.endswith(".csv"):

        total_tables += 1

        filepath = os.path.join(RAW_FOLDER, file)

        try:

            df = pd.read_csv(filepath, dtype=str)

            text = " ".join(df.astype(str).fillna("").values.flatten())

            text = text.lower()

            if any(word in text for word in keywords):

                shutil.copy(filepath,
                            os.path.join(CLEAN_FOLDER, file))

                matched_tables += 1

                print(f"Copied --> {file}")

        except Exception:

            continue

print("\n")
print("="*60)
print(f"Total Tables      : {total_tables}")
print(f"ESG Tables Found  : {matched_tables}")
print("="*60)

import os
import shutil
import pandas as pd

# ==============================
# Paths
# ==============================

MASTER_INDEX = r"../OUTPUT/Master_Index.xlsx"
SOURCE_FOLDER = r"../CLEANED_TABLES"

BASE_FOLDER = r"../CLEANED_TABLES"

CATEGORIES = {
    "Environmental": [
        "carbon","ghg","scope","emission","energy","renewable",
        "electricity","water","waste","plastic","climate",
        "biodiversity","forest","forestry","recycle","aws",
        "packaging","pollution","environment"
    ],

    "Social": [
        "employee","training","health","safety","csr",
        "community","education","livelihood","farmer",
        "gender","women","diversity","human rights"
    ],

    "Governance": [
        "board","director","audit","ethics","governance",
        "compliance","risk","committee","whistle"
    ],

    "Financial": [
        "revenue","profit","ebitda","cash flow","eps",
        "tax","assets","liabilities","finance",
        "income","balance sheet"
    ]
}

# ==============================
# Create Category Folders
# ==============================

for folder in list(CATEGORIES.keys()) + ["Others"]:
    os.makedirs(os.path.join(BASE_FOLDER, folder), exist_ok=True)

# ==============================
# Read Master Index
# ==============================

master = pd.read_excel(MASTER_INDEX)

classification_log = []

# ==============================
# Classification
# ==============================

for _, row in master.iterrows():

    file_name = row["CSV_File"]
    preview = str(row["Preview"]).lower()

    assigned = "Others"
    score = 0

    for category, words in CATEGORIES.items():

        current_score = sum(word in preview for word in words)

        if current_score > score:
            score = current_score
            assigned = category

    source_file = os.path.join(SOURCE_FOLDER, file_name)

    destination = os.path.join(BASE_FOLDER, assigned, file_name)

    if os.path.exists(source_file):
        shutil.copy(source_file, destination)

    classification_log.append({
        "CSV_File": file_name,
        "Category": assigned,
        "Keyword_Matches": score
    })

# ==============================
# Save Log
# ==============================

log = pd.DataFrame(classification_log)

log.to_excel(
    "../OUTPUT/classification_log.xlsx",
    index=False
)

print("="*60)
print("Classification Completed")
print("="*60)

print(log["Category"].value_counts())

print("\nclassification_log.xlsx created successfully.")

import os
import pandas as pd
import shutil

# ==========================
# Folder Paths
# ==========================

BRSR_FOLDER = r"../BRSR_TABLES"

OUTPUT_FOLDER = r"../OUTPUT"

ENV_FOLDER = r"../BRSR_TABLES/Environmental"

os.makedirs(ENV_FOLDER, exist_ok=True)

# ==========================
# Environmental Keywords
# ==========================

keywords = [

    "carbon",
    "ghg",
    "scope",
    "emission",
    "energy",
    "renewable",
    "electricity",
    "fuel",
    "water",
    "waste",
    "plastic",
    "biodiversity",
    "forest",
    "forestry",
    "climate",
    "recycle",
    "recycling",
    "packaging",
    "pollution",
    "rainwater",
    "aws",
    "iso 14001"

]

records = []

count = 0

print("=" * 60)
print("Identifying Environmental Tables")
print("=" * 60)

for file in os.listdir(BRSR_FOLDER):

    if file.endswith(".csv"):

        path = os.path.join(BRSR_FOLDER, file)

        try:

            df = pd.read_csv(path, dtype=str)

            text = " ".join(
                df.fillna("")
                  .astype(str)
                  .values
                  .flatten()
            ).lower()

            matches = sum(word in text for word in keywords)

            if matches >= 2:

                shutil.copy(
                    path,
                    os.path.join(ENV_FOLDER, file)
                )

                records.append({
                    "CSV_File": file,
                    "Keyword_Matches": matches
                })

                count += 1

        except:
            pass

summary = pd.DataFrame(records)

summary.to_excel(
    os.path.join(
        OUTPUT_FOLDER,
        "Environmental_Table_Index.xlsx"
    ),
    index=False
)

print("\nEnvironmental Tables :", count)
print("Environmental_Table_Index.xlsx created.")

