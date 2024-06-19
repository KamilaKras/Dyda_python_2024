import requests
import json
import pandas as pd
import mplfinance as mpl

def download_data():
    url = 'https://www.mexc.com/open/api/v2/market/kline?symbol=CROWN2_USDT&interval=60m&limit=10' # tutaj należy umieścić adres url który zwraca jsona z danymi na temat świeczek (z poprzedniego zadania z Postmanem)
    response = requests.get(url)
    responseBody = response.text
    responseBodyJson = json.loads(responseBody)
    candlesData = responseBodyJson["data"]
    return candlesData

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

def process_data(formattedCandlesData):
    df = pd.json_normalize(formattedCandlesData)
    df.time = pd.to_datetime(df.time, unit='s')
    df = df.set_index("time")
    print(df.columns)
    print(df.head())
    mpl.plot(
        df,
        type="candle",
        title="Candle chart",
        style="yahoo",
        mav=(3, 6, 9)
    )


print(download_data())
print(change_structure(download_data()))
process_data(change_structure(download_data()))

