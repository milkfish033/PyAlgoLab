#求最小
# if check: right = mid
# else: left = mid 
# note: how to initialize left, right 
#right: legal 
#left: illegal


#example 
#https://leetcode.cn/problems/find-the-smallest-divisor-given-a-threshold/description/
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 0, max(nums)  
        while left + 1 < right:
            mid = (left + right) // 2 
            #note here  //mid should be included in sum() since we are using //
            if sum ((x-1) // mid for x in nums ) <= threshold - len(nums): #上取整公式推导 
                right = mid 
            else:
                left = mid 
        return right 
