# Mobile Banking App Reviews Analysis
# 📊 Task 4 – Exploratory Data Analysis (EDA) and Sentiment Visualization

## ✅ Objective

This task focuses on performing Exploratory Data Analysis (EDA) and visualizations on cleaned and sentiment-annotated user reviews of mobile banking apps from three major Ethiopian banks:
- Bank of Abyssinia (BoA)
- Commercial Bank of Ethiopia (CBE)
- Dashen Bank

The goal is to extract insights into the sentiment trends, review characteristics, and comparative performance of each bank based on customer feedback.

---

## 📁 Data Used

Processed review datasets with sentiment scores were used from the `data/processed/` directory:
- `boa_reviews_sentiment.csv`
- `cbe_reviews_sentiment.csv`
- `dashen_reviews_sentiment.csv`

Each dataset includes:
- Original and cleaned review text
- Sentiment polarity score (from VADER)
- Sentiment classification (`positive`, `neutral`, `negative`)
- Review length and associated metadata

---

## 📊 Visualizations Performed

1. ### Sentiment Score Distribution per Bank (Boxplot)
   - Compares the spread and concentration of sentiment scores across banks.

2. ### Sentiment Class Distribution (Count Plot)
   - Shows the number of positive, neutral, and negative reviews per bank.

3. ### Review Length Distribution (Histogram)
   - Analyzes the distribution of review lengths to understand how detailed user feedback tends to be.

4. ### Sentiment vs. Review Length (Scatter Plot)
   - Investigates whether longer reviews are more positive or negative.

5. ### Average Sentiment per Bank (Bar Plot)
   - Compares the average sentiment polarity score for each bank.

---

## 🔍 Key Insights

- **CBE** has the highest average sentiment score, indicating generally more favorable reviews.
- **Dashen** and **BoA** have a wider spread in sentiment, suggesting more variability in customer experience.
- **Longer reviews** are often associated with more negative sentiment, pointing to detailed complaints or user frustration.
- Positive reviews dominate across all banks, but **Dashen** shows slightly more negative feedback.

---

## 📓 Notebook

All analyses and visualizations are contained in the notebook:

