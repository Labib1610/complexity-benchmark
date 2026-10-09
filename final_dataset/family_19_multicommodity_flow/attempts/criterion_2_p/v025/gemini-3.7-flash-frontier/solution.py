import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    n = int(next(iterator))
    m = int(next(iterator))
    _ = next(iterator)
    
    s = int(next(iterator))
    t = int(next(iterator))
    d = int(next(iterator))
    
    if s == t:
        if d == 0:
            print("YES")
            print(*(0 for _ in range(m)))
        else:
            print("NO")
        return

    # Super-source: 0, nodes 1..n, target t
    # S = 0
    # Add edge S -> s with capacity d
    
    head = [-1] * (n + 1)
    to = []
    nxt = []
    cap = []
    
    def add_edge(u, v, c):
        to.append(v)
        cap.append(c)
        nxt.append(head[u])
        head[u] = len(to) - 1
        
        to.append(u)
        cap.append(0)
        nxt.append(head[v])
        head[v] = len(to) - 1

    # Edge from super-source 0 to s
    add_edge(0, s, d)
    
    # Original edges start at index 2 (edge 2 and 3 in to/cap arrays)
    edge_indices = []
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        c = int(next(iterator))
        edge_indices.append(len(to))
        add_edge(u, v, c)
        
    # Dinic's Algorithm from S=0 to t
    level = [-1] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[0] = 0
        q = deque([0])
        while q:
            u = q.popleft()
            e = head[u]
            while e != -1:
                v = to[e]
                if cap[e] > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
                e = nxt[e]
        return level[t] >= 0

    ptr = [0] * (n + 1)
    
    def dfs(u, pushed):
        if pushed == 0 or u == t:
            return pushed
        e = ptr[u]
        while e != -1:
            v = to[e]
            tr = cap[e]
            if level[u] + 1 == level[v] and tr > 0:
                push = dfs(v, min(pushed, tr))
                if push > 0:
                    cap[e] -= push
                    cap[e ^ 1] += push
                    return push
            e = nxt[e]
            ptr[u] = e
        return 0

    flow = 0
    INF = float('inf')
    while bfs():
        for i in range(n + 1):
            ptr[i] = head[i]
        while True:
            pushed = dfs(0, INF)
            if pushed == 0:
                break
            flow += pushed

    if flow == d:
        print("YES")
        ans = [cap[idx ^ 1] for idx in edge_indices]
        print(*(ans))
    else:
        print("NO")

if __name__ == '__main__':
    solve()