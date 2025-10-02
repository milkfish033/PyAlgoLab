# pyalgolab/dp.py
"""
Dynamic Programming Algorithms
"""

def fib(n: int):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def weighted_interval_scheduling(intervals):
    intervals.sort(key=lambda x: x[1])
    n = len(intervals)
    M = [0] * (n + 1)

    def latest_non_conflict(i):
        for j in range(i - 1, -1, -1):
            if intervals[j][1] <= intervals[i][0]:
                return j
        return -1

    for i in range(1, n + 1):
        incl = intervals[i - 1][2]
        lnc = latest_non_conflict(i - 1)
        if lnc != -1:
            incl += M[lnc + 1]
        M[i] = max(incl, M[i - 1])
    return M[n]

def subset_sum(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][target]

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]
