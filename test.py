import config
from binance.client import Client
from binance.enums import *
import time
import numpy as np
from IPython.display import display
import pandas as pd                # working with data frames
import datetime as dt              # working with dates
import matplotlib.pyplot as plt    # plot data
import qgrid                       # display dataframe in notebooks 


client = Client(config.API_KEY, config.API_SECRET)
symbolTicker = 'LINKUSDT'





#klines = client.get_historical_klines(symbolTicker, "15m", "1 hour ago UTC",klines_type = HistoricalKlinesType.FUTURES)
klines2 = client.get_historical_klines(symbolTicker, "1m", "15 minutes ago UTC", klines_type = HistoricalKlinesType.FUTURES)
#display(klines2)

df = pd.DataFrame(klines2)
df = df.iloc[:, 0:6]
df.columns = ['datetime', 'open', 'high', 'low', 'close', 'volume']

df.open      = df.open.astype("float")
df.high      = df.high.astype("float")
df.low       = df.low.astype("float")
df.close     = df.close.astype("float")
df.volume    = df.volume.astype("float")
df.datetime = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.datetime]
df.to_csv("fo1.csv")
#display(df)
print(client.get_symbol_ticker(symbol="LINKUSDT"))
print(client.futures_symbol_ticker(symbol="LINKUSDT"))
print(f'200 avg {df.close.mean()}')
#print(f'100 avg {df.close.iloc[100,].mean()}')
#print(f'50 avg {df.close.iloc[150,].mean()}')
print(f'14 avg {df.close.iloc[0:].mean()}')
print(f'14 avg {df.close.iloc[:10].mean()}')
print(df.close.tolist())
print(df.close.to_numpy())

