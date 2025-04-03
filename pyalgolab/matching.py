# pyalgolab/matching.py
"""
Gale-Shapley Stable Matching Algorithm
"""

from typing import List

def gale_shapley(P: List[List[int]], A: List[List[int]]):
    n = len(P)
    matches = [None] * n
    engaged = [False] * n
    all_matched = False

    while not all_matched:
        all_matched = True
        for i in range(n):
            if engaged[i]:
                continue
            all_matched = False
            next_pref = P[i].pop()
            if matches[next_pref] is None:
                matches[next_pref] = i
                engaged[i] = True
            else:
                current = matches[next_pref]
                if A[next_pref].index(i) < A[next_pref].index(current):
                    matches[next_pref] = i
                    engaged[i] = True
                    engaged[current] = False
    return matches
