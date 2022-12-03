import json
import requests
import pandas as pd
import pandas_ta as ta
import os

TIINGO_TOKEN = os.getenv('TIINGO')


def pull_data(ticker: str, start_date: str, time_span: str = None) -> pd.DataFrame:
    headers = {
        'Content-Type': 'application/csv'
    }
    ticker = ticker.lower()
    request_link = "https://api.tiingo.com/tiingo/daily/{}/prices?startDate={}&token={}".format(ticker, start_date,
                                                                                                  TIINGO_TOKEN)
    response = requests.get(request_link, headers=headers)
    data = pd.DataFrame(response.json())
    data = data[['date', 'adjOpen', 'adjHigh', 'adjLow', 'adjClose', 'adjVolume']]
    data = data.rename(
        columns={'adjOpen': 'open', 'adjHigh': 'high', 'adjLow': 'low', 'adjClose': 'close', 'adjVolume': 'volume'})
    data.date = pd.to_datetime(data.date)
    if time_span == 'weekly':
        resample_logic = {
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last',
            'volume': 'sum'
        }
        data = data.resample('W', on='date').apply(resample_logic)

    return data

