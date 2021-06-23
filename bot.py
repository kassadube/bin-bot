import config
from binance.client import Client
from binance.enums import *
import time
import datetime
import numpy as np


client = Client(config.API_KEY, config.API_SECRET)
symbolTicker = 'ADAUSDT'
#print(client.get_account())
status = client.get_account_status()
print(status)
fees = client.get_trade_fee()
#print(fees)
info = client.get_all_isolated_margin_symbols()
#print(info)
orders = client.get_open_margin_orders(symbol=symbolTicker, recvWindow=600)
print(orders)