#hard
#https://leetcode.cn/problems/YesdPw/description/
from typing import List

class Solution:
    def largestArea(self, grid: List[str]) -> int:
        # run dfs for each inner node 
        # when reaching the boundary --> fail
        # rest: +1
        self.ans = 0
        visited = set()
        grid = [list(row) for row in grid]  # make mutable
        m, n = len(grid), len(grid[0])

        def dfs(i, j, prev):
            # 越界直接返回，不在这里计为触边；由边界判定负责
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0, False
            # 不是同一连通块或已访问
            if grid[i][j] != prev or (i, j) in visited:
                return 0, False

            visited.add((i, j))
            area = 1
            # 关键修正：当前格子在边界 => 视为与外侧走廊相邻
            touches_corridor = (i == 0 or j == 0 or i == m - 1 or j == n - 1)

            # 四个方向探索
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] == '0':
                        touches_corridor = True
                    else:
                        a, t = dfs(ni, nj, prev)
                        area += a
                        touches_corridor = touches_corridor or t
            return area, touches_corridor

        # 这里仍然只从内圈启动 DFS（保持你的结构不变），
        # 但 DFS 会跑到边界并正确标记 touches_corridor
        for x in range(1, m - 1):
            for y in range(1, n - 1):
                if grid[x][y] != '0' and (x, y) not in visited:
                    area, touch = dfs(x, y, grid[x][y])
                    if not touch:
                        self.ans = max(self.ans, area)

        return self.ans



#-----------------------------------------------------------------------------











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
            
#https://leetcode.cn/problems/island-perimeter/
class Solution:
    # O(mn)
    # O(mn) note python uses stack for recursion
    # +1 when:
    # out of index
    # move to '0'

    #note here how we define the self.ans
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.ans = 0
        def dfs(i, j):
            global ans
            if i < 0 or j < 0 or i>= len(grid) or j >= len(grid[0]):
                self.ans += 1
                return 
            if grid[i][j] == 0:
                self.ans += 1
                return 
            if grid[i][j] == 1:
                grid[i][j] = -1 #mark as visited 
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)

        for x, row in enumerate(grid):
            for i, j in enumerate(row):
                if j == 1:
                    dfs(x, i)
    
        return self.ans 
                