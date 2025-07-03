import multiprocessing
import time
import syn_flood
import http_flood
import xss_attack
import sql_injection
import dir_traversal

def run_all():
    target_ip = "127.0.0.1"
    target_port = 80
    target_url = "http://127.0.0.1:5000"

    processes = [
        multiprocessing.Process(target=syn_flood.syn_flood, args=(target_ip, target_port)),
        multiprocessing.Process(target=http_flood.http_flood, args=(target_url,)),
        multiprocessing.Process(target=xss_attack.xss_attack, args=(target_url,)),
        multiprocessing.Process(target=sql_injection.sql_injection, args=(target_url,)),
        multiprocessing.Process(target=dir_traversal.dir_traversal, args=(target_url,))
    ]

    for p in processes:
        p.start()

    time.sleep(120)  # run all attacks for 10 seconds

    for p in processes:
        p.terminate()
        p.join()

    print("[+] All attacks finished.")

if __name__ == "__main__":
    run_all()
