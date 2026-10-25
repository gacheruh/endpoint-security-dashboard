# Endpoint Security & Phishing Awareness Dashboard

A lightweight monitoring dashboard designed to aggregate simulated endpoint protection statuses, track antivirus health checks, and log reported phishing incidents or unauthorized access attempts with recommended remediation steps.

## Virtual Environment (.venv) Setup Instructions

Always run Python projects within an isolated virtual environment.

### On Unix / macOS (Terminal):
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### On Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Running the Application
After activating your virtual environment and installing dependencies:
```bash
streamlit run app.py
```
