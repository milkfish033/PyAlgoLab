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


#--------------------------------------------------------------------------------------------------------------
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


#https://leetcode.cn/problems/search-insert-position/submissions/667086210/
#O(logn)
#O(1)
#对于这道题，注意对题目要求的转化，和插入目标数值之后每个元素index的变化
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def b(t):
            left, right = -1, len(nums)
            while left + 1 < right:
                mid = (right + left)//2
                if nums[mid] < t:
                    left = mid
                else:
                    right = mid
            return right 
        
        ans = b(target)
        return ans 

#https://leetcode.cn/problems/binary-search/description/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)
        while left + 1 < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid
            else:
                right = mid 
        if right == len(nums) or nums[right] != target:
            return -1
        else:
            return right 