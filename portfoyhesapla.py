import requests
import pandas as pd

# Kullanıcının portföyü (coin miktarları)
portfoy = {
    "bitcoin": 0.1,
    "ethereum": 0.5,
    "pnut": 10000
}

def fiyatlari_cek(coinler, vs_currency="usd"):
    ids = ",".join(coinler)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies={vs_currency}"
    response = requests.get(url)
    return response.json()

def portfoy_degeri_hesapla(portfoy, fiyatlar):
    toplam = 0
    detaylar = []

    for coin, miktar in portfoy.items():
        fiyat = fiyatlar[coin]["usd"]
        deger = fiyat * miktar
        detaylar.append({
            "Coin": coin.upper(),
            "Miktar": miktar,
            "Fiyat (USD)": fiyat,
            "Toplam (USD)": deger
        })
        toplam += deger

    df = pd.DataFrame(detaylar)
    print(df)
    print(f"💰Toplam Portföy Değeri: {toplam:.2f} USD")

# Çalıştır
coinler = list(portfoy.keys())
fiyatlar = fiyatlari_cek(coinler)
portfoy_degeri_hesapla(portfoy, fiyatlar)
