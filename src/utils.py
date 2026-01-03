import requests
import time
import requests
import psycopg2
import os

def save_price_to_db(price):
    # Get the connection string from the environment variable we set in Compose
    db_url = os.getenv("DATABASE_URL")

    try:
        # Connect to the database
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()

        # Create table if it doesn't exist
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS bitcoin_prices
                    (
                        id
                        SERIAL
                        PRIMARY
                        KEY,
                        price
                        FLOAT,
                        fetched_at
                        TIMESTAMP
                        DEFAULT
                        CURRENT_TIMESTAMP
                    );
                    """)

        # Insert the price
        cur.execute("INSERT INTO bitcoin_prices (price) VALUES (%s)", (price,))

        conn.commit()
        cur.close()
        conn.close()
        print(f"--- DB Update: Saved ${price} to Postgres ---")
    except Exception as e:
        print(f"Database error: {e}")

def get_crypto_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        price = data['bitcoin']['usd']
        print(f"Current Price: ${price}")

        # Save to DB!
        save_price_to_db(price)
    except Exception as e:
        print(f"Fetch error: {e}")

def save_price_to_file(price):
    # We save it in the 'src' folder which is mapped to your computer
    file_path = "src/prices.log"
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as f:  # "a" means 'append' (add to the end)
        f.write(f"TIMESTAMP: {timestamp} - PRICE: ${price}\n")
    print(f"Saved to {file_path}")

def get_crypto_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        price = data['bitcoin']['usd']
        print(f"Current Bitcoin Price: ${price:,}")

        # Saves to prices.log
        save_price_to_file(price)
        # Save to DB
        save_price_to_db(price)


    except Exception as e:
        print(f"Error: {e}")
