import requests

try:
    response = requests.get("https://www.google.com", timeout=10)
    print("[INFO] Connected successfully!")
except requests.exceptions.RequestException as e:
    print(f"[ERROR] Failed to connect: {e}")
