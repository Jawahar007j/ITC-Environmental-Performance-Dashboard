import pdfplumber
import pandas as pd
import os

# -------------------------------
# File Paths
# -------------------------------
PDF_PATH = r"../input/ITC-Report-and-Accounts-2026.pdf"
OUTPUT_FOLDER = r"../raw_tables"

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Counter for extracted tables
table_count = 0

print("=" * 60)
print("ITC ESG TABLE EXTRACTION STARTED")
print("=" * 60)

# Open PDF
with pdfplumber.open(PDF_PATH) as pdf:

    print(f"\nTotal Pages : {len(pdf.pages)}\n")

    # Loop through every page
    for page_number, page in enumerate(pdf.pages, start=1):

        try:
            tables = page.extract_tables()

            if tables:

                print(f"Page {page_number} --> {len(tables)} table(s) found")

                for i, table in enumerate(tables):

                    if len(table) > 1:

                        df = pd.DataFrame(table[1:], columns=table[0])

                        filename = f"page_{page_number}_table_{i+1}.csv"

                        filepath = os.path.join(OUTPUT_FOLDER, filename)

                        df.to_csv(filepath, index=False)

                        table_count += 1

        except Exception as e:

            print(f"Error on Page {page_number}: {e}")

print("\n" + "=" * 60)
print(f"Extraction Completed")
print(f"Total Tables Extracted : {table_count}")
print("=" * 60)
