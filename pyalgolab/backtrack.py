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
