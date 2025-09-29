#template
# Binary Search
def binary_search(arr, target): #return the ***first*** position of first number which is bigger or equal to target
    #开区间写法 （）
    left, right = -1, len(arr)
    while left + 1 < right:  
        mid = (left + right) // 2
        if arr[mid] < target: #the order here matters !!!
            left = mid 
        else:
            right = mid 
    return right if right < len(arr) else -1

# >  : (>= x + 1) 
# <  : (>=x) - 1
# <= : (>x) - 1

#https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/666881976/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def b(t):
            left, right = -1, len(nums)
            while left + 1 < right:
                mid = (left + right) // 2 
                if nums[mid] < t:
                    left = mid
                else:
                    right = mid 
            return right 
        start = b(target)
        if start == len(nums) or nums[start] != target:
        #整个数组的数都<target或者找到了>target的数
            return [-1, -1]
        end = b(target+1) - 1 # > target左边的第一个数
        return [start, end]

