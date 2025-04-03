# tests/test_union_find.py

from pyalgolab.union_find import UnionFind

def test_union_find():
    uf = UnionFind(5)
    uf.union(0,1)
    uf.union(1,2)
    assert uf.find(0) == uf.find(2)
    assert uf.find(3) != uf.find(0)

