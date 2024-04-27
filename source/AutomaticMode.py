from lumibot.strategies.strategy import Strategy
from lumibot.backtesting import yahoo_backtesting
from User import User
from datetime import datetime
from MarketBuy import MarketBuy
from Buy import Buy

user = User("PKXZ0MLECCNOT6EWNEAS", "aoJJ75KGbyF2BJZ9bnaudnoZRLxuE8M8x2sqttnN", True)
class MLTrader(Strategy):
    def initialize(self, symbol: str = "SPY"):
        self.symbol = symbol
        self.sleeptime = "24H"
        self.last_trade = None

    def on_trading_iteration(self):
        if self.last_trade == None:
            marketBuy = MarketBuy(user=user, symbol="SPY", qty=10)
            marketBuy.execute()
            self.last_trade = "buy"
            

start_date = datetime(2023,12,15)
end_date = datetime(2023,12,31)

user = User("PKXZ0MLECCNOT6EWNEAS", "aoJJ75KGbyF2BJZ9bnaudnoZRLxuE8M8x2sqttnN", True)

broker = user.get_broker()
strategy = MLTrader(name = 'mlstrat', broker = broker,
                    parameters={"symbol": "SPY"})
strategy.backtest(
    yahoo_backtesting.YahooDataBacktesting,
    start_date,
    end_date,
    parameters={"symbol": "SPY"}
)

