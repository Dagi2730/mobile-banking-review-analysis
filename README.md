# 📲 Mobile Banking App Reviews Analysis

## ✅ Task 1: Data Collection and Preprocessing

### 🎯 Objective
To collect and clean user review data from the Google Play Store for three major Ethiopian banking apps, ensuring it is ready for analysis.

---

### 🛠️ Methodology

- **Scraping Tool:**  
  Utilized the `google-play-scraper` Python package to fetch user reviews, star ratings, and review dates from the following apps:
  - **Commercial Bank of Ethiopia (CBE):** `com.combanketh.mobilebanking`  
  - **Bank of Abyssinia (BoA):** `com.boa.boaMobileBanking`  
  - **Dashen Bank:** `com.dashen.dashensuperapp`

- **Data Collection:**  
  Targeted a minimum of **400 reviews per app**, resulting in over **1,200 reviews** in total.

- **Data Preprocessing:**  
  - Converted raw data into structured **Pandas DataFrames**  
  - Selected and standardized key fields: `review`, `rating`, `date`, `bank`, and `source`  
  - Cleaned text by removing leading/trailing whitespace and filtering out invalid or missing entries  
  - Removed duplicate reviews to preserve data integrity  
  - Normalized all dates to `YYYY-MM-DD` format for consistency  
  - Dropped rows with missing reviews or ratings  
  - Saved both per-bank and combined cleaned datasets as `.csv` files

---

### 📊 Results

- Collected **400+ cleaned reviews per bank app**, yielding a high-quality dataset
- Generated:
  - `cbe_reviews_clean.csv`  
  - `boa_reviews_clean.csv`  
  - `dashen_reviews_clean.csv`  
  - `all_banks_clean.csv` (combined dataset)

---
