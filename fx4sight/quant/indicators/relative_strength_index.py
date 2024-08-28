import numpy as np

class RelativeStrengthIndex():
    def __init__(self, period: int = 14) -> None:
        '''
        Momentum oscillator that measures the speed and magnitude of 
        changes in price movements. RSI oscillates between 0 and 100.
        Typically, a value above 70 indicates overbought conditions 
        and a value below 30 indicates oversold conditions.

        Args:
            period (int): Number of periods (recent price bars) to consider
                when calculating the RSI. Defaults to 14.
        '''
        self.period = period
        self.prices = []
        self.gains = []
        self.losses = []
        self.avg_gain = 0.0
        self.avg_loss = 0.0
        self.rsi = 0.0
    
    def update(self, price: float) -> float:
        '''
        Updates the RSI with the latest price.
        Ensure that the price's timestamp is
        of the same granularity as the period.
        
        Args:
            price (float): Latest price.
        '''
        self.prices.append(price)

        if len(self.prices) > 1:
            change = self.prices[-1] - self.prices[-2]
            
            if change > 0:
                self.gains.append(change)
                self.losses.append(0)
            else:
                self.gains.append(0)
                self.losses.append(-change)
        
        if len(self.prices) > self.period:
            if len(self.prices) == self.period + 1:
                self.avg_gain = np.mean(self.gains)
                self.avg_loss = np.mean(self.losses)
            else:
                self.avg_gain = ((self.avg_gain * (self.period - 1)) + self.gains[-1]) / self.period
                self.avg_loss = ((self.avg_loss * (self.period - 1)) + self.losses[-1]) / self.period
            rs = self.avg_gain / self.avg_loss
            self.rsi = 100 - (100 / (1 + rs))
        return self.rsi

    def get(self) -> float:
        '''
        Returns the current RSI value (float).

        If not updated with at least `period` prices, 
        the RSI will be 0.0.
        '''
        return self.rsi