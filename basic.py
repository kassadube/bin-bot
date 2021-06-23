import asyncio
import json

from binance import AsyncClient, DepthCacheManager, BinanceSocketManager


async def main():

    # initialise the client
    client = await AsyncClient.create()

    # run some simple requests
    #print(json.dumps(await client.get_exchange_info(), indent=2))

    print(json.dumps(await client.get_symbol_ticker(symbol="BTCUSDT"), indent=2))

    # initialise websocket factory manager
    bsm = BinanceSocketManager(client)

    # create listener using async with
    # this will exit and close the connection after 5 messages
    async with bsm.trade_socket('ETHUSDT') as ts:
        for _ in range(20):
            res = await ts.recv()
            print(f'recv {res}')

    # get historical kline data from any date range

    # fetch 1 minute klines for the last day up until now
    klines = await client.get_historical_klines("ETHUSDT", AsyncClient.KLINE_INTERVAL_1MINUTE, "1 hour ago UTC")
    print(klines)
    # use generator to fetch 1 minute klines for the last day up until now
    ## async for kline in await client.get_historical_klines_generator("ETHUSDT", AsyncClient.KLINE_INTERVAL_1MINUTE, "1 day ago UTC"):
    ##    print(kline)

    
    # fetch 30 minute klines for the last month of 2017
    ##klines = await client.get_historical_klines("MATICUSDT", client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2020", "1 Jan, 2021")
    ##print(klines)
    
    # fetch weekly klines since it listed
    ##klines = await client.get_historical_klines("NEOUSDT", client.KLINE_INTERVAL_1WEEK, "1 Jan, 2020")
    ##print(klines)

     # setup an async context the Depth Cache and exit after 5 messages
    async with DepthCacheManager(client, symbol='ETHUSDT') as dcm_socket:
        for _ in range(5):
            depth_cache = await dcm_socket.recv()
            print(f"symbol {depth_cache.symbol} updated:{depth_cache.update_time}")
            print("Top 5 asks:")
            print(depth_cache.get_asks()[:5])
            print("Top 5 bids:")
            print(depth_cache.get_bids()[:5])


    await client.close_connection()
   

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())