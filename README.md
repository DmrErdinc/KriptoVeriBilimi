
# 💹 Kripto Veri Seti Projeleri – Python ile Kripto Para Analizi

Bu repo, Python kullanılarak geliştirilmiş 4 farklı **kripto para analizi ve takip sistemi** içerir.  
Canlı veri çekimi, Telegram bot entegrasyonu, LSTM ile fiyat tahmini ve portföy hesaplama gibi işlevler sunar.

📁 Ana klasör: `KriptoVeriSeti`

---

## 🔍 Kapsanan Projeler

| Dosya Adı          | Açıklama |
|--------------------|----------|
| `anlik_takip.py`   | En büyük 10 coinin anlık fiyatını, 24s değişimini ve piyasa hacmini gösteren terminal tabanlı takip aracı |
| `fiyat_alarm.py`   | Belirli bir coin (örn: PNUT) belirlenen fiyatın altına düştüğünde Telegram'dan uyarı mesajı gönderir |
| `lstmTahmini.py`   | LSTM modeli ile geçmiş 30 günlük verilere bakarak gelecek fiyatları tahmin eder ve grafikle sunar |
| `portfoyhesapla.py`| Elinizdeki coin’lerin toplam değerini hesaplar ve detaylı tablo ile gösterir |

---

## 🧰 Kullanılan Teknolojiler

- Python 3.10 (zorunlu)
- CoinGecko API (gerçek zamanlı kripto verisi)
- Telegram Bot API (fiyat uyarı sistemi)
- TensorFlow (LSTM fiyat tahmin modeli)
- Pandas, NumPy, Matplotlib, Scikit-learn (veri işleme ve görselleştirme)
- Schedule (otomatik alarm çalıştırma)

---

## ⚙️ Kurulum – Adım Adım

### 1. Python 3.10 Yükle  
🔗 [Python 3.10.9 İndir](https://www.python.org/downloads/release/python-3109/)  
> ❗ Python 3.13 desteklenmemektedir, TensorFlow çalışmaz.

### 2. Sanal Ortam Oluştur (opsiyonel ama önerilir)
```bash
cd KriptoVeriSeti
python3.10 -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3. Gerekli Kütüphaneleri Kur
```bash
pip install requests pandas numpy matplotlib scikit-learn tensorflow schedule python-telegram-bot==13.15
```

---

## ▶️ Modül Kullanım Rehberi

### 📟 Anlık Coin Takibi (100 büyük coin):
```bash
python anlik_takip.py
```

### 🔔 Fiyat Alarm Botu (Telegram):
1. Telegram’da @BotFather ile bot oluştur
2. Bot token'ını ve chat_id’ni al
3. `fiyat_alarm.py` içinde:
   ```python
   TELEGRAM_TOKEN = "bot_token"
   CHAT_ID = "senin_chat_id"
   ```
4. Terminalde çalıştır:
```bash
python fiyat_alarm.py
```

### 📈 LSTM ile Fiyat Tahmini:
```bash
python lstmTahmini.py
```
> Son 30 günlük fiyatlara göre tahmin yapar ve grafikle sunar.

### 💰 Portföy Hesaplama:
```bash
python portfoyhesapla.py
```
> Kendi portföyünü sözlük olarak düzenle:
```python
portfoy = {
    "bitcoin": 0.1,
    "ethereum": 1.2,
    "pnut": 5000
}
```

---

## 📡 Veri Kaynağı

CoinGecko API → [https://www.coingecko.com/en/api](https://www.coingecko.com/en/api)  
Her API çağrısı için saniyede 10 isteğe kadar ücretsiz.

---

## 🧠 Gelecekte Geliştirme Planları

- 📲 Streamlit tabanlı web arayüzü
- 🧠 Çoklu model karşılaştırmaları (ARIMA vs LSTM)
- 🔐 Kullanıcı kayıt sistemi (portföy takibi için)
- 📊 WebSocket ile canlı grafik paneli

---

## 🖼️ Örnek Ekran Görüntüleri 

> LSTM Tahmin Grafiği  KriptoVeriSeti/Grafik.png
> Telegram'dan gelen uyarı mesajı  
> Anlık takip terminal çıktısı  
> Portföy hesaplama tablosu

---

## 👨‍💻 Geliştirici

**Erdinç**  
🔗 GitHub: [github.com/DmrErdinc](https://github.com/DmrErdinc)

MIT License © 2025

---
