"""
var.py
-------
Historical Value-at-Risk (1-sided).
"""

import numpy as np
import pandas as pd

def historical_var(pnl_series: pd.Series, alpha: float = 0.99):
    
    if not 0 < alpha < 1:
        raise ValueError("alpha must be in (0,1)")
    return -np.quantile(pnl_series.dropna(), 1 - alpha)