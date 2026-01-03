import requests
import time

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
        save_price_to_file(price)
    except Exception as e:
        print(f"Error: {e}")
