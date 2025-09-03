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

#https://leetcode.cn/problems/perfect-squares/?envType=study-plan-v2&envId=top-100-liked

#isqrt(10) --> 3
#1: 对于这种多次调用的情况，把dfs定义在顶层可以节省内存
#2: 对于求最小值问题，需要考虑是否需要定义一个最大值inf来表示不可能完成的情况，避免无限循环
from math import inf, isqrt
@cache 
def dfs(i, j):
    if j == 0:
        return 0
    #如果i=0，会一直循环，所以定义一个最大值用来规避这条路径
    elif i == 0:
        return float("inf")
    elif j >= i**2: 
        return min(dfs(i-1, j), 1+ dfs(i, j-i**2))
    else:
        return dfs(i-1, j)
class Solution:
    def numSquares(self, n: int) -> int:
        return dfs(isqrt(n),n)

##类似的-->下一题
#https://leetcode.cn/problems/coin-change/submissions/654325063/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        @cache
        def dfs(i, j):
            #i --> index, j--> rest
            if i < 0:
                return 0 if j == 0 else inf 
            
            if coins[i] > j:
                return dfs(i-1, j)
            
            else:
                return min(dfs(i-1, j), 1 + dfs(i, j - coins[i]))
        
        ans = dfs(n-1, amount) 
        
        return ans if ans < inf else -1
    

#https://leetcode.cn/problems/partition-equal-subset-sum/?envType=study-plan-v2&envId=top-100-liked
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)

        # 如果总和为奇数，不可能分成两个相等的子集
        if total % 2 != 0:
            return False
        
        target = total // 2  # 目标是找到一个子集和为 total//2

        @cache
        def dfs(i, curr):
            # 如果找到目标子集和，返回 True
            if curr == target:
                return True
            # 如果超出范围或当前和超过 target，就不行
            if i >= n or curr > target:
                return False
            
            # 两个选择：选当前元素 或 不选
            return dfs(i+1, curr + nums[i]) or dfs(i+1, curr)

        return dfs(0, 0)

#https://leetcode.cn/problems/word-break/submissions/659300156/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # 提高查询效率
        n = len(s)

        @cache
        def dfs(i: int) -> bool:
            # 如果走到结尾，说明可以拼出来
            if i == n:
                return True
            # 尝试 s[i:j] 是否在字典中
            for j in range(i + 1, n + 1):
                if s[i:j] in wordSet and dfs(j):
                    return True
            return False

        return dfs(0)


        