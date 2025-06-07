# Mobile Banking App Reviews Analysis

## Task 1: Data Collection and Preprocessing

### Objective
Scrape user reviews from Google Play Store for three Ethiopian bank mobile apps and preprocess the data for further analysis.

### Methodology

- **Scraping:**  
  Used the `google-play-scraper` Python package to collect user reviews, ratings, and review dates for the following bank apps:  
  - CBE: `com.combanketh.mobilebanking`  
  - BOA: `com.boa.boaMobileBanking`  
  - Dashen Bank: `com.dashen.dashensuperapp`  

- **Data Collection:**  
  Targeted a minimum of 400 reviews per app, resulting in over 1200 reviews in total.

- **Preprocessing:**  
  - Converted the scraped data into pandas DataFrames.  
  - Selected relevant columns: review text, rating, date, bank name, and source.  
  - Cleaned review texts by trimming whitespace and handling missing or non-string entries.  
  - Removed duplicate reviews to ensure data quality.  
  - Dropped rows with missing reviews or ratings.  
  - Normalized dates to the `YYYY-MM-DD` format for consistency.  
  - Saved cleaned individual CSV files per bank and a combined CSV file for all banks.

### Results

- Successfully collected and cleaned 400 reviews per bank app.  
- Generated clean CSV files ready for exploratory data analysis.

---

## How to Run the Scripts

- Install dependencies using `pip install -r requirements.txt`.  
- Run the scraping and preprocessing script: `python scrape_and_preprocess.py`.

---

