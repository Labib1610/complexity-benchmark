import sys
from collections import deque

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

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
    
    if s == t:
        if d == 0:
            print("YES")
            print(*(0 for _ in range(m)))
        else:
            print("NO")
        return

    head = [-1] * (n + 1)
    to = []
    nxt = []
    cap = []
    flow = []
    edge_indices = []

    def add_edge(u, v, c, idx):
        to.append(v)
        cap.append(c)
        flow.append(0)
        nxt.append(head[u])
        edge_indices.append(idx)
        head[u] = len(to) - 1

        to.append(u)
        cap.append(0)
        flow.append(0)
        nxt.append(head[v])
        edge_indices.append(-1)
        head[v] = len(to) - 1

    orig_edges = []
    for i in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        L = int(next(iterator))
        orig_edges.append(len(to))
        add_edge(u, v, L, i)

    level = [-1] * (n + 1)
    ptr = [0] * (n + 1)

    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            e = head[u]
            while e != -1:
                v = to[e]
                if cap[e] - flow[e] > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
                e = nxt[e]
        return level[t] != -1

    def dfs(u, pushed):
        if pushed == 0:
            return 0
        if u == t:
            return pushed
        e = ptr[u]
        while e != -1:
            v = to[e]
            tr = cap[e] - flow[e]
            if level[u] + 1 == level[v] and tr > 0:
                push = dfs(v, min(pushed, tr))
                if push > 0:
                    flow[e] += push
                    flow[e ^ 1] -= push
                    return push
            ptr[u] = nxt[e]
            e = nxt[e]
        return 0

    tot_flow = 0
    while tot_flow < d and bfs():
        for i in range(n + 1):
            ptr[i] = head[i]
        while tot_flow < d:
            pushed = dfs(s, d - tot_flow)
            if pushed == 0:
                break
            tot_flow += pushed

    if tot_flow == d:
        print("YES")
        ans = [0] * m
        for i in range(m):
            e_idx = orig_edges[i]
            ans[i] = flow[e_idx]
        print(*(ans))
    else:
        print("NO")

if __name__ == '__main__':
    solve()