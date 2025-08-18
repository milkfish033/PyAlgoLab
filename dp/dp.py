from functools import cache

#https://leetcode.cn/problems/climbing-stairs/?envType=study-plan-v2&envId=top-100-liked

#note we can replace this res list by using decorator #cache in python 
class Solution:
    def climbStairs(self, n: int) -> int:
        res = [-1] * n
        #@cache
        def dp(x):
            if x <= 1:
                return 1
            elif res[x-1] != -1:
                return res[x-1]
            else:
                cur =  dp(x-1) + dp(x-2)
                res[x-1] = cur
                return cur 
        return dp(n)
    
#https://leetcode.cn/problems/house-robber/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def rob(self, nums) -> int:
        i = len(nums)
        @cache 
        def dp(x):
            if x <0:
                return 0
            res = max(dp(x-1), dp(x-2) + nums[x])
            return res 
        return dp(i-1)
    

#Pascal's Triangle
#https://leetcode.cn/problems/pascals-triangle/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def generate(self, numRows: int):
        c = [[1]* (m+1) for m in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                c[i][j] = c[i-1][j] + c[i-1][j-1] #understand this as how many ways can we pick j items from i items
        return c


#https://leetcode.cn/problems/longest-increasing-subsequence/?envType=study-plan-v2&envId=top-100-liked

#bisect 用于快速进行二分查找的一个包
import bisect
from typing import List

#这里的核心思想是贪心+二分查找
#proof of greedy algorithm: 同等长度下，将原先的数字替换为一个更小的数字可以增加后续延长序列的可能性
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            #bisect_left >= ; bisect_right >
            i = bisect.bisect_left(sub, x) 
            if i == len(sub):
                sub.append(x)
            else:
                sub[i] = x
        return len(sub)
