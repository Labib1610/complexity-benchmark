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
    _ = int(next(iterator))
    
    s = int(next(iterator)) - 1
    t = int(next(iterator)) - 1
    d = int(next(iterator))

    if s == t:
        if d == 0:
            print("YES")
            print(*(0 for _ in range(m)))
        else:
            print("NO")
        return

    # Dinic's Algorithm
    head = [-1] * n
    to = []
    cap = []
    nxt = []
    orig_edge_idx = []

    def add_edge(u, v, c, idx):
        to.append(v)
        cap.append(c)
        nxt.append(head[u])
        orig_edge_idx.append(idx)
        head[u] = len(to) - 1

        to.append(u)
        cap.append(0)
        nxt.append(head[v])
        orig_edge_idx.append(-1)
        head[v] = len(to) - 1

    for i in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        c = int(next(iterator))
        add_edge(u, v, c, i)

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
        if pushed == 0 or v == t:
            return pushed
        e = ptr[v]
        while e != -1:
            trg = to[e]
            if level[v] + 1 == level[trg] and cap[e] > 0:
                tr = dfs(trg, min(pushed, cap[e]))
                if tr > 0:
                    cap[e] -= tr
                    cap[e ^ 1] += tr
                    return tr
            e = nxt[e]
            ptr[v] = e
        return 0

    flow = 0
    while flow < d and bfs():
        for i in range(n):
            ptr[i] = head[i]
        while True:
            pushed = dfs(s, d - flow)
            if pushed == 0:
                break
            flow += pushed
            if flow == d:
                break

    if flow == d:
        print("YES")
        ans = [0] * m
        for i in range(0, len(to), 2):
            idx = orig_edge_idx[i]
            # flow pushed through forward edge is initial capacity - remaining capacity
            # which is equal to cap[i ^ 1]
            ans[idx] = cap[i ^ 1]
        print(*(ans[i] for i in range(m)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()