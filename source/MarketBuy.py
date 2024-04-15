from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import Action
import User
class MarketBuy(Action):
    def execute(self, user: User) -> str: 
        symbol = input("Enter the ticker symbol: ").capitalize()
        qty = float(input("Enter the quantity you wish to trade to 3 decimal points: "))
        side = OrderSide.BUY
        time_in_force = TimeInForce.DAY
        trading_client = user().get_trading_client()

        market_order_data = MarketOrderRequest(symbol, qty, side, time_in_force)
        market_order = trading_client

