#https://leetcode.cn/problems/daily-temperatures/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        l = len(temperatures)
        res = [0] * l
        for i in range(l):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res

