from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from Action import Action
from User import User
class MarketBuy(Action):
    def execute(self, user: User) -> str: 
        symbol = input("Enter the ticker symbol: ").capitalize()
        qty = float(input("Enter the quantity you wish to trade to 3 decimal places: "))
        side = OrderSide.BUY
        time_in_force = TimeInForce.DAY
        trading_client = user.get_trading_client()

        market_order_data = MarketOrderRequest(symbol, qty, side, time_in_force)
        market_order = trading_client.submit_order(market_order_data)
        return "Order placed!"
    
    def menudescription(self) -> str:
        return "Buy a stock at the current market price."
