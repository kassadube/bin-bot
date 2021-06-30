#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: example_kline_1m_with_unicorn_fy.py
#
# Part of ‘UNICORN Binance WebSocket API’
# Project website: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api
# Documentation: https://oliver-zehentleitner.github.io/unicorn-binance-websocket-api
# PyPI: https://pypi.org/project/unicorn-binance-websocket-api/
#
# Author: Oliver Zehentleitner
#         https://about.me/oliver-zehentleitner
#
# Copyright (c) 2019-2021, Oliver Zehentleitner
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager
import logging
import time
import os


# https://docs.python.org/3/library/logging.html#logging-levels
logging.basicConfig(level=logging.ERROR,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")

# create instance of BinanceWebSocketApiManager
binance_websocket_api_manager = BinanceWebSocketApiManager(exchange="binance.com-futures", output_default="UnicornFy")

markets = {'linkusdt'}

#binance_websocket_api_manager.create_stream('kline_1m', markets, stream_label="UnicornFy", output="UnicornFy")

binance_websocket_api_manager.create_stream('kline_1m', markets, stream_label="dict", output="dict", ping_interval=100)

#binance_websocket_api_manager.create_stream('kline_1m', markets, stream_label="raw_data", output="raw_data")

try:
    while True:
        if binance_websocket_api_manager.is_manager_stopping():
            exit(0)
        oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
        if oldest_stream_data_from_stream_buffer is False:
            print('fff')
            try:
                time.sleep(1)
            except KeyboardInterrupt as ex:
                print('KeyboardInterrupt caught as expected.')
                print('Exception type: %s' % type(ex).__name__)
                exit()   
            print('ddd')
            
        else:
            if oldest_stream_data_from_stream_buffer is not None:
                try:
                    print (oldest_stream_data_from_stream_buffer)
                    if oldest_stream_data_from_stream_buffer['event_time'] >= \
                            oldest_stream_data_from_stream_buffer['kline']['kline_close_time']:
                        # print only the last kline
                        print(f"UnicornFy: {oldest_stream_data_from_stream_buffer}")
                except KeyboardInterrupt:
                    print(f"exxxx")
                except KeyError:
                    print(f"dict: {oldest_stream_data_from_stream_buffer}")
                except TypeError:
                    print(f"raw_data: {oldest_stream_data_from_stream_buffer}") 
except KeyboardInterrupt as ex:
    try:
        # Catch all exceptions and test if it is KeyboardInterrupt, native or
        # PyCharm's.
        

        print('KeyboardInterrupt caught as expected.')
        print('Exception type: %s' % type(ex).__name__)
        exit()

    except ValueError:
        print('ValueError!')            