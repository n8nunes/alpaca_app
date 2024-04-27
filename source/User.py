from alpaca.trading.client import TradingClient
from lumibot.brokers import Alpaca
from lumibot.backtesting import yahoo_backtesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import trader
from datetime import datetime

class User:
    '''
    Handles the buying and selling actions in manual mode.
    The user can specify which stocks to buy/sell.
    '''
    def __init__(self, api_key: str, secret_key: str, base_url: str, paper: bool=True) -> None:
        alpaca_creds = {
            "API_KEY": api_key,
            "API_SECRET": secret_key,
            "PAPER": paper
        }
        self.broker = Alpaca(alpaca_creds)
    
    def get_broker(self) -> TradingClient:
        return self.broker