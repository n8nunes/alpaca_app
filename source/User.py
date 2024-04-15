from alpaca.trading.client import TradingClient

class User:
    '''
    Handles the buying and selling actions in manual mode.
    The user can specify which stocks to buy/sell.
    '''
    def __init__(self, api_key: str, secret_key: str, paper: bool) -> None:
        self.trading_client = TradingClient(api_key, secret_key, paper)
        self.account = self.trading_client.get_account()
    
    def get_trading_client(self) -> TradingClient:
        return self.trading_client