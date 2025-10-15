#https://leetcode.cn/problems/number-of-islands/description/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #run DFS for each [1], everytime when encounter a new[1]
        #size of islands += 1
        #O(mn) where m = len(grid) and n = len(grid[0])
        #O(mn) since recursion itself uses a stack 
        
        def dfs(i, j):
            if i >= len(grid) or i <0 or j >= len(grid[0]) or j < 0 or grid[i][j] != '1':
                return 
            grid[i][j] = '2'
            dfs(i + 1, j) 
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        ans = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    dfs(x, y)
                    ans += 1
        return ans 



#https://leetcode.cn/problems/max-area-of-island/description/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0 
        def dfs(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] != 1:
                return 0
            size = 1
            grid[i][j] = 2
            size += dfs(i+1, j)
            size += dfs(i-1, j)
            size += dfs(i, j+1)
            size += dfs(i, j-1)
            return size 
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    ans = max(ans, dfs(x, y))
        return ans

#https://leetcode.cn/problems/count-islands-with-total-value-divisible-by-k/
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        def dfs(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] == 0:
                return 0
            size = grid[i][j]
            grid[i][j] = 0 #更新遍历过的元素，否则计算重复
            size += dfs(i+1, j)
            size += dfs(i-1, j)
            size += dfs(i, j+1)
            size += dfs(i, j-1)
            return size 
        
        ans = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] != 0:
                    if dfs(x, y) % k == 0:
                        ans += 1
        return ans 

#https://leetcode.cn/problems/pond-sizes-lcci/description/
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        
        def dfs(i, j):
            if i >= len(land) or i < 0 or j >= len(land[0]) or j < 0 or land[i][j] != 0:
                return 0
            land[i][j] = 9 #mark as visited
            area = 1
            area += dfs(i-1, j)
            area += dfs(i+1, j)
            area += dfs(i, j-1)
            area += dfs(i, j+1)

            area += dfs(i-1, j-1)
            area += dfs(i-1, j+1)
            area += dfs(i+1, j-1)
            area += dfs(i+1, j+1)
            return area

        ans = []
        for x in range(len(land)):
            for y in range(len(land[0])):
                if land[x][y] == 0:
                    ans.append(dfs(x,y))
        ans.sort()
        return ans
            

        