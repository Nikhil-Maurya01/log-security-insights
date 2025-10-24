# Log Security Insights (Python Log Analyzer + CSV Report)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg?style=for-the-badge&logo=python&logoColor=ffdd54)
![Log Analysis](https://img.shields.io/badge/Log%20Analysis-HTTP%20Access%20Log?style=for-the-badge&logo=log&logoColor=ffdd54)
![Security](https://img.shields.io/badge/Threat%20Detection-red.svg?style=for-the-badge&logo=lock&logoColor=ffdd54)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge&logo=license&logoColor=ffdd54)

A lightweight Python tool that scans HTTP access logs to detect suspicious activity (e.g., failed login attempts, bot traffic) and generates a structured CSV report for quick threat analysis.

---

## ✨ Highlights

- **Regex-based log parsing** for IPs and status codes.
- **Security-focused filtering** (e.g., 401/403 status codes).
- **CSV output** for easy reporting and visualization.
- **Modular Python script** for quick integration or automation.

---

## ⚙️ Tech Stack

- **Python 3.9+**
- **Regex** for log parsing
- **CSV module** for report generation
- **Standard HTTP access logs** as input

---

## 📁 Sample Output

The tool generates a `security_report.csv` with columns:
- `IP Address`
- `Failed Attempts`

Example :

| IP Address | Failed Attempts |
|-------------|-------------|
| `5.134.128.102` | 176 |
| `37.9.113.152` | 309 |
| `5.45.207.88` | 27 |
| `37.9.113.36` | 62 |
| `37.9.113.126` | 117 |

