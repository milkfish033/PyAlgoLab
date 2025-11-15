# 1. Length Fixed

## Template :

https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

```
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
```

## Harder