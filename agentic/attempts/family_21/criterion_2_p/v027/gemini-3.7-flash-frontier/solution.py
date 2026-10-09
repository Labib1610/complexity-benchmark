import sys
from collections import deque

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    s = int(data[2])
    t = int(data[3])
    B = int(data[4])
    
    if s == t:
        print("NO")
        return

    # Dinic's algorithm
    # Graph representation
    head = [-1] * (n + 1)
    to = []
    cap = []
    nxt = []
    
    def add_edge(u, v, c):
        to.append(v)
        cap.append(c)
        nxt.append(head[u])
        head[u] = len(to) - 1
        
        to.append(u)
        cap.append(c)
        nxt.append(head[v])
        head[v] = len(to) - 1

    original_edges = []
    idx = 5
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        w = int(data[idx+2])
        idx += 3
        original_edges.append((u, v, w))
        add_edge(u, v, w)

    level = [-1] * (n + 1)
    
    def bfs():
        for i in range(1, n + 1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            e = head[u]
            while e != -1:
                v = to[e]
                if cap[e] > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
                e = nxt[e]
        return level[t] != -1

    cur = [0] * (n + 1)

    def dfs(u, flow):
        if u == t or flow == 0:
            return flow
        pushed = 0
        e = cur[u]
        while e != -1:
            cur[u] = e
            v = to[e]
            if level[v] == level[u] + 1 and cap[e] > 0:
                tr = dfs(v, min(flow, cap[e]))
                if tr > 0:
                    cap[e] -= tr
                    cap[e ^ 1] += tr
                    pushed += tr
                    flow -= tr
                    if flow == 0:
                        break
            e = nxt[e]
        return pushed

    INF = float('inf')
    max_flow = 0
    while bfs():
        for i in range(1, n + 1):
            cur[i] = head[i]
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

    # Find reachable nodes from s in residual graph
    visited = [False] * (n + 1)
    visited[s] = True
    q = deque([s])
    while q:
        u = q.popleft()
        e = head[u]
        while e != -1:
            v = to[e]
            if cap[e] > 0 and not visited[v]:
                visited[v] = True
                q.append(v)
            e = nxt[e]

    cut_edges = []
    for u, v, w in original_edges:
        if visited[u] != visited[v]:
            cut_edges.append((u, v))

    print("YES")
    print(len(cut_edges))
    for u, v in cut_edges:
        print(f"{u} {v}")

if __name__ == '__main__':
    solve()