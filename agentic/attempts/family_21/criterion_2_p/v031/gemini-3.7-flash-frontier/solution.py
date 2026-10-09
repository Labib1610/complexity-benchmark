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
    B = int(input_data[4])

    edges_input = []
    idx = 5

    head = [-1] * (n + 1)
    to = []
    cap = []
    flow = []
    nxt = []

    def add_edge(u, v, c):
        # u -> v
        nxt.append(head[u])
        to.append(v)
        cap.append(c)
        flow.append(0)
        head[u] = len(to) - 1

        # v -> u
        nxt.append(head[v])
        to.append(u)
        cap.append(c)
        flow.append(0)
        head[v] = len(to) - 1

    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        edges_input.append((u, v, w))
        add_edge(u, v, w)
        idx += 3

    # Dinic's Algorithm
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
                if cap[e] - flow[e] > 0 and level[u] == -1:
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
            tr = cap[e] - flow[e]
            if level[v] + 1 == level[u] and tr > 0:
                tr_pushed = dfs(u, min(pushed, tr))
                if tr_pushed > 0:
                    flow[e] += tr_pushed
                    flow[e ^ 1] -= tr_pushed
                    return tr_pushed
            ptr[v] = nxt[ptr[v]]
            e = ptr[v]
        return 0

    max_flow = 0
    INF = 10**18
    while bfs():
        for i in range(n + 1):
            ptr[i] = head[i]
        while True:
            pushed = dfs(s, INF)
            if pushed == 0:
                break
            max_flow += pushed
            if max_flow > B:
                break
        if max_flow > B:
            break

    if max_flow > B:
        print("NO")
        return

    # Find reachable nodes from s in the residual graph
    visited = [False] * (n + 1)
    visited[s] = True
    q = deque([s])
    while q:
        v = q.popleft()
        e = head[v]
        while e != -1:
            u = to[e]
            if cap[e] - flow[e] > 0 and not visited[u]:
                visited[u] = True
                q.append(u)
            e = nxt[e]

    # Collect cut edges
    cut_edges = []
    for u, v, w in edges_input:
        if (visited[u] and not visited[v]) or (visited[v] and not visited[u]):
            cut_edges.append((u, v))

    print("YES")
    print(len(cut_edges))
    for u, v in cut_edges:
        print(f"{u} {v}")

if __name__ == '__main__':
    solve()