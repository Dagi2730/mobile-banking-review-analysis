import cx_Oracle
import pandas as pd
import os

# Absolute path to the cleaned review CSV files
data_dir = r"C:\Users\HP\Desktop\mobile-banking-review-analysis\notebook\data"

# Database connection info
username = "system"
password = "your_password"  # Replace with your actual password
dsn = "localhost:1522/XE"   # Adjust the port (1522) if your listener uses a different one

def insert_reviews_from_csv(bank_file, bank_name):
    # Full path to the CSV file
    csv_file_path = os.path.join(data_dir, f"{bank_file}.csv")

    if not os.path.exists(csv_file_path):
        print(f"CSV file not found: {csv_file_path}")
        return

    # Load the cleaned reviews CSV
    df = pd.read_csv(csv_file_path)

    try:
        # Connect to the Oracle database
        connection = cx_Oracle.connect(username, password, dsn)
        cursor = connection.cursor()

        # Insert each review
        for _, row in df.iterrows():
            review_text = row.get("review", "")
            rating = row.get("rating", None)
            sentiment = row.get("sentiment", "")
            theme = row.get("theme", "")

            cursor.execute("""
                INSERT INTO cleaned_reviews (bank_name, review, rating, sentiment, theme)
                VALUES (:1, :2, :3, :4, :5)
            """, (bank_name, review_text, rating, sentiment, theme))

        # Commit and clean up
        connection.commit()
        print(f"✅ Inserted reviews for {bank_name} successfully.")

    except cx_Oracle.DatabaseError as e:
        print(f"❌ Oracle DB error: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Insert reviews for all three banks
insert_reviews_from_csv("boa_reviews_cleaned", "Bank of Abyssinia")
insert_reviews_from_csv("dashen_reviews_cleaned", "Dashen Bank")
insert_reviews_from_csv("cbe_reviews_cleaned", "Commercial Bank of Ethiopia")
