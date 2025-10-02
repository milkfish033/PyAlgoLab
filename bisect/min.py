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


#https://leetcode.cn/problems/minimum-time-to-complete-trips/description/
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = min(time) - 1
        right = min(time) * totalTrips
        # left, right = 0, totalTrips*max(time)
        while left + 1 < right:
            mid = (left + right) // 2 
            if sum(mid//x for x in time) >= totalTrips:
                right = mid 
            else:
                left = mid 
        return right 