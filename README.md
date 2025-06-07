# Mobile Banking Review Analysis

This project analyzes user satisfaction with mobile banking apps of three Ethiopian banks using reviews from the Google Play Store.

## Objectives

- Scrape 400+ reviews per bank using `google-play-scraper`
- Clean and preprocess review data
- Prepare the data for sentiment analysis and visualization

## Folder Structure

- `data/`: raw and cleaned CSV files
- `scripts/`: scraping and preprocessing scripts
- `notebooks/`: optional notebooks for analysis

## Bank Package IDs

- CBE: `com.combanketh.mobilebanking`
- BOA: `com.boa.boaMobileBanking`
- Dashen: `com.dashen.dashensuperapp`

## Usage

Run `scrape_reviews.py` to collect data and `preprocess_reviews.py` to clean it.
