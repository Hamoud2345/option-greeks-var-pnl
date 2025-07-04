from pricing import black_scholes_price

def test_put_call_parity():
    S, K, T, r, sigma = 100, 100, 0.5, 0.02, 0.25
    call = black_scholes_price(S, K, T, r, sigma, "call")
    lhs = call - (black_scholes_price(S, K, T, r, sigma, "put"))
    rhs = S - K * pow(2.718281828, -r * T)
    assert abs(lhs - rhs) < 1e-6