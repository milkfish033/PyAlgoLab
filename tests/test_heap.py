# tests/test_heap.py

from pyalgolab.heap import MinHeap

def test_heap():
    h = MinHeap()
    for val in [5, 3, 7, 1]:
        h.insert(val)
    assert h.extract_min() == 1
