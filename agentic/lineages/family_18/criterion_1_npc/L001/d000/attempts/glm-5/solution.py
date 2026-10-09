import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # BFS from node 0 to compute distances
    dist = [-1] * n
    q = deque([0])
    dist[0] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    
    # Sort nodes by distance from node 0
    nodes = list(range(n))
    nodes.sort(key=lambda x: dist[x])
    
    # Assign stations: node at position i in sorted order gets station i+1
    station_of_node = [0] * n
    for i, node in enumerate(nodes):
        station_of_node[node] = i + 1
    
    # Compute total cord length
    total = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                total += abs(station_of_node[u] - station_of_node[v])
    
    if total <= k:
        print("YES")
        print(' '.join(map(str, station_of_node)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()