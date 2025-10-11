def solve(n: int, edges: List[List[int]]) -> List[int]:
    # 节点编号从 0 到 n-1
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)  # 无向图

    vis = [False] * n

    def dfs(x: int) -> int:
        vis[x] = True  # 避免重复访问节点
        size = 1
        for y in g[x]:
            if not vis[y]:
                size += dfs(y)
        return size

    # 计算每个连通块的大小
    ans = []
    for i, b in enumerate(vis):
        if not b:  # i 没有访问过
            size = dfs(i)
            ans.append(size)
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
            