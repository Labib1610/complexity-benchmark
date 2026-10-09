from collections import deque
import sys

# Increase recursion depth for deep DFS in Dinic's algorithm
sys.setrecursionlimit(300000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    # input_data[2] is 1 (product category)
    s = int(input_data[3])
    t = int(input_data[4])
    d = int(input_data[5])

    # Graph representation:
    # 0 is super-source, hubs are 1..n
    head = [-1] * (n + 1)
    to = []
    cap = []
    flow = []
    nxt = []

    def add_edge(u, v, c):
        idx_forward = len(to)
        nxt.append(head[u])
        head[u] = idx_forward
        to.append(v)
        cap.append(c)
        flow.append(0)

        nxt.append(head[v])
        head[v] = idx_forward + 1
        to.append(u)
        cap.append(0)
        flow.append(0)
        return idx_forward

    # Add source edge to limit max total flow to d
    add_edge(0, s, d)

    edge_indices = []
    idx = 6
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        idx += 3
        edge_indices.append(add_edge(u, v, c))

    src = 0
    sink = t

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
                if cap[e] - flow[e] > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
                e = nxt[e]
        return level[sink] != -1

    ptr = [0] * (n + 1)

    def dfs(u, pushed):
        if pushed == 0 or u == sink:
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

    max_f = 0
    INF = 10**18
    while bfs():
        for i in range(n + 1):
            ptr[i] = head[i]
        while True:
            pushed = dfs(src, INF)
            if pushed == 0:
                break
            max_f += pushed

    if max_f == d:
        print("YES")
        print(*(flow[e_idx] for e_idx in edge_indices))
    else:
        print("NO")


if __name__ == "__main__":
    solve()