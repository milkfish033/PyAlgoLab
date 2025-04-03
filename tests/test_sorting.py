# tests/test_sorting.py

from pyalgolab import sorting

def test_bubble_sort():
    arr = [5, 1, 4, 2, 8]
    sorting.bubble_sort(arr)
    assert arr == [1, 2, 4, 5, 8]

def test_insertion_sort():
    arr = [9, 7, 5, 3]
    sorting.insertion_sort(arr)
    assert arr == [3, 5, 7, 9]

def test_selection_sort():
    arr = [3, 1, 2]
    sorting.selection_sort(arr)
    assert arr == [1, 2, 3]
