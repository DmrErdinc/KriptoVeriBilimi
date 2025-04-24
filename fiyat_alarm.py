import requests
import time
import schedule
from telegram import Bot

# 🛠️ Telegram ayarları
TELEGRAM_TOKEN = "7679182060:AAE3wMHk9v56Ayhw5fWcNkNEUylFhKVXts8"
CHAT_ID = "5528946397"

bot = Bot(token=TELEGRAM_TOKEN)

# 🔍 PNUT Coin için ayarlar (CoinGecko ID: "pnut")
COIN = "pnut"
CURRENCY = "usd"  # CoinGecko'da "usdt" yok, ama "usd" stabil olduğu için aynı sonucu verir
ALARM_ALT =0,1545  # Örneğin0,1545 USDT altına düşerse alarm verir

def kontrol_et():
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={COIN}&vs_currencies={CURRENCY}"
    response = requests.get(url)
    price = response.json()[COIN][CURRENCY]

    print(f"Anlık {COIN.upper()} fiyatı: {price} {CURRENCY.upper()}")

    if price < ALARM_ALT:
        mesaj = f"⚠️ {COIN.upper()} fiyatı {price} {CURRENCY.upper()} altına düştü! 🚨"
        bot.send_message(chat_id=CHAT_ID, text=mesaj)

# ⏰ Her 1 dakikada bir kontrol
schedule.every(1).minutes.do(kontrol_et)

print("📡 PNUT fiyat alarm sistemi başlatıldı...")
while True:
    schedule.run_pending()
    time.sleep(1)
