import requests
import pandas as pd
from tabulate import tabulate

def veri_cek():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": "false"
    }
    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame([{
        "Coin": coin["name"],
        "Fiyat (USD)": coin["current_price"],
        "24s Değişim (%)": coin["price_change_percentage_24h"],
        "Hacim (USD)": coin["total_volume"],
        "Market Cap": coin["market_cap"]
    } for coin in data])

    print(tabulate(df, headers="keys", tablefmt="fancy_grid"))

veri_cek()
