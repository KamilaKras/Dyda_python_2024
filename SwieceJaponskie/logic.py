import requests
import pandas as pd
import mplfinance as mpl
import json

def download_data(symbol, interval, limit):
    url = f'https://www.mexc.com/open/api/v2/market/kline?symbol={symbol}&interval={interval}&limit={limit}'
    response = requests.get(url)
    if response.status_code != 200:
        return []
    return response.json()['data']

def change_structure(candlesArray):
    result = []
    for candle in candlesArray:
        result.append({
            'time': candle[0],
            'open': float(candle[1]),
            'close': float(candle[2]),
            'high': float(candle[3]),
            'low': float(candle[4])
        })
    return result

def find_match(candles, last_ten):
    std_candles = [(c['open'] / c['close'] - 1) for c in candles]
    std_last_ten = [(c['open'] / c['close'] - 1) for c in last_ten]
    best_match_idx = -1
    min_difference = float('inf')
    for i in range(len(std_candles) - 10):
        current_segment = std_candles[i:i + 10]
        difference = sum(abs(a - b) for a, b in zip(current_segment, std_last_ten))
        if difference < min_difference:
            min_difference = difference
            best_match_idx = i
    return candles[best_match_idx:best_match_idx + 10]

def draw_plot_candles(title, candles):
    df = pd.DataFrame(candles)
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    df = df.set_index('time')
    mpl.plot(df, type='candle', title=title, style='yahoo', mav=(3, 6, 9))
