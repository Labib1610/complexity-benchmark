import sys
from collections import deque

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        _ = int(next(iterator))  # currency count, always 1
        s = int(next(iterator))
        t = int(next(iterator))
        d = int(next(iterator))
    except StopIteration:
        return

    # Dinic's Algorithm
    head = [-1] * (n + 1)
    to = []
    cap = []
    nxt = []
    edge_idx = []  # to identify the original edge index

    def add_edge(u, v, c, idx):
        to.append(v)
        cap.append(c)
        nxt.append(head[u])
        edge_idx.append(idx)
        head[u] = len(to) - 1

        to.append(u)
        cap.append(0)
        nxt.append(head[v])
        edge_idx.append(-1)
        head[v] = len(to) - 1

    orig_edges = []
    for i in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        limit = int(next(iterator))
        orig_edges.append(len(to))  # the forward edge is at this index
        add_edge(u, v, limit, i)

    if d == 0:
        print("YES")
        print(" ".join("0" for _ in range(m)))
        return

    level = [-1] * (n + 1)
    ptr = [0] * (n + 1)

    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            e = head[v]
            while e != -1:
                u = to[e]
                if cap[e] > 0 and level[u] < 0:
                    level[u] = level[v] + 1
                    q.append(u)
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
                push = dfs(u, min(pushed, tr))
                if push > 0:
                    cap[e] -= push
                    cap[e ^ 1] += push
                    return push
            ptr[v] = nxt[e]
            e = nxt[e]
        return 0

    flow = 0
    while flow < d and bfs():
        for i in range(n + 1):
            ptr[i] = head[i]
        while flow < d:
            pushed = dfs(s, d - flow)
            if pushed == 0:
                break
            flow += pushed

    if flow < d:
        print("NO")
    else:
        print("YES")
        ans = []
        for e_id in orig_edges:
            # The flow sent along the forward edge is cap of reverse edge
            ans.append(str(cap[e_id ^ 1]))
        print(" ".join(ans))

if __name__ == '__main__':
    solve()