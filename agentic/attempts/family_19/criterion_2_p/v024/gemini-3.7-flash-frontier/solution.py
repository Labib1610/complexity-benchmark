import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    _ = int(next(iterator)) # extract type = 1
    
    s = int(next(iterator))
    t = int(next(iterator))
    d = int(next(iterator))
    
    # 1-indexed to 0-indexed
    s -= 1
    t -= 1
    
    # Dinic's Algorithm
    head = [-1] * n
    to = []
    cap = []
    nxt = []
    orig_cap = []
    edge_idx_map = []
    
    def add_edge(u, v, c, idx):
        to.append(v)
        cap.append(c)
        orig_cap.append(c)
        nxt.append(head[u])
        edge_idx_map.append(idx)
        head[u] = len(to) - 1
        
        to.append(u)
        cap.append(0)
        orig_cap.append(0)
        nxt.append(head[v])
        edge_idx_map.append(-1)
        head[v] = len(to) - 1

    edge_forward_indices = []
    for i in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        c = int(next(iterator))
        edge_forward_indices.append(len(to))
        add_edge(u, v, c, i)
        
    if d == 0:
        print("YES")
        print(*(0 for _ in range(m)))
        return

    level = [-1] * n
    ptr = [0] * n
    
    def bfs():
        for i in range(n):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            e = head[v]
            while e != -1:
                if cap[e] > 0 and level[to[e]] < 0:
                    level[to[e]] = level[v] + 1
                    q.append(to[e])
                e = nxt[e]
        return level[t] != -1

    def dfs(v, pushed):
        if pushed == 0:
            return 0
        if v == t:
            return pushed
        e = ptr[v]
        while e != -1:
            u = to[e]
            tr = cap[e]
            if level[v] + 1 == level[u] and tr > 0:
                push = pushed if pushed < tr else tr
                tr_pushed = dfs(u, push)
                if tr_pushed > 0:
                    cap[e] -= tr_pushed
                    cap[e ^ 1] += tr_pushed
                    return tr_pushed
            e = nxt[e]
            ptr[v] = e
        return 0

    flow = 0
    while flow < d and bfs():
        for i in range(n):
            ptr[i] = head[i]
        while flow < d:
            pushed = dfs(s, d - flow)
            if pushed == 0:
                break
            flow += pushed

    if flow == d:
        print("YES")
        ans = [orig_cap[edge_forward_indices[i]] - cap[edge_forward_indices[i]] for i in range(m)]
        print(*ans)
    else:
        print("NO")

if __name__ == '__main__':
    solve()