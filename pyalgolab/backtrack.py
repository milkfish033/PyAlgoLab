##template for backtrack

def backtrack(path, choice):
    if valid:
        result.append(path.copy())
        return 
        
    for c in choice:
        if not valid(c):
            continue
        path.append(c)
        backtrack(path, choice)
        path.pop() #backtrack



#example usage 
#https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-100-liked
from collections import defaultdict

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        code = defaultdict(str)
        code["2"] = ("a", "b", "c")
        code["3"] = ("d", "e", "f")
        code["4"] = ("g", "h", "i")
        code["5"] = ("j", "k", "l")  
        code["6"] = ("m", "n", "o")
        code["7"] = ("p", "q", "r", "s")
        code["8"] = ("t", "u", "v")
        code["9"] = ("w", "x", "y", "z")

        # Validate input digits
        for d in digits:
            if int(d) > 9 or int(d) < 2:
                return []
        
        # Create a list of choices for each digit position
        choices = [code[d] for d in digits]
        result = []
        
        def backtrack(index, path):
            if index == len(digits):
                result.append(path)
                return
            
            for c in choices[index]:
                backtrack(index + 1, path + c)
        
        backtrack(0, "")
        return result


#https://leetcode.cn/problems/combination-sum/?envType=study-plan-v2&envId=top-100-liked
#输入
#candidates =[2,3,6,7]
#target =7
#输出
#[[2,2,3],[7]]

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        check = []
        #backtrack recursive function
        def dfs(path):
            if sum(path) == target:
                ccopy = sorted(path)
                if ccopy not in check:
                    check.append(ccopy.copy())
                    result.append(path.copy())
                    return 
            
            for c in candidates:
                if sum(path) + c > target:
                    continue 
                
                path.append(c)
                dfs(path)
                path.pop()
        dfs([])
        return result


#https://leetcode.cn/problems/generate-parentheses/solutions/?envType=study-plan-v2&envId=top-100-liked
#backtrack & dynamic programming
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l, r = n , n
        result = []
        def backtrack(path, i, j):
            if len(path) == 2*n:
                result.append(path)
                return

            if i == 0:
                backtrack(path + ")", i, j-1)

            elif j == i:
                backtrack(path + "(", i-1, j)
            
            else:
                backtrack(path + "(", i-1, j)
                backtrack(path + ")", i, j-1)

                
        backtrack("",l, r)
        return result

#https://leetcode.cn/problems/word-search/submissions/643044860/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, i):
            if i == len(word): return True
            if x >= len(board) or y >= len(board[0]) or x < 0 or y < 0 or board[x][y] != word[i]:
                return False 

            else:
                temp = board[x][y]
                board[x][y] = '#'
                found = dfs(x+1, y, i+1) or dfs(x-1, y, i+1) or dfs(x, y+1, i+1) or dfs(x, y-1, i+1)                 
                board[x][y] = temp
                return found 
            
        for m in range(len(board)):
            for n in range(len(board[0])):
                if dfs(m, n, 0): return True
        return False 



#https://leetcode.cn/problems/palindrome-partitioning/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        # 考虑 s[i:] 怎么分割
        def dfs(i: int) -> None:
            if i == n:  # s 分割完毕
                ans.append(path.copy())  # 复制 path
                return
            for j in range(i, n):  # 枚举子串的结束位置
                t = s[i: j + 1]  # 分割出子串 t
                if t == t[::-1]:  # 判断 t 是不是回文串
                    path.append(t)
                    # 考虑剩余的 s[j+1:] 怎么分割
                    dfs(j + 1)
                    path.pop()  # 恢复现场

        dfs(0)
        return ans

