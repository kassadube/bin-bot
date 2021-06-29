import config
from binance.client import Client
from binance.enums import *
import time
import datetime
import numpy as np
from IPython.display import display


client = Client(config.API_KEY, config.API_SECRET)
symbolTicker = 'LINKUSDT'
#print(client.get_account())

def _ma50_():
    
    ma50_local = 0
    sum = 0

    klines = client.get_historical_klines(symbolTicker, Client.KLINE_INTERVAL_15MINUTE, "15 hour ago UTC",klines_type = HistoricalKlinesType.FUTURES)
    display(klines)
    if (len(klines)==60):
        for i in range (10,60):
            sum = sum + float(klines[i][4])
        ma50_local = sum / 50

    return ma50_local

print(_ma50_())
