#----------------------------------------------------------------------------------#
#困难题#
#https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/
from collections import defaultdict
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ans = s = 0
        cnt = defaultdict(int)
        for i, x in enumerate(nums):
            # 1. 进入窗口
            s += x
            cnt[x] += 1
            left = i - k + 1
            if left < 0:  # 窗口大小不足 k
                continue
            # 2. 更新答案
            if len(cnt) >= m:
                ans = max(ans, s)
            # 3. 离开窗口
            out = nums[left]
            s -= out
            cnt[out] -= 1
            if cnt[out] == 0: #注意这里需要去掉出现次数为0的数
                del cnt[out]
        return ans



#https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/description/
#运用转换的思想，找到题目中的滑动窗口，和求出的值
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = 0 
        first_sum = 0
        total = sum(cardPoints)
        n = len(cardPoints)
        if k == n:
            return total
        for right, x in enumerate(cardPoints):
            first_sum += x
            left = right + 1 - n + k 
            if left >= 0:
                ans = max(ans, total- first_sum)
                print(left)
                first_sum -= cardPoints[left]
        return ans

#https://leetcode.cn/problems/grumpy-bookstore-owner/description/
#T: O(n)
#S: O(1)
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        #实用技巧能挽留的最大值： 不满意--》满意
        cur = ans = 0 
        res = 0
        for right, x in enumerate (customers):
            if grumpy[right] == 1:
                cur += x
            left = right - minutes + 1
            if left >= 0:
                ans = max(cur, ans)
                if grumpy[left] == 1:
                    cur -= customers[left]
                    
        #不使用技巧的满意值
        for j, k in enumerate (customers):
            if grumpy[j] == 0:
                res += k
        return ans + res


#https://leetcode.cn/problems/shortest-and-lexicographically-smallest-beautiful-string/description/
#O(n^2)
#O(n)
class Solution:
    from collections import Counter
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        cnt = Counter()
        n = len(s)
        ans = n + 1   # 最短长度
        res = ""      # 记录答案
        left = 0 
        for right, x in enumerate(s):
            cnt[x] += 1
            while cnt['1'] >= k:     
                # 如果是合法的美丽子字符串
                if cnt['1'] == k:
                    length = right - left + 1
                    sub = s[left:right+1]
                    # 更新最短，或在同样长度下比较字典序
                    if length < ans or (length == ans and sub < res):
                        ans = length
                        res = sub
                cnt[s[left]] -= 1
                left += 1 

        return res




#https://leetcode.cn/problems/subarray-product-less-than-k/
#对于这种求子数组个数的题目，当内层循环[left, right]是合法的，[left+1, right], [left+2, right]....都合法
#所以往往最后修改为 ans+= right - left + 1
#越短越合法
#O(n)
#O(n)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = left = 0 
        cur = 1 #因为是乘法，初始值为1 
        if k <= 1:#对于这种情况特殊判定：题目提示1<=nums[i]<=1000
            return 0
        for right, x in enumerate(nums):
            cur *= x
            while cur >= k:
                cur = cur/(nums[left])
                left += 1
            ans += right - left + 1
        return ans
        

#越长越合法
#对于这类题型， 首先找到刚好满足临界值的left，right， 即【left，right】不合法
#对于[left-1, right], [left-2, right]...都是合法的
#ans += left
#https://leetcode.cn/problems/number-of-substrings-containing-all-three-characters/submissions/665537461/
#O(n)
#O(1)
class Solution:
    from collections import Counter
    def numberOfSubstrings(self, s: str) -> int:
        cnt = Counter()
        left = ans = 0 
        for right, x in enumerate(s):
            cnt[x] += 1
            while len(cnt) == 3:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
            ans += left 
        return ans 
                

#---------------------------------------------------------------------------------------------#



