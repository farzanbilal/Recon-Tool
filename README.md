# Recon-Tool

A basic external pentesting and reconnaissance automation tool built with Python.

This project was created to automate common recon workflows used during external penetration testing and bug bounty hunting.

---

# Features

* Subdomain Enumeration
* Async Port Scanning
* HTTP Probing
* JavaScript File Discovery
* Security Header Analysis
* Screenshot Automation
* JSON Report Generation

---

# Tech Stack

* Python
* Asyncio
* HTTPX
* Playwright
* BeautifulSoup4

---

# Installation

Clone the repository:

```bash
git clone https://github.com/farzanbilal/Recon-Tool.git
cd Recon-Tool
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

# Usage

Run the tool:

```bash
python main.py
```

Enter target domain:

```txt
example.com
```

---

# Example Output

```json
{
  "subdomains": {
    "api.example.com": {
      "open_ports": [80, 443],
      "http": {
        "status": 200,
        "title": "API Gateway"
      }
    }
  }
}
```

---

# Project Structure

```txt
reconx/
│
├── main.py
├── requirements.txt
│
├── core/
│   ├── subdomains.py
│   ├── portscan.py
│   ├── httpprobe.py
│   ├── headers.py
│   ├── jsfinder.py
│   ├── screenshots.py
│   └── report.py
│
└── output/
```


---

# Disclaimer

This tool is intended for educational purposes and authorized security testing only.

Do not use this tool against systems without proper authorization.

---

