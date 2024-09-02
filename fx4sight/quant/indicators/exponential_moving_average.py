import numpy as np

class ExponentialMovingAverage():
    def __init__(self, period: int = 14) -> None:
        '''
        A type of moving average that places a greater weight and significance 
        on the most recent data points. The EMA reacts more significantly to 
        recent price changes than a simple moving average (SMA), which applies 
        an equal weight to all observations in the period.
        Generally, the 12 and 26-day EMAs are considered the most common
        short-term averages, and the 50 and 200-day EMAs are considered the
        most common long-term averages. When the shorter-term EMA crosses above
        the longer-term EMA, it is generally considered a bullish signal,
        but due to the lagging nature of the EMA, the signal may come late.
        When the 200-day EMA is crossed, it is a signal that a reversal is
        has occurred.
        
        Args:
            period (int): Number of periods (recent price bars) to consider
                when calculating the EMA. Defaults to 14.
        '''
        self.period = period
        self.prices = []
        self.ema = None
        self.ema_prev = None
        self.multiplier = 2 / (self.period + 1)
        self.history = np.array([])

    def update(self, price: float) -> float:
        '''
        Updates the EMA with the latest price.
        Ensure that the price's timestamp is
        of the same granularity as the period.
        
        Args:
            price (float): Latest price.
        Returns:
            Current EMA value (float). If there are not
            at least `period` prices, the EMA will be NaN.
        '''
        self.prices.append(price)
        
        if len(self.prices) >= self.period:
            if self.ema_prev == None:
                self.ema = np.mean(self.prices[-self.period:]) / self.period
            else:
                self.ema = price * self.multiplier + self.ema_prev * (1 - self.multiplier)
            self.ema_prev = self.ema
            self.history = np.append(self.history, self.ema)
        return self.ema
    
    def get(self) -> float:
        '''
        Returns:
            The current EMA value (float). If there are not
            at least `period` prices, the EMA will be NaN.
        '''
        return self.ema
    
    def get_history(self) -> np.array:
        '''
        Returns:
            All stored EMA values (np.array).
        '''
        return self.history