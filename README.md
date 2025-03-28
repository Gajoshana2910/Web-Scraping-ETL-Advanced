# 🚀 Web Scraping ETL Advanced

Extract → Transform → Load (ETL) Pipeline for Scraping Quotes and Storing in PostgreSQL

---

## 📌 Project Overview


This project scrapes quotes from Quotes to Scrape, cleans the data, and loads it into a PostgreSQL database. The pipeline is automated with Python, Requests, BeautifulSoup, Pandas, and SQLAlchemy.


## 🏗️ Project Structure

```
📂 Web-Scraping-ETL-Advanced
│── 📂 scripts
│   │── extract.py     # Web Scraping Logic
│   │── transform.py   # Data Cleaning & Formatting
│   │── load.py        # PostgreSQL Data Insertion
│── main.py            # ETL Process Runner
│── requirements.txt    # Python Dependencies
│── README.md          # Project Documentation
```

## ⚙ Installation & Setup

1️⃣ Clone the Repository
```
git clone https://github.com/your-username/Web-Scraping-ETL-Advanced.git
cd Web-Scraping-ETL-Advanced
```

2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

3️⃣ Setup PostgreSQL Database
```
CREATE DATABASE quotes_db;
```

4️⃣ Configure PostgreSQL Connection
Update db_url in scripts/load.py:

```
db_url = "postgresql+psycopg2://postgres:your_password@localhost:5432/quotes_db"
```

## 🚀 Run the ETL Pipeline
```
python main.py
```

## 🔍 Checking Data in PostgreSQL
```
SELECT * FROM quotes LIMIT 10;
```

## 🛠 Troubleshooting
1️⃣ Connection Timeout Issues?

- Try adding a User-Agent in extract.py:

```
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(base_url.format(page), headers=headers, timeout=10)
```

2️⃣ PostgreSQL Errors?

- Ensure PostgreSQL is running and credentials are correct.
- Install psycopg2 if missing:
```
pip install psycopg2-binary
```

## 📜 License

This project is licensed under the MIT License 
👉 see the [LICENSE](https://github.com/Gajoshana2910/Web-Scraping-ETL-Advanced/blob/main/LICENSE) file for details.  

## 👨‍💻 Developed by

👉 [Gajalakshmi A K](https://github.com/Gajoshana2910)






