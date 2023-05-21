import time
from binance.client import Client
from binance.enums import *

# Enter your Binance API credentials here
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'

# Create a Binance client
client = Client(API_KEY, API_SECRET)

# Define the symbol to trade
symbol = 'BTCUSDT'

# Define trading parameters
quantity = 0.001  # The quantity of Bitcoin to buy/sell
profit_percent = 0.02  # The desired profit percentage (2%)

# Define trading states
IN_POSITION = False  # Indicates whether we have an open position
BOUGHT_PRICE = 0.0  # The price at which we bought the asset

def place_buy_order(symbol, quantity):
    try:
        buy_order = client.create_order(
            symbol=symbol,
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )
        return buy_order['fills'][0]['price']
    except Exception as e:
        print('An error occurred during the buy order placement:', e)
        return None

def place_sell_order(symbol, quantity):
    try:
        sell_order = client.create_order(
            symbol=symbol,
            side=SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )
        return sell_order['fills'][0]['price']
    except Exception as e:
        print('An error occurred during the sell order placement:', e)
        return None

while True:
    try:
        # Check if we have an open position
        if IN_POSITION:
            current_price = float(client.get_symbol_ticker(symbol=symbol)['price'])
            profit_threshold = BOUGHT_PRICE * (1 + profit_percent)

            # Check if the current price has reached the profit threshold
            if current_price >= profit_threshold:
                sell_price = place_sell_order(symbol, quantity)
                if sell_price:
                    print('Sold at price:', sell_price)
                    IN_POSITION = False
                    BOUGHT_PRICE = 0.0
            else:
                time.sleep(5)  # Wait for 5 seconds before checking again
        else:
            # Place a buy order
            buy_price = place_buy_order(symbol, quantity)
            if buy_price:
                print('Bought at price:', buy_price)
                IN_POSITION = True
                BOUGHT_PRICE = float(buy_price)

    except Exception as e:
        print('An error occurred:', e)
        time.sleep(5)  # Wait for 5 seconds before trying again
