from .candle_signals.hammer_signal import HammerSignal
from .indicators.simple_moving_average import SimpleMovingAverage as SMA
from .indicators.exponential_moving_average import ExponentialMovingAverage as EMA
from .indicators.relative_strength_index import RelativeStrengthIndex as RSI

# Classes to be imported when using `from fx4sight.quant import *`.
__all__ = ['HammerSignal', 'SMA', 'EMA', 'RSI']

