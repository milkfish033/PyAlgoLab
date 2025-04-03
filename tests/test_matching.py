# tests/test_matching.py

from pyalgolab import matching

def test_gale_shapley():
    P = [[0,1], [0,1]]
    A = [[0,1], [0,1]]
    res = matching.gale_shapley([p.copy() for p in P], A)
    assert sorted(res) == [0,1]
