import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))  # number of cargo types, always 1
    s = int(next(it))
    t = int(next(it))
    d = int(next(it))
    
    edges_input = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        limit = int(next(it))
        edges_input.append((u, v, limit))
    
    # Build graph for max flow
    # Nodes: 1..n
    adj = [[] for _ in range(n + 1)]
    edges = []
    
    def add_edge(u, v, cap):
        # forward edge index is len(edges)
        adj[u].append(len(edges))
        edges.append({'to': v, 'cap': cap, 'flow': 0, 'rev': len(edges) + 1})
        # reverse edge
        adj[v].append(len(edges))
        edges.append({'to': u, 'cap': 0, 'flow': 0, 'rev': len(edges) - 1})
    
    for u, v, limit in edges_input:
        add_edge(u, v, limit)
    
    # Dinic's algorithm
    level = [0] * (n + 1)
    ptr = [0] * (n + 1)
    
    def bfs():
        for i in range(1, n + 1):
            level[i] = -1
        q = deque()
        level[s] = 0
        q.append(s)
        while q:
            u = q.popleft()
            for idx in adj[u]:
                e = edges[idx]
                if e['cap'] > e['flow'] and level[e['to']] == -1:
                    level[e['to']] = level[u] + 1
                    q.append(e['to'])
        return level[t] != -1
    
    def dfs(u, pushed):
        if pushed == 0 or u == t:
            return pushed
        for i in range(ptr[u], len(adj[u])):
            ptr[u] = i
            idx = adj[u][i]
            e = edges[idx]
            if level[e['to']] != level[u] + 1:
                continue
            tr = dfs(e['to'], min(pushed, e['cap'] - e['flow']))
            if tr == 0:
                continue
            e['flow'] += tr
            edges[e['rev']]['flow'] -= tr
            return tr
        return 0
    
    flow = 0
    while bfs():
        ptr = [0] * (n + 1)
        while True:
            pushed = dfs(s, d - flow)
            if pushed == 0:
                break
            flow += pushed
            if flow == d:
                break
        if flow == d:
            break
    
    if flow < d:
        print("NO")
        return
    
    print("YES")
    result = []
    for i in range(m):
        # forward edge is at index 2*i
        result.append(str(edges[2*i]['flow']))
    print(' '.join(result))

if __name__ == "__main__":
    solve()