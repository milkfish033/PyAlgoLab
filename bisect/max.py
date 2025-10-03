#求最小
# if check: left = mid
# else: right = mid 
# note: how to initialize left, right 
# right: illegal 
# left: legal
# return left 哪个合法return哪个

#https://leetcode.cn/problems/h-index-ii/description/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n+1
        while left + 1 < right:
            mid = (left + right) // 2
            if citations[n-mid] >= mid: 
                left = mid
            else:
                right = mid
        return left
    
#https://leetcode.cn/problems/maximum-candies-allocated-to-k-children/description/
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 0, min(max(candies)+1, sum(candies)//k+1)
        while left + 1 < right:
            mid = (left + right)//2
            if sum(x//mid for x in candies) >= k:
                left = mid 
            else:
                right = mid
        return left 
            
    


