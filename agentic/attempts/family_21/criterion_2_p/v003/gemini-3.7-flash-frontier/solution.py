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
    
    # Dinic's algorithm for min-cut
    head = [-1] * (n + 1)
    to = []
    cap = []
    nxt = []
    edge_id = []
    
    def add_edge(u, v, c, eid):
        nonlocal to, cap, nxt, head, edge_id
        nxt.append(head[u])
        head[u] = len(to)
        to.append(v)
        cap.append(c)
        edge_id.append(eid)
        
        nxt.append(head[v])
        head[v] = len(to)
        to.append(u)
        cap.append(c)
        edge_id.append(eid)
        
    edges = []
    idx = 5
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        idx += 3
        edges.append((u, v, w))
        add_edge(u, v, w, i)
        
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
                if cap[e] > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
                e = nxt[e]
        return level[t] >= 0

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

    total_flow = 0
    INF = 10**18
    while bfs():
        for i in range(n + 1):
            cur[i] = head[i]
        while True:
            f = dfs(s, INF)
            if f == 0:
                break
            total_flow += f
            if total_flow > B:
                break
        if total_flow > B:
            break

    if total_flow > B:
        print("NO")
        return

    # Find reachable nodes from s in residual graph
    visited = [False] * (n + 1)
    q = deque([s])
    visited[s] = True
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
    for u, v, w in edges:
        if visited[u] != visited[v]:
            cut_edges.append((u, v))

    print("YES")
    print(len(cut_edges))
    out = []
    for u, v in cut_edges:
        out.append(f"{u} {v}")
    if out:
        sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()