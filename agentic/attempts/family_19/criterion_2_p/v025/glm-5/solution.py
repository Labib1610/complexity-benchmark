import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    _ = int(data[idx]); idx += 1
    s = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    d = int(data[idx]); idx += 1

    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        cap = int(data[idx]); idx += 1
        edges.append((u, v, cap))

    # Dinic max flow
    N = n + 1
    head = [-1] * N
    to = []
    cap_list = []
    nxt = []

    def add_edge(u, v, c):
        to.append(v)
        cap_list.append(c)
        nxt.append(head[u])
        head[u] = len(to) - 1
        to.append(u)
        cap_list.append(0)
        nxt.append(head[v])
        head[v] = len(to) - 1

    for (u, v, c) in edges:
        add_edge(u, v, c)

    level = [0] * N
    ptr = [0] * N
    from collections import deque

    def bfs():
        for i in range(N):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            e = head[u]
            while e != -1:
                v = to[e]
                if cap_list[e] > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
                e = nxt[e]
        return level[t] >= 0

    def dfs(u, f):
        if u == t:
            return f
        e = ptr[u]
        while e != -1:
            v = to[e]
            if cap_list[e] > 0 and level[v] == level[u] + 1:
                pushed = dfs(v, f if f < cap_list[e] else cap_list[e])
                if pushed > 0:
                    cap_list[e] -= pushed
                    cap_list[e ^ 1] += pushed
                    return pushed
            e = nxt[e]
            ptr[u] = e
        return 0

    max_flow = 0
    while bfs():
        for i in range(N):
            ptr[i] = head[i]
        while True:
            pushed = dfs(s, 10**18)
            if pushed == 0:
                break
            max_flow += pushed

    if max_flow < d:
        sys.stdout.write("NO\n")
        return

    # Extract flow on each original edge
    flow_vals = []
    for i in range(m):
        # original edge index in adjacency: 2*i (forward), residual = cap_list[2*i]
        orig_cap = edges[i][2]
        residual = cap_list[2 * i]
        flow_vals.append(orig_cap - residual)

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, flow_vals)) + "\n")

if __name__ == "__main__":
    solve()