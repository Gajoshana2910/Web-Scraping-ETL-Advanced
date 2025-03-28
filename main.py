from scripts.extract import extract  # 🔹 HINT: Extract data from the website
from scripts.transform import transform  # 🔹 HINT: Clean and standardize data
from scripts.load import load  # 🔹 HINT: Store data into PostgreSQL

print("[INFO] Starting ETL process...\n")

# 🔹 Step 1: Extract Data
print("[INFO] Extracting data from the website...")
data = extract()
if data.empty:  # 🔹 HINT: Check if extraction returned no data
    print("[ERROR] Extraction failed. No data found!")
    exit(1)
print(f"[INFO] Extraction successful! {len(data)} records found.\n")

# 🔹 Step 2: Transform Data
print("[INFO] Transforming data (cleaning & formatting)...")
cleaned_data = transform(data)
if cleaned_data.empty:
    print("[ERROR] Transformation resulted in no data! Check transform logic.")
    exit(1)
print(f"[INFO] Transformation successful! {len(cleaned_data)} records cleaned.\n")

# 🔹 Step 3: Load Data
print("[INFO] Loading data into PostgreSQL database...")
try:
    load(cleaned_data)
    print("[INFO] Data successfully stored in PostgreSQL!")
except Exception as e:
    print(f"[ERROR] Failed to load data: {e}")
    exit(1)

print("[INFO] ETL process completed successfully!")
