# tests/test_dp.py

from pyalgolab import dp

def test_fib():
    assert dp.fib(10) == 55

def test_knapsack():
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    assert dp.knapsack(values, weights, capacity) == 220
