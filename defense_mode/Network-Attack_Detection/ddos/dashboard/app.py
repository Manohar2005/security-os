from flask import Flask, render_template
import json
import os
import sys


sys.path.insert(0, '/home/manohar/projects/ddos')

from detector.attack_signature import match_attack

app = Flask(__name__)

@app.route("/")
def index():
    packets = []
    log_path = "/home/manohar/projects/ddos/logs/packets.json"

    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            for line in f:
                try:
                    pkt = json.loads(line.strip())
                    pkt["alerts"] = match_attack(pkt)
                    packets.append(pkt)
                except:
                    continue
    return render_template("index.html", packets=packets[::-1])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

