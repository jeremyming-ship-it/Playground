from utils import *
import time
import os

if __name__ == "__main__":
    print("Starting Bitcoin Tracker...")
    while True:
        get_crypto_price()
        print("Waiting 10 seconds for next update...")
        time.sleep(10)