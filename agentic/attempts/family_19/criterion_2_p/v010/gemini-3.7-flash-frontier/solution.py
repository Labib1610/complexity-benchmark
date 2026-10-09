import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    k = int(next(iterator))
    
    s = int(next(iterator))
    t = int(next(iterator))
    d = int(next(iterator))
    
    if d < 0:
        print("NO")
        return
    
    if s == t:
        if d == 0:
            print("YES")
            print(" ".join(["0"] * m))
        else:
            print("NO")
        return

    # Dinic's Algorithm
    src = 0
    snk = t
    
    # Graph representation
    head = [-1] * (n + 1)
    to = []
    cap = []
    flow = []
    nxt = []
    edge_idx = []
    
    def add_edge(u, v, c, idx):
        to.append(v)
        cap.append(c)
        flow.append(0)
        nxt.append(head[u])
        edge_idx.append(idx)
        head[u] = len(to) - 1
        
        to.append(u)
        cap.append(0)
        flow.append(0)
        nxt.append(head[v])
        edge_idx.append(-1)
        head[v] = len(to) - 1

    add_edge(src, s, d, -1)
    
    for i in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        c = int(next(iterator))
        add_edge(u, v, c, i)
        
    level = [-1] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[src] = 0
        q = deque([src])
        while q:
            u = q.popleft()
            e = head[u]
            while e != -1:
                v = to[e]
                if cap[e] - flow[e] > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
                e = nxt[e]
        return level[snk] != -1

    cur_ptr = [0] * (n + 1)
    
    def dfs(u, pushed):
        if pushed == 0:
            return 0
        if u == snk:
            return pushed
        
        e = cur_ptr[u]
        while e != -1:
            cur_ptr[u] = e
            v = to[e]
            tr = cap[e] - flow[e]
            if level[u] + 1 == level[v] and tr > 0:
                push = dfs(v, min(pushed, tr))
                if push > 0:
                    flow[e] += push
                    flow[e ^ 1] -= push
                    return push
            e = nxt[e]
        return 0

    max_flow = 0
    INF = 10**18
    while bfs():
        for i in range(n + 1):
            cur_ptr[i] = head[i]
        while True:
            pushed = dfs(src, INF)
            if pushed == 0:
                break
            max_flow += pushed

    if max_flow == d:
        print("YES")
        ans = [0] * m
        for e in range(len(to)):
            idx = edge_idx[e]
            if idx != -1:
                ans[idx] = flow[e]
        print(*(ans))
    else:
        print("NO")

if __name__ == '__main__':
    solve()