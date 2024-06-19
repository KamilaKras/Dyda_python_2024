import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout
from datetime import datetime, timedelta
import api  # Importing api.py

# Configuration
symbol = 'BTCUSDT'
interval = '5m'
candle_count = 1000
time_step = 60
model_save_path = 'lstm_model.h5'

# Fetching data from the API
df = api.fetch_data(symbol, interval, candle_count)

# Check if data was fetched successfully
if df.empty:
    print("No data fetched. Exiting...")
    exit()

# Processing the data
df['Future_Close'] = df['Close'].shift(-1)
df.dropna(inplace=True)

# Scaling the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df[['Close', 'Future_Close']])

# Creating training and testing data
train_data, test_data = train_test_split(scaled_data, test_size=0.2, shuffle=False)

# Function to create dataset
def create_dataset(data, time_step):
    X, y = [], []
    for i in range(len(data) - time_step):
        X.append(data[i:(i + time_step), 0])
        y.append(data[i + time_step, 1])
    return np.array(X), np.array(y)

# Creating datasets
X_train, y_train = create_dataset(train_data, time_step)
X_test, y_test = create_dataset(test_data, time_step)

# Reshaping input to fit the model input shape
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# Building the LSTM model
model = Sequential()
model.add(LSTM(units=100, return_sequences=True, input_shape=(time_step, 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=75, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Training the model
model.fit(X_train, y_train, epochs=10, batch_size=64, validation_data=(X_test, y_test))

# Save the model
model.save(model_save_path)

# Load the model (if needed)
# model = load_model(model_save_path)

# Making predictions
predictions = model.predict(X_test)
predictions_with_zeros = np.hstack((predictions, np.zeros((predictions.shape[0], 1))))
predicted_prices = scaler.inverse_transform(predictions_with_zeros)[:, 0]

# Visualizing results
df['Open_time'] = pd.to_datetime(df['Open_time'], unit='ms')

# Adjusting array lengths for plotting
hours_to_show = 24
interval_minutes = 5
points_to_show = hours_to_show * 60 // interval_minutes

real_prices_with_zeros = np.hstack((test_data[:, 0].reshape(-1, 1), np.zeros((test_data.shape[0], 1))))
real_prices_scaled = scaler.inverse_transform(real_prices_with_zeros)[:, 0]

# Ensure that we only plot as many points as the shortest array can provide
min_length = min(len(df['Open_time'][-points_to_show:]), len(real_prices_scaled), len(predicted_prices))
time_to_plot = df['Open_time'][-min_length:]
real_prices_to_plot = real_prices_scaled[-min_length:]
predicted_prices_to_plot = predicted_prices[-min_length:]

plt.figure(figsize=(12, 6))
ax = plt.gca()

ax.plot(time_to_plot, real_prices_to_plot, color='blue', label='Actual Prices')
ax.plot(time_to_plot, predicted_prices_to_plot, color='green', label='Predicted Prices')
ax.set_xlabel('Time')
ax.set_ylabel('Price')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.xticks(rotation=20)
ax.legend()
plt.title(f'{interval} BTCUSDT ({candle_count})')
plt.show()
