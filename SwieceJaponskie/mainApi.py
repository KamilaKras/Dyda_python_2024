import api
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Pobranie danych z API
symbol = 'BTCUSDT'
interval = '5m'
candle_count = 1000
df = api.fetch_data(symbol, interval, candle_count)

# Przetwarzanie danych
df['Future_Close'] = df['Close'].shift(-1)
df.dropna(inplace=True)

# Skalowanie danych
scaler = MinMaxScaler(feature_range=(0,1))
scaler_data = scaler.fit_transform(df[['Close', 'Future_Close']])

# Tworzenie danych treningowych i testowych
train_size = int(len(scaler_data) * 0.8)
train_data = scaler_data[:train_size]
test_data = scaler_data[train_size:]

# Funkcja tworząca dane do modelu
def create_dataset(data, time_step):
    X, y = [], []
    for i in range(len(data) - time_step):
        X.append(data[i:(i + time_step), 0])
        y.append(data[i + time_step, 1])
    return np.array(X), np.array(y)

# Tworzenie zestawu danych
time_step = 60
X_train, y_train = create_dataset(train_data, time_step)
X_test, y_test = create_dataset(test_data, time_step)

# Reshape input do formatu [samples, time steps, features]
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# Model
model = Sequential()
model.add(LSTM(units=100, return_sequences=True, input_shape=(time_step, 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=75))
model.add(Dropout(0.2))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

# Trening modelu
model.fit(X_train, y_train, epochs=10, batch_size=64, validation_data=(X_test, y_test))

# Predykcja
predictions = model.predict(X_test)
predictions_with_zeros = np.hstack((predictions, np.zeros((predictions.shape[0], 1))))
predicted_prices = scaler.inverse_transform(predictions_with_zeros)[:, 0]

# Generowanie prognoz
future_steps = 5
future_predictions = []
last_sequence = X_test[-1:]
for _ in range(future_steps):
    last_prediction = model.predict(last_sequence)
    future_predictions.append(last_prediction[0, 0])
    last_sequence = np.roll(last_sequence, -1, axis=1)
    last_sequence[0, -1, 0] = last_prediction[0, 0]

future_prices_array = np.array(future_predictions).reshape(-1, 1)
future_prices_scaled = np.hstack((future_prices_array, np.zeros((future_prices_array.shape[0], 1))))
future_predictions = scaler.inverse_transform(future_prices_scaled)[:, 0]

# Przygotowanie danych
test_data_with_zeros = np.hstack((test_data[time_step + 1:, 0].reshape(-1, 1), np.zeros((test_data[time_step + 1:, 0].reshape(-1, 1).shape[0], 1))))
real_prices_scaled = scaler.inverse_transform(test_data_with_zeros)[:, 0]

df['Open_time'] = pd.to_datetime(df['Open_time'], unit='ms')


# Rysowanie wykresu

plt.figure(figsize=(12, 6))
ax = plt.gca()
hours_to_show = 24
points_to_show = hours_to_show * 60 // 5

data_points = len(df['Open_time'])
if data_points < points_to_show:
    points_to_show = data_points  # Adjust to show all points we have

times_to_show = df['Open_time'][-points_to_show:]

# Check to ensure the length matches
if len(real_prices_scaled) >= points_to_show:
    real_prices_to_show = real_prices_scaled[-points_to_show:]
    ax.plot(times_to_show, real_prices_to_show, color='blue', label='Real prices')
else:
    # Not enough data to display as requested
    print("Not enough data to display the requested number of points.")

#ax.plot(times_to_show, real_prices_scaled[-points_to_show:], color='blue', label='Real prices')
ax.plot(times_to_show, predicted_prices[-points_to_show:], color='green', label='Predicted prices')

last_time = df['Open_time'].iloc[-1]
future_times = [last_time + timedelta(minutes=5 * i) for i in range(1, future_steps + 1)]
ax.plot(future_times, future_predictions, color='red', linestyle='dashed', label='Predicted prices')

ax.set_xlabel('Time')
ax.set_ylabel('Price')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.xticks(rotation=20)
plt.title(f'{interval} {symbol} ({candle_count})')
plt.legend()
plt.show()
