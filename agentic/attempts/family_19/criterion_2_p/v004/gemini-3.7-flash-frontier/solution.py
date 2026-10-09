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
    
    # 0 to n are original nodes (1-indexed, so 1..n)
    # super source = 0
    src = 0
    dst = t
    
    head = [-1] * (n + 1)
    to = []
    nxt = []
    cap = []
    edge_idx = []
    
    def add_edge(u, v, c, idx):
        to.append(v)
        cap.append(c)
        edge_idx.append(idx)
        nxt.append(head[u])
        head[u] = len(to) - 1
        
        to.append(u)
        cap.append(0)
        edge_idx.append(-1)
        nxt.append(head[v])
        head[v] = len(to) - 1

    add_edge(src, s, d, -1)
    
    orig_caps = []
    orig_edge_indices = []
    
    for i in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        c = int(next(iterator))
        orig_caps.append(c)
        orig_edge_indices.append(len(to))
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
                if cap[e] > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
                e = nxt[e]
        return level[dst] >= 0

    ptr = [0] * (n + 1)
    
    def dfs(u, pushed):
        if pushed == 0 or u == dst:
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
            ptr[u] = nxt[e]
            e = nxt[e]
        return 0

    total_flow = 0
    INF = 10**18
    while bfs():
        for i in range(n + 1):
            ptr[i] = head[i]
        while True:
            pushed = dfs(src, INF)
            if pushed == 0:
                break
            total_flow += pushed

    if total_flow == d:
        ans = []
        for i in range(m):
            e = orig_edge_indices[i]
            # flow is orig_cap - cap[e]
            ans.append(orig_caps[i] - cap[e])
        print("YES")
        print(*(ans))
    else:
        print("NO")

if __name__ == '__main__':
    solve()