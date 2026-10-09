import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1

    S = n + k + 1
    T = S + 1
    total_nodes = T + 1

    head = [-1] * total_nodes
    to = []
    cap = []
    nxt = []
    edge_id = []

    def add_edge(u, v, c, eid=-1):
        head[u] = len(to)
        to.append(v); cap.append(c); nxt.append(head[u]); edge_id.append(eid)
        head[v] = len(to)
        to.append(u); cap.append(0); nxt.append(head[v]); edge_id.append(-1)

    for i in range(k):
        s = int(input_data[idx]) - 1; idx += 1
        t = int(input_data[idx]) - 1; idx += 1
        d = int(input_data[idx]); idx += 1
        add_edge(S, n + i, d)
        add_edge(n + i, s, d)
        add_edge(t, n + i, d)

    for j in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        c = int(input_data[idx]); idx += 1
        add_edge(u, v, c, j)

    total_demand = 0
    e = 0
    while e < len(to):
        if edge_id[e] == -1 and to[e] == n:
            total_demand += cap[e]
        e += 2

    level = [0] * total_nodes
    it = [0] * total_nodes

    def bfs():
        for i in range(total_nodes):
            level[i] = -1
        level[S] = 0
        q = deque([S])
        while q:
            u = q.popleft()
            e = head[u]
            while e != -1:
                if cap[e] > 0 and level[to[e]] < 0:
                    level[to[e]] = level[u] + 1
                    q.append(to[e])
                e = nxt[e]
        return level[T] >= 0

    def dfs(u, f):
        if u == T:
            return f
        while it[u] != -1:
            e = it[u]
            v = to[e]
            if cap[e] > 0 and level[v] == level[u] + 1:
                ret = dfs(v, min(f, cap[e]))
                if ret > 0:
                    cap[e] -= ret
                    cap[e ^ 1] += ret
                    return ret
            it[u] = nxt[e]
        return 0

    flow = 0
    while bfs():
        for i in range(total_nodes):
            it[i] = head[i]
        while True:
            f = dfs(S, 10**18)
            if f == 0:
                break
            flow += f

    if flow < total_demand:
        print("NO")
        return

    ans = [[0] * m for _ in range(k)]
    e = 0
    while e < len(to):
        if edge_id[e] >= 0:
            j = edge_id[e]
            v = to[e]
            if n <= v < n + k:
                ans[v - n][j] = cap[e ^ 1]
        e += 2

    print("YES")
    out = []
    for i in range(k):
        out.append(' '.join(map(str, ans[i])))
    sys.stdout.write('\n'.join(out) + '\n')

solve()