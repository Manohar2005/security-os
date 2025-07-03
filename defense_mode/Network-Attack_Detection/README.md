# 🛡️ Network Attack Detection Tool

This tool is built to detect common network-based attacks like SYN Flood, SQL Injection, XSS, and Directory Traversal in real-time using live packet sniffing. It was developed as part of the **Defense Mode** in my Security-OS project to simulate realistic threat detection in lab environments.

---

## 📌 What It Does

- Captures live traffic on the system using Python and Scapy  
- Checks for patterns that match known attack behaviors (e.g., SYN flood attempts, suspicious GET/POST requests, known payloads)  
- Displays alerts in real-time through a Flask web dashboard  
- Helps understand how basic intrusion detection works by showing how packets can be analyzed and flagged  

---

## 📁 Folder Structure

network-attack-detector/
├── detector/ # Core detection logic
│ ├── sniffer.py # Packet sniffing and routing
│ ├── analyzer.py # Attack pattern detection
│ └── logger.py # Simple log handler
├── dashboard/ # Flask web interface
│ ├── app.py # Web server
│ └── templates/
│ └── index.html # Frontend UI
├── attacks/ # Sample payloads and attack signatures
├── logs/ # Stores detection logs
├── runall.sh # One-click launcher script
├── requirements.txt # Python dependencies
└── README.md # You're reading it :)


---

## ⚙️ How It Works

1. **Packet Sniffing**  
   The tool uses `scapy` to sniff all incoming and outgoing packets on the interface.

2. **Detection Logic**  
   It checks for:
   - **SYN Floods** by counting abnormal TCP SYN patterns
   - **SQL Injection / XSS** by scanning payloads in HTTP requests
   - **Directory Traversal** using encoded patterns like `../`

3. **Alerting**  
   If something suspicious is found:
   - It prints a message to the terminal
   - Logs the event with a timestamp
   - Displays the alert in a Flask-based web dashboard

4. **Visualization**  
   Open the dashboard in your browser to view alerts in real time.

---

## 🚀 How to Run

### 🐍 Step 1: Install Dependencies

Make sure Python 3.8+ is installed.

```bash
pip install -r requirements.txt

Or install manually:

pip install flask scapy

🏃 Step 2: Start the Detector

python detector/sniffer.py

This will begin capturing packets and analyzing them.
🌐 Step 3: Launch the Dashboard

In a new terminal:

python dashboard/app.py

Then open this in your browser:

http://localhost:5000

You’ll see detected alerts live on the web UI.
📓 Notes

    The tool is made for learning and testing purposes only

    It works best on Linux systems with root privileges

    You can simulate attacks using tools like hping3, curl, or test payloads from the attacks/ folder

    Detection logs are saved inside the logs/ folder with timestamps

🔥 Example Attack Simulations
SYN Flood Attack

sudo hping3 -S -p 80 --flood 127.0.0.1

XSS Test

curl "http://localhost/?q=<script>alert('XSS')</script>"

The detector should flag the packet and log the alert, which will show up on the dashboard.
👨‍💻 Author

Hi, I'm Manohar Kosana. I built this tool as part of the Defense Mode in my Security-OS project to learn more about how network attacks work and how they can be detected.
You can check out more of my profile(Manohar2005)
🔐 Disclaimer

This project is intended for educational and ethical testing purposes only.
Do not use it on networks you don’t own or have permission to test.
