# pyalgolab/heap.py
"""
MinHeap Data Structure
"""

class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i): return (i - 1) // 2
    def _left(self, i): return 2 * i + 1
    def _right(self, i): return 2 * i + 2

    def _swap(self, i, j): self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0 and self.heap[i] < self.heap[self._parent(i)]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def extract_min(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        min_val = self.heap[0]
        self._swap(0, -1)
        self.heap.pop()
        self._heapify(0)
        return min_val

    def _heapify(self, i):
        smallest = i
        left, right = self._left(i), self._right(i)
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self._swap(i, smallest)
            self._heapify(smallest)
