""" Helpers to (i) compute position-weighted Greeks,
(ii) explain daily P&L via delta * dS.
"""

import pandas as pd
from pricing import black_scholes_price, greeks

def portfolio_greeks(df, S, r):
    """
    Compute portfolio Greeks for a dataframe of positions.

    df columns expected: K, T, sigma, qty, option_type
    """
    greeks_dict = {"delta": [], "gamma": [], "vega": [], "theta": []}
    for _, row in df.iterrows():
        g = greeks(S, row.K, row.T, r, row.sigma)
        for k in greeks_dict:
            greeks_dict[k].append(g[k] * row.qty)
    return {k: sum(v) for k, v in greeks_dict.items()}


def pnl_by_delta(df, S_today, S_yday, r):
    """
    First-order P&L attribution: Δ·dS for entire portfolio.
    """
    dS = S_today - S_yday
    deltas = []
    for _, row in df.iterrows():
        d = greeks(S_yday, row.K, row.T, r, row.sigma)["delta"]
        deltas.append(d * row.qty)
    return sum(deltas) * dS