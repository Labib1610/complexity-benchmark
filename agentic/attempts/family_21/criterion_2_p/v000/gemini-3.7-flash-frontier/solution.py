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
    
    head = [-1] * (n + 1)
    to = []
    cap = []
    flow = []
    nxt = []
    
    def add_edge(u, v, w):
        nxt.append(head[u])
        head[u] = len(to)
        to.append(v)
        cap.append(w)
        flow.append(0)
        
        nxt.append(head[v])
        head[v] = len(to)
        to.append(u)
        cap.append(w)
        flow.append(0)

    idx = 5
    original_edges = []
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        idx += 3
        original_edges.append((u, v, w))
        add_edge(u, v, w)
        
    level = [-1] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            e = head[u]
            while e != -1:
                v = to[e]
                if cap[e] - flow[e] > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
                e = nxt[e]
        return level[t] >= 0

    ptr = [0] * (n + 1)
    
    def dfs(u, pushed):
        if pushed == 0 or u == t:
            return pushed
        e = ptr[u]
        while e != -1:
            v = to[e]
            tr = cap[e] - flow[e]
            if level[u] + 1 == level[v] and tr > 0:
                p = dfs(v, min(pushed, tr))
                if p > 0:
                    flow[e] += p
                    flow[e ^ 1] -= p
                    return p
            ptr[u] = nxt[e]
            e = nxt[e]
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
        print("NO")
        return

    visited = [False] * (n + 1)
    q = deque([s])
    visited[s] = True
    while q:
        u = q.popleft()
        e = head[u]
        while e != -1:
            v = to[e]
            if cap[e] - flow[e] > 0 and not visited[v]:
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