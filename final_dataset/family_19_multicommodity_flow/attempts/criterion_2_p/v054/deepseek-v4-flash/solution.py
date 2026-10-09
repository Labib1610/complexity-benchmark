import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, _ = map(int, input().split())
    s, t, d = map(int, input().split())
    s -= 1
    t -= 1
    
    edges = []
    graph = [[] for _ in range(n)]
    
    for i in range(m):
        u, v, cap = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append([v, cap, i, len(graph[v])])
        graph[v].append([u, 0, i, len(graph[u]) - 1])
        edges.append((u, v, cap))
    
    # Dinic's algorithm
    level = [-1]*n
    iter = [0]*n
    
    def bfs():
        for i in range(n):
            level[i] = -1
        q = deque()
        level[s] = 0
        q.append(s)
        while q:
            v = q.popleft()
            for to, cap, _, _ in graph[v]:
                if cap > 0 and level[to] < 0:
                    level[to] = level[v] + 1
                    q.append(to)
        return level[t] >= 0
    
    def dfs(v, f):
        if v == t:
            return f
        for i in range(iter[v], len(graph[v])):
            iter[v] = i
            to, cap, idx, rev = graph[v][i]
            if cap > 0 and level[v] + 1 == level[to]:
                ret = dfs(to, min(f, cap))
                if ret > 0:
                    graph[v][i][1] -= ret
                    graph[to][rev][1] += ret
                    return ret
        return 0
    
    flow = 0
    INF = 10**18
    while bfs():
        iter = [0]*n
        while True:
            f = dfs(s, INF)
            if f == 0:
                break
            flow += f
    
    if flow < d:
        print("NO")
    else:
        print("YES")
        # Now get the flow values from residual graph
        # For each original edge, flow = original cap - current residual cap
        res = []
        for u, v, cap in edges:
            # find the forward edge in graph[u]
            for to, cap_left, idx, rev in graph[u]:
                if to == v and cap_left <= cap:
                    res.append(cap - cap_left)
                    break
        print(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()