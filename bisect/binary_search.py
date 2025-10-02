import bisect
# bisect_left(arr, x) --> return the first position which is >= x
# bisect_right(arr, x) --> return the first position which is > x 


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
        
#https://leetcode.cn/problems/find-smallest-letter-greater-than-target/description/
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def b(t):
            left, right = -1, len(letters)
            while left + 1 < right:
                mid = (right + left) // 2
                if letters[mid] < t:
                    left = mid
                else:
                    right = mid
            return right 
        ans = b( chr(ord(target)+1) )
        return letters[ans] if ans < len(letters) else letters[0]

#https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/description/
#O(logn)
#O(1)
class Solution:
    def lowerbound(self, target, arr):
        left, right = -1, len(arr)
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid 
            else:
                right = mid
        return right 
    def maximumCount(self, nums: List[int]) -> int:
        pos = self.lowerbound(1, nums)
        neg = self.lowerbound(0, nums) - 1 
        return max(neg+1, len(nums)-pos)
    
#https://leetcode.cn/problems/successful-pairs-of-spells-and-potions/submissions/
from bisect import bisect_left
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        return [m - bisect_left(potions, success / x) for x in spells]

#https://leetcode.cn/problems/find-the-distance-value-between-two-arrays/solutions/3010185/liang-chong-fang-fa-er-fen-cha-zhao-san-15u9b/
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for x in arr1:
            i = bisect_left(arr2, x - d)
            if i == len(arr2) or arr2[i] > x + d:
                ans += 1
        return ans


#https://leetcode.cn/problems/longest-subsequence-with-limited-sum/description/
#O(logn)
#O(1)
#前缀和+二分查找
from bisect import bisect_right
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        list.sort(nums)
        #构建前缀和for nums 
        s = 0
        for m, n in enumerate(nums):
            s += n
            nums[m] = s
        ans = [] 
        for i in queries:
            ans.append(bisect_right(nums, i))
        return ans 

#https://leetcode.cn/problems/compare-strings-by-frequency-of-the-smallest-character/
from typing import List
from bisect import bisect_right

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            return s.count(min(s))   # 字典序最小的字符出现频次
        # 先计算 words 的频次数组并排序
        words_freq = sorted(f(w) for w in words)
        ans = []
        for q in queries:
            fq = f(q)
            # 找到大于 f(q) 的数量
            ans.append(len(words_freq) - bisect_right(words_freq, fq))
        return ans


        
