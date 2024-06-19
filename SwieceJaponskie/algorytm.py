import requests
import json
import pandas as pd
import mplfinance as mpl
import numpy as np


def download_data():
    url = 'https://www.mexc.com/open/api/v2/market/kline?symbol=RARI_USDT&interval=1m&limit=100'
    response = requests.get(url)
    if response.status_code != 200:
        return []
    data = response.json()['data']
    return data


def change_structure(candlesArray):
    result = []
    for candle in candlesArray:
        result.append({'time': candle[0],
                       'open': float(candle[1]),
                       'close': float(candle[2]),
                       'high': float(candle[3]),
                       'low': float(candle[4])
                       })
    return result


def find_match(candles, last_ten):
    # liczę wskaźnik
    std_candles = [(c['open'] / c['close'] - 1) for c in candles]
    std_last_ten = [(c['open'] / c['close'] - 1) for c in last_ten]

    # wyszukuję najlepsze dopasowanie
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


try:
    candles = download_data()
    formatted_candles = change_structure(candles)
    last_ten = formatted_candles[-10:]
    match = find_match(formatted_candles[:-10], last_ten)

    # wykresy
    draw_plot_candles("Najnowsze 10 świec", last_ten)
    draw_plot_candles("Znalezione dopasowanie", match)

except:
    print("Coś poszło nie tak")
