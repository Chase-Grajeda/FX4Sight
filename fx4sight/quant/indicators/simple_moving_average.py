import numpy as np

class SimpleMovingAverage():
    def __init__(self, period: int = 14) -> None:
        '''
        The average of the closing prices over a specified number of periods.
        The SMA is a lagging indicator that smooths price data to identify
        trends. When a shorter-term SMA crosses above a longer-term SMA, it
        is generally considered a bullish signal (golden cross). 
        Conversely, when a shorter-term SMA crosses below a longer-term SMA, 
        it is generally considered a bearish signal (death cross).
        
        Args:
            period (int): Number of periods (recent price bars) to consider
                when calculating the SMA. Defaults to 14.
        '''
        self.period = period
        self.prices = []
        self.sma = None
        self.history = np.array([])

    def update(self, price: float) -> float:
        '''
        Updates the SMA with the latest price.
        Ensure that the price's timestamp is
        of the same granularity as the period.
        
        Args:
            price (float): Latest price.
        Returns:
            Current SMA value (float). If there are not
            at least `period` prices, the SMA will be NaN.
        '''
        self.prices.append(price)
        
        if len(self.prices) >= self.period:
            self.sma = np.mean(self.prices[-self.period:])
            self.history = np.append(self.history, self.sma)
        return self.sma
    
    def get(self) -> float:
        '''
        Returns:
            The current SMA value (float). If not updated
            with at least `period` prices, the SMA will be NaN.
        '''
        return self.sma
    
    def get_history(self) -> np.array:
        '''
        Returns:
            All stored SMA values (np.array).
        '''
        return self.history