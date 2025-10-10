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

                    

        