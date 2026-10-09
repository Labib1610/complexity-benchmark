import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    _ = int(next(iterator)) # category count (1)
    
    s = int(next(iterator))
    t = int(next(iterator))
    d = int(next(iterator))
    
    if s == t:
        if d == 0:
            print("YES")
            print(" ".join(["0"] * m))
        else:
            print("NO")
        return

    # Nodes: 0 to n, where 0 is super source
    SRC = 0
    SINK = t
    
    head = [-1] * (n + 1)
    to = []
    cap = []
    flow = []
    nxt = []
    
    def add_edge(u, v, c):
        idx = len(to)
        to.append(v)
        cap.append(c)
        flow.append(0)
        nxt.append(head[u])
        head[u] = idx
        
        to.append(u)
        cap.append(0)
        flow.append(0)
        nxt.append(head[v])
        head[v] = idx ^ 1
        return idx

    # Super source to s with capacity d
    add_edge(SRC, s, d)
    
    edge_indices = []
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        c = int(next(iterator))
        e_idx = add_edge(u, v, c)
        edge_indices.append(e_idx)
        
    level = [-1] * (n + 1)
    ptr = [0] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[SRC] = 0
        q = deque([SRC])
        while q:
            v = q.popleft()
            e = head[v]
            while e != -1:
                u = to[e]
                if cap[e] - flow[e] > 0 and level[u] < 0:
                    level[u] = level[v] + 1
                    q.append(u)
                e = nxt[e]
        return level[SINK] != -1

    def dfs(v, pushed):
        if pushed == 0 or v == SINK:
            return pushed
        e = ptr[v]
        while e != -1:
            u = to[e]
            tr = cap[e] - flow[e]
            if level[v] + 1 == level[u] and tr > 0:
                push = dfs(u, min(pushed, tr))
                if push > 0:
                    flow[e] += push
                    flow[e ^ 1] -= push
                    return push
            e = nxt[e]
            ptr[v] = e
        return 0

    total_flow = 0
    INF = 10**18
    while bfs():
        for i in range(n + 1):
            ptr[i] = head[i]
        while True:
            pushed = dfs(SRC, INF)
            if pushed == 0:
                break
            total_flow += pushed

    if total_flow == d:
        print("YES")
        ans = [str(flow[e_idx]) for e_idx in edge_indices]
        print(" ".join(ans))
    else:
        print("NO")

if __name__ == '__main__':
    solve()