import config
from binance.client import Client
from binance.enums import *
import time
import datetime as dt
import numpy as np
from IPython.display import display


client = Client(config.API_KEY, config.API_SECRET)
symbolTicker = 'LINKUSDT'

enddate = dt.datetime.now()
tmd = dt.timedelta(minutes=10)
startdate = dt.datetime.now() - tmd

print (f"startDate {dt.datetime.timestamp(startdate)}")
print (f"endDate {dt.datetime.timestamp(dt.datetime.now())}")

date_time = dt.datetime.fromtimestamp(1624965204.864095)
print(date_time)



klines = client.get_historical_klines(symbolTicker, "15m", "1 hour ago UTC",klines_type = HistoricalKlinesType.FUTURES)
klines2 = client.get_historical_klines(symbolTicker, "15m", dt.datetime.timestamp(startdate), dt.datetime.timestamp(dt.datetime.now()), klines_type = HistoricalKlinesType.FUTURES)
display(klines2)


