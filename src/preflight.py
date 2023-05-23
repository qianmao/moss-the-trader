import os
from binance.client import Client
from rich.console import Console
from datetime import datetime

# Enter your Binance API credentials here
BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET')

console = Console()

with console.status('[bold green]preflight check...') as status:
    client = Client(BINANCE_API_KEY, BINANCE_API_SECRET, tld='us')
    console.log('[bold]:white_check_mark: Connected to Binance')

    client.ping()
    console.log('[bold]:white_check_mark: Pinged the server')

    time_res = client.get_server_time()
    timestamp_millis = time_res['serverTime']
    datetime = str(datetime.fromtimestamp(time_res['serverTime']/1000))
    console.log('[bold]:white_check_mark: Binance server timne: ' + datetime + ' (' + str(timestamp_millis) + ')')

    exchange_info = client.get_exchange_info()
    console.log('[bold]:white_check_mark: Succesfully fetched exchange info.')

    prices = client.get_all_tickers()
    console.log('[bold]:white_check_mark: Succesfully fetched all tickers')

    depth = client.get_order_book(symbol='BTCUSD')
    console.log('[bold]:white_check_mark: Succesfully fetched order book for BTCUSD')

    # fetch 30 minute klines for the last month of 2022
    klines = client.get_historical_klines("ETHUSDT", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2022", "1 Jan, 2023")
    console.log('[bold]:white_check_mark: Succesfully fetched historical klines for ETHUSDT')

    account_info = client.get_account()
    console.log('[bold]:white_check_mark: Succesfully fetched account info')

    usdt_balance = client.get_asset_balance(asset='USDT')
    console.log('[bold]:white_check_mark: Succesfully fetched USDT balance: ' + str(usdt_balance))

    test_order = client.create_test_order(
        symbol='BTCUSDT',
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_MARKET,
        quantity=1)
    console.log('[bold]:white_check_mark: Succesfully placed test order')

    console.log('[bold green]All checks passed!')

    


