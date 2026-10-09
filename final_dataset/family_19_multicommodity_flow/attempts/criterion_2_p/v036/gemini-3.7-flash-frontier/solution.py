import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))

    s = int(next(it))
    t = int(next(it))
    d = int(next(it))

    # We will use 0-based indexing for internal nodes.
    # Virtual source S_prime = 0
    # Original nodes 1..n will be 1..n
    # Total nodes = n + 1
    S_prime = 0
    num_nodes = n + 1

    head = [-1] * num_nodes
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
        head[v] = idx + 1
        return idx

    # Add edge from S_prime to s with capacity d
    add_edge(S_prime, s, d)

    original_edge_indices = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        c = int(next(it))
        idx = add_edge(u, v, c)
        original_edge_indices.append(idx)

    # Dinic's Algorithm from S_prime to t
    level = [-1] * num_nodes
    ptr = [0] * num_nodes

    def bfs():
        for i in range(num_nodes):
            level[i] = -1
        level[S_prime] = 0
        q = deque([S_prime])
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
        if pushed == 0 or u == t:
            return pushed
        e = ptr[u]
        while e != -1:
            v = to[e]
            tr = cap[e] - flow[e]
            if level[v] == level[u] + 1 and tr > 0:
                push = dfs(v, min(pushed, tr))
                if push > 0:
                    flow[e] += push
                    flow[e ^ 1] -= push
                    return push
            e = nxt[e]
            ptr[u] = e
        return 0

    max_flow = 0
    INF = 10**18
    while bfs():
        for i in range(num_nodes):
            ptr[i] = head[i]
        while True:
            pushed = dfs(S_prime, INF)
            if pushed == 0:
                break
            max_flow += pushed

    if max_flow == d:
        print("YES")
        res = [str(flow[idx]) for idx in original_edge_indices]
        print(" ".join(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()