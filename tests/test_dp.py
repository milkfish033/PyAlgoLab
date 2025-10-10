# tests/test_dp.py

from dp import dp_basic

def test_fib():
    assert dp_basic.fib(10) == 55

def test_knapsack():
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    assert dp_basic.knapsack(values, weights, capacity) == 220
