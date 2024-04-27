from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from lumibot.strategies.strategy import Strategy
from Buy import Buy
from User import User

class MarketBuy(Buy, Strategy):
    def __init__(self, user: User, symbol: str, qty: float, time_in_force: TimeInForce=TimeInForce.DAY) -> None:
        self.user = user
        self.symbol = symbol
        self.qty = qty
        self.time_in_force = time_in_force
        self.side = OrderSide.BUY

    
    def execute(self) -> str: 
        market_order_data = self.create_order(
            self.symbol,
            self.qty,
            "buy",
            type="market"
            )
        market_order = self.user.broker.submit_order(market_order_data)
        return "Order placed!"
    
    def menudescription(self) -> str:
        return "Buy a stock at the current market price."
