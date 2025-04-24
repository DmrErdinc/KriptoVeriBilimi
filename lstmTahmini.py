
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

# 1. Veri Çekimi (PNUT için son 30 gün)
def veri_cek(coin_id="pnut", currency="usd", days=30):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": currency, "days": days}
    response = requests.get(url, params=params)
    data = response.json()["prices"]
    df = pd.DataFrame(data, columns=["timestamp", "price"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)
    return df

# 2. Veri Ön İşleme
def veri_hazirla(df):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df[["price"]])

    X, y = [], []
    seq_length = 10
    for i in range(seq_length, len(scaled_data)):
        X.append(scaled_data[i-seq_length:i, 0])
        y.append(scaled_data[i, 0])
    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    return X, y, scaler

# 3. LSTM Modeli
def modeli_egit(X, y):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], 1)))
    model.add(LSTM(units=50))
    model.add(Dense(1))
    model.compile(optimizer="adam", loss="mean_squared_error")
    model.fit(X, y, epochs=20, batch_size=16, verbose=0)
    return model

# 4. Tahmin ve Görselleştirme
def tahmin_et(model, X, scaler, df):
    predicted = model.predict(X)
    predicted_prices = scaler.inverse_transform(predicted)

    real_prices = df["price"].values[10:]

    # Görsel
    plt.figure(figsize=(10, 6))
    plt.plot(real_prices, label="Gerçek Fiyat")
    plt.plot(predicted_prices, label="Tahmin")
    plt.title("PNUT/USD Fiyat Tahmini")
    plt.xlabel("Gün")
    plt.ylabel("Fiyat (USD)")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

# Ana Akış
df = veri_cek()
X, y, scaler = veri_hazirla(df)
model = modeli_egit(X, y)
tahmin_et(model, X, scaler, df)
