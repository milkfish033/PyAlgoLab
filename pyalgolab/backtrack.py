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
