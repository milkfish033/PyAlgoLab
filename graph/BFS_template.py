# 计算从 start 到各个节点的最短路长度
# 如果节点不可达，则最短路长度为 -1
# 节点编号从 0 到 n-1，边权均为 1
def bfs(n: int, edges: List[List[int]], start: int) -> List[int]:
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)  # 无向图

    dis = [-1] * n  # -1 表示尚未访问到
    dis[start] = 0
    q = deque([start])
    while q:
        x = q.popleft()
        for y in g[x]:
            if dis[y] < 0:
                dis[y] = dis[x] + 1
                q.append(y)
    return dis

