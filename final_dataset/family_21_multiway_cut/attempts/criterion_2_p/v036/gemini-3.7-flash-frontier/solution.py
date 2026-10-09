import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        s = int(next(iterator)) - 1
        t = int(next(iterator)) - 1
        B = int(next(iterator))
    except StopIteration:
        return

    edges_input = []
    # Dinic's algorithm graph representation
    # head, to, cap, next_edge
    head = [-1] * n
    to = []
    cap = []
    next_edge = []
    
    def add_edge(u, v, c):
        to.append(v)
        cap.append(c)
        next_edge.append(head[u])
        head[u] = len(to) - 1
        
        to.append(u)
        cap.append(c)
        next_edge.append(head[v])
        head[v] = len(to) - 1

    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        w = int(next(iterator))
        edges_input.append((u, v, w))
        add_edge(u, v, w)
        
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
                e = next_edge[e]
        return level[t] >= 0

    def dfs(v, pushed):
        if pushed == 0:
            return 0
        if v == t:
            return pushed
        e = ptr[v]
        while e != -1:
            tr = to[e]
            if level[v] + 1 == level[tr] and cap[e] > 0:
                tr_pushed = dfs(tr, min(pushed, cap[e]))
                if tr_pushed > 0:
                    cap[e] -= tr_pushed
                    cap[e ^ 1] += tr_pushed
                    return tr_pushed
            ptr[v] = next_edge[e]
            e = next_edge[e]
        return 0

    flow = 0
    INF = 10**18
    while bfs():
        for i in range(n):
            ptr[i] = head[i]
        while True:
            pushed = dfs(s, INF)
            if pushed == 0:
                break
            flow += pushed

    if flow > B:
        print("NO")
        return

    # Find the reachable component from s in residual graph
    visited = [False] * n
    q = deque([s])
    visited[s] = True
    while q:
        v = q.popleft()
        e = head[v]
        while e != -1:
            if cap[e] > 0 and not visited[to[e]]:
                visited[to[e]] = True
                q.append(to[e])
            e = next_edge[e]

    cut_edges = []
    for u, v, w in edges_input:
        if visited[u] != visited[v]:
            cut_edges.append((u + 1, v + 1))

    print("YES")
    print(len(cut_edges))
    for u, v in cut_edges:
        print(f"{u} {v}")

if __name__ == '__main__':
    solve()