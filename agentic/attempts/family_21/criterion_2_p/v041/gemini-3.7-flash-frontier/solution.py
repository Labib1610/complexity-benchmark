import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    s = int(input_data[2])
    t = int(input_data[3])
    cap = int(input_data[4])

    if s == t:
        print("NO")
        return

    # Dinic's algorithm
    head = [-1] * (n + 1)
    to = []
    nxt = []
    capacity = []
    flow = []
    orig_edges = []

    def add_edge(u, v, c, idx):
        # Forward edge
        to.append(v)
        capacity.append(c)
        flow.append(0)
        nxt.append(head[u])
        head[u] = len(to) - 1

        # Backward edge
        to.append(u)
        capacity.append(c)
        flow.append(0)
        nxt.append(head[v])
        head[v] = len(to) - 1

    idx = 5
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        idx += 3
        add_edge(u, v, w, i)
        orig_edges.append((u, v, w))

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
                if capacity[e] - flow[e] > 0 and level[u] < 0:
                    level[u] = level[v] + 1
                    q.append(u)
                e = nxt[e]
        return level[t] >= 0

    def dfs(v, pushed):
        if pushed == 0:
            return 0
        if v == t:
            return pushed
        e = ptr[v]
        while e != -1:
            u = to[e]
            tr = capacity[e] - flow[e]
            if level[v] + 1 == level[u] and tr > 0:
                push = dfs(u, min(pushed, tr))
                if push > 0:
                    flow[e] += push
                    flow[e ^ 1] -= push
                    return push
            e = nxt[e]
            ptr[v] = e
        return 0

    max_flow = 0
    INF = 10**18
    while bfs():
        for i in range(n + 1):
            ptr[i] = head[i]
        while True:
            pushed = dfs(s, INF)
            if not pushed:
                break
            max_flow += pushed
            if max_flow > cap:
                break
        if max_flow > cap:
            break

    if max_flow > cap:
        print("NO")
        return

    # Find reachable nodes from s in residual graph
    visited = [False] * (n + 1)
    q = deque([s])
    visited[s] = True
    while q:
        v = q.popleft()
        e = head[v]
        while e != -1:
            u = to[e]
            if capacity[e] - flow[e] > 0 and not visited[u]:
                visited[u] = True
                q.append(u)
            e = nxt[e]

    cut_edges = []
    for u, v, w in orig_edges:
        if visited[u] != visited[v]:
            cut_edges.append((u, v))

    print("YES")
    print(len(cut_edges))
    for u, v in cut_edges:
        print(f"{u} {v}")

if __name__ == '__main__':
    solve()