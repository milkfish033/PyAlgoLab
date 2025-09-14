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


        