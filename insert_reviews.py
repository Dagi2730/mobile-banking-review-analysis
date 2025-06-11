import cx_Oracle
from datetime import datetime

# Define connection credentials
username = "bank_reviews"
password = "Dagi2730"
dsn = cx_Oracle.makedsn("localhost", 1522, service_name="XEPDB1")

def insert_sample_data():
    connection = None
    cursor = None
    try:
        # Establish connection
        connection = cx_Oracle.connect(username, password, dsn)
        cursor = connection.cursor()

        # Insert sample banks (if not already present)
        banks = [
            ('Commercial Bank of Ethiopia', 'com.combanketh.mobilebanking'),
            ('Dashen Bank', 'com.dashen.dashensuperapp'),
            ('Bank of Abyssinia', 'com.boa.boaMobileBanking'),
        ]

        for bank_name, app_package in banks:
            try:
                cursor.execute("""
                    INSERT INTO banks (bank_name, app_package)
                    VALUES (:1, :2)
                """, (bank_name, app_package))
            except cx_Oracle.IntegrityError:
                pass  # Bank already exists

        connection.commit()

        # Get bank_id values for inserting reviews
        cursor.execute("SELECT bank_id, bank_name FROM banks")
        bank_id_map = {name: bid for bid, name in cursor.fetchall()}

        # Insert sample reviews
        sample_reviews = [
            {
                "bank_name": "Commercial Bank of Ethiopia",
                "review_text": "App is very slow and crashes frequently.",
                "rating": 2,
                "review_date": datetime(2025, 6, 1),
                "sentiment": "Negative",
                "keywords": "slow, crashes",
                "theme": "Performance Issues"
            },
            {
                "bank_name": "Dashen Bank",
                "review_text": "Great interface and easy to use.",
                "rating": 5,
                "review_date": datetime(2025, 6, 2),
                "sentiment": "Positive",
                "keywords": "great, interface, easy",
                "theme": "User Experience"
            },
            {
                "bank_name": "Bank of Abyssinia",
                "review_text": "Customer support is unhelpful.",
                "rating": 1,
                "review_date": datetime(2025, 6, 3),
                "sentiment": "Negative",
                "keywords": "customer support, unhelpful",
                "theme": "Customer Service"
            },
        ]

        for review in sample_reviews:
            bank_id = bank_id_map.get(review["bank_name"])
            if bank_id:
                cursor.execute("""
                    INSERT INTO reviews 
                    (bank_id, review_text, rating, review_date, sentiment, keywords, theme)
                    VALUES (:1, :2, :3, :4, :5, :6, :7)
                """, (
                    bank_id,
                    review["review_text"],
                    review["rating"],
                    review["review_date"],
                    review["sentiment"],
                    review["keywords"],
                    review["theme"]
                ))

        connection.commit()
        print("✅ Sample data inserted successfully.")

    except cx_Oracle.Error as e:
        print("❌ Error occurred:", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    insert_sample_data()
