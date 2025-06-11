# Mobile Banking App Reviews Analysis
# 🚀 Task 3: Oracle Storage - Mobile Banking Reviews

## 📋 Overview
This task focuses on inserting **cleaned mobile banking app reviews** from CSV files into an **Oracle database**.  

The data is organized into two main tables:  
- 🏦 **banks**: stores bank details (name, app package)  
- 📝 **reviews**: stores individual reviews linked to banks, including review text, rating, sentiment, keywords, and themes

The script reads cleaned CSV files for each bank and inserts their review data into the database.

---

## 📁 File Structure

- `insert_cleaned_reviews.py` — Python script to load CSV files and insert data into Oracle  
- `notebook/data/` — Folder containing cleaned review CSVs for each bank:  
  - `boa_reviews_cleaned.csv`  
  - `dashen_reviews_cleaned.csv`  
  - `cbe_reviews_cleaned.csv`  

---

## ⚙️ Prerequisites

- Oracle Database up and running  
- Python package `cx_Oracle` installed (`pip install cx_Oracle`)  
- Oracle Instant Client installed and configured  
- Python 3.7+  

---

## 🚦 Usage Instructions

1. Update Oracle DB credentials & DSN in `insert_cleaned_reviews.py`:

   ```python
   username = "bank_reviews"
   password = "Dagi2730"
   dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")
