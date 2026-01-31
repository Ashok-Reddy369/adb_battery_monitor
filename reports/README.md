# ADB Battery Monitor

ADB Battery Monitor is a Python + pytest based automation framework to validate **Android battery health** using real devices.  
It collects battery metrics via `dumpsys battery`, captures **ADB logcat**, and generates **human-readable text reports** for debugging, audits, and CI usage.

---

## 📌 Features

- Real Android device testing via ADB
- Battery health, level, and temperature validation
- Robust parsing of `dumpsys battery`
- Automatic ADB logcat collection
- Text-based test reports
- Pytest-based execution with markers
- CI-friendly logging and reporting

---

## 📂 Project Structure

```text
adb_battery_monitor/
├── adb_logs/                  # ADB logcat output (auto-generated)
├── reports/                   # Battery health reports (text)
├── src/                       # Core implementation
│   ├── __init__.py
│   ├── battery_tester.py
│   ├── adb_log_collector.py
│   └── report_generator.py
├── tests/                     # Pytest test cases & fixtures
│   ├── conftest.py
│   └── test_battery.py
├── pytest.ini                 # Pytest configuration & logging
├── requirements.txt
└── README.md
