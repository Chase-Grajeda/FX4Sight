import numpy as np


class HammerSignal:
    def __init__(self, bull: bool = True, inverse: bool = False) -> None:
        """Candlestick pattern that occurs when the wick is long with a short
        upper body. This is usually a reversal signal found at the bottom of
        downtrends. The bearish version is often referred to as the hanging
        man, and shooting star for the inverse.

        Args:
            bull (bool, optional): Desired sentiment to return. Setting to
                `False` would look for bearish hammer signals.
                Defaults to `True`.
            inverse (bool, optional): Searches for the inverted pattern if set
                to `True`. Defaults to `False`.
        """
        self.bull = bull
        self.inverse = inverse