#https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
#时间复杂度：O(n)
#空间复杂度 O(1)
#要点：从右边开始枚举，注意什么时候窗口开始出现，每次维护窗口时需要注意是否需要更新cur
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans, cur = 0, 0
        for right, i in enumerate(s):
            if i in 'aeiou':
                cur += 1

            left = right - k + 1
            if left < 0 :#没有形成窗口
                continue 

            ans = max(ans, cur)
            if ans == k: #优化：如果已经达到k，可以提前退出
                break 
                
            if s[left] in 'aeiou':
                cur -= 1

        return ans

#https://leetcode.cn/problems/maximum-average-subarray-i/
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans, cur = float('-inf'), 0
        for right, x in enumerate(nums):
            cur += x 
            left = right - k + 1

            if left >= 0: #注意题目要求，在窗口没有形成之前，不用计算平均值，否则会用错误的均值进行比较
                avg = cur / k
                ans = max(avg, ans)
                cur -= nums[left]
        return ans

#https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left, ans = 0, n
        for right, x in enumerate(nums):
            while x > k*nums[left]:
                left += 1
            ans = min(ans, n- (right - left + 1))
        return ans 

#prompt1: 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 
        ans = []
        det = True

        for i in range(len(s)):
            if i == len(s)-1 and s[i] not in ans:
                return max(res, len(ans)+1)
            if s[i] not in ans:
                ans.append(s[i])
            else:
                #每次遇到重复的元素，记录当前子串长度，同时更新滑动窗口
                cur = ans.index(s[i])
                res = max(res, len(ans))
                ans = ans[cur+1:]
                print(i, ans)
                ans.append(s[i])

        return res


#prompt2: 
#时间复杂度 O(n)
#空间复杂度 O(1) : at most 128 cuz s consists of ASCII 
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0 
        left = 0
        cnt = Counter()

        for right, x in enumerate(s): 
            cnt[x] += 1
            while cnt[x] > 1: #持续删除左边的元素直到字串里没有重复元素
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            
        return ans 

#https://leetcode.cn/problems/find-all-anagrams-in-a-string/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        temp = sorted(p)
        n = len(p)
        res = []
        i = 0
        while i < len(s)-n+1:
            #i左标， i+n-1为右标
            cur = s[i:i+n]
            if sorted(cur) == temp:
                res.append(i)
                i += 1
            else:
                i += 1
        return res 
        
#https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/submissions/663075119/
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        tar = k*threshold
        ans = 0
        cur = 0
        for right, x in enumerate(arr):
            cur += x
            if cur >= tar and right >= k-1:
                print(right, cur )
                ans += 1
            
            left = right -k + 1
            if left >=0:
                cur -= arr[left]

        return ans 
                
