from sqlalchemy import create_engine
import pandas as pd

def load(df, db_url="postgresql+psycopg2://postgres:postgres@localhost:5432/quotes_db"):
    """Load data into PostgreSQL database."""
    
    if df is None or df.empty:
        print("[ERROR] ❌ No data to load.")
        return

    try:
        print("[INFO] 🗄️ Connecting to PostgreSQL database...")
        
        # Create SQLAlchemy engine
        engine = create_engine(db_url)

        # Load DataFrame into PostgreSQL
        df.to_sql("quotes", con=engine, if_exists="replace", index=False, method="multi")

        print("[INFO] ✅ Data successfully loaded into PostgreSQL!")

    except Exception as e:
        print(f"[ERROR] ❌ Failed to insert data into PostgreSQL: {e}")

    finally:
        engine.dispose()
        print("[INFO] 🔒 Database connection closed.")
