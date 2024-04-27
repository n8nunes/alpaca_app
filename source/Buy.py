from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from Action import Action
from User import User
from abc import ABC, abstractmethod


class Buy(Action, ABC):
    def __init__(self, user: User, symbol: str, qty: float, time_in_force: TimeInForce):
        self.user = user
        self.symbol = symbol
        self.qty = qty
        self.time_in_force = time_in_force
        self.side = OrderSide.BUY
        self.trading_client = self.user.get_trading_client()
    
    @abstractmethod
    def execute(self, user: User) -> str: 
        # create an order object
        # pass the order object into trading_client.submit_order()
        pass
    
    @abstractmethod
    def menudescription(self) -> str:
        pass