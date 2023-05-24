import ccxt
import os
from rich.console import Console
from datetime import datetime

BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET')

console = Console()

with console.status('[bold green]preflight check...') as status:
    supported_exchanges = ' '.join(ccxt.exchanges)
    console.log('[bold]:white_check_mark: Supported exchanges: ' + supported_exchanges)

    exchange = ccxt.binanceus({
        'apiKey': BINANCE_API_KEY,
        'secret': BINANCE_API_SECRET,
    })
    console.log('[bold]:white_check_mark: Connected to BinanceUS')

    timestamp_millis = exchange.fetch_time()
    datetime = str(datetime.fromtimestamp(timestamp_millis/1000))
    console.log('[bold]:white_check_mark: Binance server timne: ' + datetime + ' (' + str(timestamp_millis) + ')')

    order_book = exchange.fetch_order_book(symbol='BTCUSD', limit=1)
    console.log('[bold]:white_check_mark: Succesfully fetched order book for BTCUSD: ' + str(order_book))

    ticker = exchange.fetch_ticker(symbol='ETHUSD')
    console.log('[bold]:white_check_mark: Succesfully fetched ticker for ETHUSD: ' + str(ticker))

    klines = exchange.fetch_ohlcv(symbol='DOGEUSD', timeframe='1m', limit=1)
    console.log('[bold]:white_check_mark: Succesfully fetched klines for DOGEUSD: ' + str(klines))

    trade = exchange.fetch_trades(symbol='SOLUSD', limit=1)
    console.log('[bold]:white_check_mark: Succesfully fetched trades for SOLUSD: ' + str(trade))

    account_balance = exchange.fetch_balance()
    console.log('[bold]:white_check_mark: Succesfully fetched account balance.')

    # Make sure you set test params otherwise you will place REAL order!
    order = exchange.create_order('USDTUSD', 'limit', 'buy', 1.0, 1.0, {'test': True})
    console.log('[bold]:white_check_mark: Succesfully placed test order: ' + str(order))

    console.log('[bold green]All checks passed!')

    


