import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    critical = set()
    for _ in range(t):
        critical.add(int(input_data[idx]) - 1); idx += 1
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    def bfs_farthest(start, targets):
        dist = [-1] * n
        parent = [-1] * n
        dist[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v, w in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    queue.append(v)
        best = -1
        best_node = start
        for node in targets:
            if dist[node] > best:
                best = dist[node]
                best_node = node
        return best_node, parent
    
    start = next(iter(critical))
    a, _ = bfs_farthest(start, critical)
    b, parent = bfs_farthest(a, critical)
    
    diameter_path = set()
    node = b
    while node != -1:
        diameter_path.add(node)
        node = parent[node]
    
    marked = set(diameter_path)
    for c in critical:
        node = c
        while node not in marked:
            marked.add(node)
            node = parent[node]
    
    total = 0
    for u in range(n):
        if u in marked:
            for v, w in adj[u]:
                if v > u and v in marked:
                    total += w
    
    print(total)

solve()