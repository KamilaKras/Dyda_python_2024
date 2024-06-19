import requests
import pandas as pd

def fetch_data(symbol, interval, candle_count):
    url = 'https://api.binance.com/api/v3/klines'
    limit = 1000  # Maximum number of candles per request
    all_candles = []

    try:
        if candle_count <= limit:
            # If we need less or equal to 1000 candles
            params = {'symbol': symbol, 'interval': interval, 'limit': candle_count}
            data = requests.get(url, params=params).json()
            all_candles = data + all_candles
        else:
            # If we need more than 1000 candles
            iterations = candle_count // limit  # Number of full iterations
            remaining = candle_count % limit  # Remaining candles to fetch

            # Fetch data in batches
            end_time = None  # Initially no specific end time
            for _ in range(iterations):
                params = {'symbol': symbol, 'interval': interval, 'limit': limit, 'endTime': end_time}
                data = requests.get(url, params=params).json()
                all_candles = data + all_candles
                end_time = data[0][0]  # Set end time to the start of the fetched batch

            # Fetch the remaining candles
            if remaining > 0:
                params = {'symbol': symbol, 'interval': interval, 'limit': remaining, 'endTime': end_time}
                data = requests.get(url, params=params).json()
                all_candles = data + all_candles

        # Create DataFrame from fetched data
        df = pd.DataFrame(all_candles, columns=['Open_time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time',
                                                'Quote_asset_volume', 'Number_of_trades', 'Taker_buy_base_asset_volume',
                                                'Taker_buy_quote_asset_volume', 'Ignore'])
        df['Close'] = df['Close'].astype(float)
        return df

    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error
