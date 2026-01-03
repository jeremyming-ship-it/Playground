import requests
import time

def get_crypto_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        price = data['bitcoin']['usd']
        print(f"Current Bitcoin Price: ${price:,}")
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    print("Starting Bitcoin Tracker...")
    while True:
        get_crypto_price()
        print("Waiting 10 seconds for next update...")
        time.sleep(10)