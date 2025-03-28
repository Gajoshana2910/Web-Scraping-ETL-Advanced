import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# 🔹 HINT: Use different User-Agent values to prevent getting blocked
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
]

def extract():
    """
    Extracts quotes from multiple pages of 'Quotes to Scrape' website.
    
    - Uses rotating User-Agent headers.
    - Implements retries in case of connection errors.
    - Introduces random delays to avoid blocking.
    
    Returns:
        pandas.DataFrame: DataFrame containing extracted quotes and authors.
    """
    
    base_url = "https://quotes.toscrape.com/page/{}/"
    quotes_data = []  # List to store extracted quotes
    
    page = 1
    while True:
        headers = {"User-Agent": random.choice(USER_AGENTS)}  # 🔹 HINT: Pick a random User-Agent
        print(f"[INFO] Scraping page {page}...")

        try:
            # 🔹 HINT: Setting a timeout of 20 seconds to handle slow responses
            response = requests.get(base_url.format(page), headers=headers, timeout=20)  
            response.raise_for_status()  # 🔹 HINT: If the request fails (e.g., 404, 500), this will raise an error

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Request failed: {e}")
            print("[INFO] Retrying in 10 seconds...")
            time.sleep(10)  # 🔹 HINT: Adding delay before retrying
            continue  # Retry the same page

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")  # 🔹 HINT: Extract all quotes from the page

        if not quotes:  # 🔹 HINT: Stop if no more quotes are found (last page reached)
            print("[INFO] No more pages to scrape. Exiting...")
            break

        for quote in quotes:
            text = quote.find("span", class_="text").text.strip().replace("“", "").replace("”", "")  # 🔹 HINT: Remove extra characters
            author = quote.find("small", class_="author").text.strip()  # 🔹 HINT: Extract author name
            quotes_data.append({"quote": text, "author": author})

        page += 1  # 🔹 HINT: Move to the next page
        time.sleep(random.uniform(1, 3))  # 🔹 HINT: Random delay (1-3 sec) to prevent detection

    print(f"[INFO] Scraped {len(quotes_data)} quotes successfully!")
    return pd.DataFrame(quotes_data)  # 🔹 HINT: Return extracted data as a Pandas DataFrame
