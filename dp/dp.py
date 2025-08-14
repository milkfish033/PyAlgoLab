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