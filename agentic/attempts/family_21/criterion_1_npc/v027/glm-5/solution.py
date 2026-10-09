import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))
    
    anchors = set()
    for _ in range(k):
        anchors.add(int(next(it)))
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # BFS to find shortest paths from anchors
    INF = float('inf')
    dist = [INF] * (n + 1)
    source = [0] * (n + 1)
    q = deque()
    
    for a in anchors:
        dist[a] = 0
        source[a] = a
        q.append(a)
    
    while q:
        u = q.popleft()
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                source[v] = source[u]
                q.append(v)
    
    # Find minimum cut edges
    cut_edges = []
    for u, v, w in edges:
        if source[u] != source[v]:
            cut_edges.append((w, u, v))
    
    # Sort by weight and use greedy selection
    cut_edges.sort()
    total = 0
    result_edges = []
    
    for w, u, v in cut_edges:
        if total + w <= B:
            total += w
            result_edges.append((u, v))
        else:
            break
    
    # Check if all anchors are separated
    # Build graph without selected edges
    blocked = set()
    for u, v in result_edges:
        if u > v:
            u, v = v, u
        blocked.add((u, v))
    
    adj2 = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        a, b = u, v
        if a > b:
            a, b = b, a
        if (a, b) not in blocked:
            adj2[u].append(v)
            adj2[v].append(u)
    
    visited = [False] * (n + 1)
    anchor_list = list(anchors)
    
    for a in anchor_list:
        if visited[a]:
            continue
        q = deque([a])
        visited[a] = True
        anchor_count = 0
        while q:
            u = q.popleft()
            if u in anchors:
                anchor_count += 1
            for v in adj2[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        if anchor_count > 1:
            print("NO")
            return
    
    print("YES")
    print(len(result_edges))
    for u, v in result_edges:
        print(u, v)

if __name__ == "__main__":
    solve()