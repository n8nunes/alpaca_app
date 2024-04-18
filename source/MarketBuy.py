from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from Buy import Buy
from User import User

class MarketBuy(Buy):
    def __init__(self) -> None:
        return super().__init__

    
    def execute(self, user: User) -> str: 
        market_order_data = MarketOrderRequest(
            symbol=self.symbol, 
            qty=self.qty,
            side=self.side, 
            time_in_force=self.time_in_force
            )
        market_order = self.trading_client.submit_order(market_order_data)
        return "Order placed!"
    
    def menudescription(self) -> str:
        return "Buy a stock at the current market price."
