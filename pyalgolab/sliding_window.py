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


#https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-100-liked

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
        



        