import pandas as pd

def transform(df):
    """
    Clean and standardize scraped data.

    🔹 HINT:
    - Remove unwanted special characters from quotes.
    - Ensure author names are properly capitalized.
    - Handle missing/null values gracefully.
    """

    if df is None or df.empty:
        print("[ERROR] No data to transform. Skipping transformation.")
        return None

    try:
        print("[INFO] Cleaning and standardizing data...")

        # 🔹 Remove unwanted special characters from quotes
        df["quote"] = df["quote"].str.replace("“", "").str.replace("”", "")

        # 🔹 Capitalize author names properly
        df["author"] = df["author"].str.title()

        # 🔹 Handle missing values (if any)
        df = df.dropna(subset=["quote", "author"])  # Remove rows with missing values

        # 🔹 Remove duplicates (if any)
        df = df.drop_duplicates()

        print("[INFO]  Transformation successful!")

        return df

    except Exception as e:
        print(f"[ERROR] Data transformation failed: {e}")
        return None
