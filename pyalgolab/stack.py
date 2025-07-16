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

#https://leetcode.cn/problems/next-greater-element-i/solutions/1065517/xia-yi-ge-geng-da-yuan-su-i-by-leetcode-bfcoj/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            res[num] = stack[-1] if stack else -1
            stack.append(num)
        return [res[num] for num in nums1]
