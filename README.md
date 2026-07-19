# Ford GoBike Large-Scale Data Analysis Pipeline

An end-to-end data engineering and analytics project processing over 1.8 million bike-share records from the San Francisco Bay Area using Python, Pandas, and macOS isolated environments.

## 🛠️ Tech Stack & Environment
* **Language:** Python 3.14
* **Libraries:** Pandas, NumPy, Glob, Zipfile
* **Environment:** macOS Virtual Environment (`venv`)

## 📋 Data Pipeline Architecture

### 1. Ingestion & Merging (`First.py`)
* Dynamically targets zip archives within the local directory.
* Automatically extracts and concatenates 18 monthly CSV datasets into a unified master database without memory exhaustion.

### 2. Cleaning & Feature Engineering (`Second.py`)
* Filters out operational anomalies (trips under 1 minute or exceeding 8 hours).
* Converts raw text timestamps into functional DateTime objects.
* Engineers analytical features: `start_hour`, `start_day_of_week`, `start_month`, `duration_min`, and `member_age`.

### 3. Analytics Engine (`Third.py`)
* Computes high-level operational metrics and user demographic distributions.

## 📊 Core Business Insights
* **Total Records Analyzed:** 1,861,140 clean trips
* **Average Trip Duration:** 13.07 minutes
* **User Segmentation:** Commuter-heavy ecosystem dominated by **Subscribers (85.0%)** vs. casual Customers (15.0%).
* **Temporal Peaks:** Twin demand spikes aligning with standard corporate rush hours: **5:00 PM** (219k+ trips) and **8:00 AM** (206k+ trips).
* **Weekly Cadence:** Peak volume occurs mid-week (Tuesday/Wednesday), dropping by nearly 50% on weekends.
* **Logistical Hotspots:** Highest traffic density heavily concentrated around transit gateways, led by the *San Francisco Ferry Building* (38,392 trips).
