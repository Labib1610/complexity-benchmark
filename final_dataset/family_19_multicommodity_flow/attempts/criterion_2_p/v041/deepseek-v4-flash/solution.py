import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))  # constant 1
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))
    
    edges = []
    graph = [[] for _ in range(n)]
    
    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
        graph[u].append([v, cap, i, len(graph[v])])
        graph[v].append([u, 0, i, len(graph[u]) - 1])
    
    # Dinic's algorithm
    def bfs():
        level = [-1] * n
        q = deque([s])
        level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, idx, rev in graph[u]:
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level
    
    def dfs(u, f, level, it_ptr):
        if u == t:
            return f
        while it_ptr[u] < len(graph[u]):
            v, cap, idx, rev = graph[u][it_ptr[u]]
            if cap > 0 and level[v] == level[u] + 1:
                ret = dfs(v, min(f, cap), level, it_ptr)
                if ret > 0:
                    graph[u][it_ptr[u]][1] -= ret
                    graph[v][rev][1] += ret
                    return ret
            it_ptr[u] += 1
        return 0
    
    flow = 0
    INF = 10**18
    while True:
        level = bfs()
        if level[t] < 0:
            break
        it_ptr = [0] * n
        while True:
            f = dfs(s, INF, level, it_ptr)
            if f == 0:
                break
            flow += f
    
    if flow < d:
        print("NO")
        return
    
    # Extract flow on each original edge
    result = [0] * m
    for u in range(n):
        for v, cap, idx, rev in graph[u]:
            if idx != -1 and cap < edges[idx][2]:
                # original capacity minus remaining capacity = flow
                result[idx] = edges[idx][2] - cap
    
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    solve()