#https://leetcode.cn/problems/k-radius-subarray-averages/
#时间 O(n)
#空间 O(n)
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans  = []
        if n - 1>= 2*k:
            cur = sum(nums[0: 2*k])
        if n - 1 < 2*k:
            return [-1] * n
        if k == 0:
            return nums

        for mid, x in enumerate(nums):
            if mid < k or mid >= n - k:
                ans.append(-1)
            else:
                left, right = mid - k, mid + k
                cur += nums[right]
                print(left, right, cur )
                
                ans.append(cur // (2*k+1))
                cur -= nums[left]

        return ans 
            

#https://leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks/submissions/663099637/
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # == 给定一个长度为k的字串，求W的最小数值
        ans, cur = inf, 0
        for right, x in enumerate(blocks):
            if x == 'W':
                cur += 1
            
            left = right - k + 1
            if left < 0:
                continue 
            
            ans = min(ans, cur)
            if ans == 0:
                break 
            if blocks[left] == 'W':
                cur -= 1
        return ans 
    
#https://leetcode.cn/problems/maximum-sum-of-distinct-subarrays-with-length-k/submissions/663453844/
from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cur = ans = 0
        cnt = defaultdict(int)
        for right, x in enumerate(nums):
            cur += x
            cnt[x] += 1
            left = right - k + 1
            if left < 0:
                continue
            if len(cnt) == k:
                ans = max( cur, ans)
            past = nums[left]
            cur -= past
            cnt[past] -= 1
            if cnt[past] == 0:
                del cnt[past]
        return ans 

#https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/submissions/664090547/
#T:O(n) 注意这里的时间复杂度是O（n）因为：left从左往右增加，最多移动len（s）次，不会每次循环都从头开始
#S:O(1) 
class Solution:
    from collections import Counter
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = Counter()
        left = ans = 0
        for right, x in enumerate(s):
            cnt[x] += 1
            while cnt[x] > 2:
                cnt[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans 

#https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/submissions/664146122/
#T: O(n)
#S : O(1)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = cnt0 = left = 0
        for right, x in enumerate(nums):
            cnt0 += 1 - x  # 维护窗口中的 0 的个数
            while cnt0 > 1: 
                cnt0 -= 1 - nums[left]  
                left += 1
            #注意这里每次更新答案都是窗口内只有1个0的情况
            ans = max(ans, right - left)
        return ans


#https://leetcode.cn/problems/get-equal-substrings-within-budget/
#T: O(n)
#S: O(k) or O(1)
class Solution:
    from collections import defaultdict
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = defaultdict(int)
        for i in range(len(s)):
            diff[i] = abs(ord(s[i]) - ord(t[i]))
        ans = cur = 0 
        left = 0 
        for right, x in enumerate(s):
            cur += diff[right]
            while cur > maxCost:
                cur -= diff[left]
                left += 1
            ans = max(ans, right - left + 1) 
        return ans 
        
#https://leetcode.cn/problems/fruit-into-baskets/submissions/664819863/
class Solution:
    from collections import Counter
    def totalFruit(self, fruits: List[int]) -> int:
        #==求最多含有两种不同元素的字串的最大长度
        cnt = Counter()
        ans = left = 0
        for right, x in enumerate(fruits):
            cnt[x] += 1
            while len(cnt) > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    del cnt[fruits[left]]
                left += 1
            ans = max(right - left + 1, ans)
        return ans 

#https://leetcode.cn/problems/minimum-size-subarray-sum/
#O(n)
#O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur = left = 0
        ans = inf
        for right, x in enumerate(nums):
            cur += x
            while cur >= target:
                ans = min(right - left + 1, ans)
                cur -= nums[left]
                left += 1
        return ans if ans != inf else 0 

        
#https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-i/description/
class Solution:
    from collections import Counter
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        cnt = Counter()
        ans = left = 0 
        for right, x in enumerate(s):
            cnt[x] += 1
            while cnt['0'] > k and cnt['1'] > k:
                cnt[s[left]] -= 1
                left += 1
            ans += right - left + 1
        return ans 

#https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/s
class Solution:
    from collections import Counter
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cnt_t = 0 #注意当题目只关注单一元素时，可以用一个计数器来代替哈希表
        target = max(nums)
        ans = left = 0 
        for right, x in enumerate(nums):
            if x == target:
                cnt_t += 1
            while cnt_t == k: #只关注单一元素的出现次数
                if nums[left] == target:
                    cnt_t -= 1
                left += 1
            ans += left 
        return ans


#https://leetcode.cn/problems/count-substrings-with-k-frequency-characters-i/description/
class Solution:
    from collections import Counter
    def numberOfSubstrings(self, s: str, k: int) -> int:
        cnt = Counter()
        ans = left = 0 
        for _, x in enumerate(s):
            cnt[x] += 1
            while cnt[x] == k:
                cnt[s[left]]-= 1
                left += 1
            ans += left
        return ans 

#https://leetcode.cn/problems/count-complete-subarrays-in-an-array/description/
class Solution:
    from collections import Counter
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uq = len(set(nums)) 
        left = ans = 0 
        cnt = Counter()
        for x in nums:
            cnt[x] += 1
            while len(cnt) >= uq:
                cur = nums[left]
                cnt[cur] -= 1
                if cnt[cur] == 0:
                    del cnt[cur]
                left += 1
            ans += left
        return ans