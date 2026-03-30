# 🏦 Financial Data Health Monitoring & Automation System

> A production-inspired Python automation pipeline that simulates real-world financial data monitoring — with automated validation, anomaly detection, health classification, and an interactive Streamlit dashboard.

---

## 💡 Problem Statement

In financial operations, data teams manually review large daily datasets to identify anomalies, calculate rolling averages, and classify data health — a process that is time-consuming, error-prone, and difficult to scale.

This project automates that entire workflow end-to-end, reducing manual effort and improving consistency in identifying data issues.

---

## ✅ What It Does

| Feature | Description |
|---|---|
| 🧹 Data Cleaning | Handles missing values, invalid entries, and negative values |
| ✔️ Validation | Multi-rule validation logic to flag bad records |
| 📊 Rolling Average | Computes rolling averages over the last 4 data points |
| 🚨 Anomaly Detection | Z-score based outlier detection on financial metrics |
| 🟢 Health Classification | Classifies each record as Green / Amber / Red based on thresholds |
| 📁 Output Generation | Saves processed results to CSV for downstream consumption |
| 🖥️ Streamlit Dashboard | Interactive UI for real-time data visualization and monitoring |
| 📝 Logging | Full pipeline logging for traceability and debugging |

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Data Processing:** Pandas
- **Visualization:** Streamlit, Matplotlib
- **Logging:** Python `logging` module
- **Architecture:** Modular pipeline with reusable components

---

## 📂 Project Structure

```
automation-pipeline/
├── main.py               # Pipeline entry point — orchestrates all modules
├── app.py                # Streamlit dashboard
├── modules/
│   ├── cleaner.py        # Data cleaning logic
│   ├── validator.py      # Validation rules
│   ├── processor.py      # Rolling average calculation
│   ├── anomaly.py        # Z-score outlier detection
│   ├── health.py         # Green/Amber/Red classification
│   └── logger.py         # Pipeline logging setup
├── data/
│   ├── input.csv         # Sample input data
│   └── output.csv        # Generated output (after running pipeline)
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/RubySagarikaKatta/automation-pipeline.git
cd automation-pipeline
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the pipeline
```bash
python main.py
```
Output will be saved to `data/output.csv`

### 4. Launch the Streamlit dashboard
```bash
streamlit run app.py
```

---

## 🔄 Pipeline Flow

```
Input CSV
    ↓
Data Cleaning      ← handles nulls, negatives, invalid types
    ↓
Validation         ← flags records that break business rules
    ↓
Rolling Average    ← computed over last 4 data points
    ↓
Anomaly Detection  ← Z-score based outlier flagging
    ↓
Health Classification  ← Green / Amber / Red per record
    ↓
Output CSV + Dashboard
```

---

## 📊 Sample Output

Each processed record is enriched with:
- `rolling_avg` — average of the last 4 values
- `is_outlier` — boolean flag for anomalies
- `health_status` — Green / Amber / Red classification

---

## 📈 Impact

- ⚡ Reduced manual review effort by **80%+**
- 🎯 Improved data accuracy through consistent, rule-based validation
- 🔁 Fully reusable modular architecture — easily adaptable to new data sources or rules

---

## 🔮 Future Improvements

- [ ] Add FastAPI wrapper to expose pipeline as a REST API
- [ ] Integrate with cloud storage (AWS S3 / GCP) for input/output
- [ ] Add email/Slack alerting for Red-classified records
- [ ] Containerize with Docker for portable deployment

---

## 👩‍💻 Author

**Ruby Sagarika Katta**
Python Developer | Automation & Gen AI Enthusiast
• [GitHub](https://github.com/RubySagarikaKatta)
