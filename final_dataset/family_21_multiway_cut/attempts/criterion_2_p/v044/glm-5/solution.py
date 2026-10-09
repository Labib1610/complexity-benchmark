import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n, m, s, t, B = map(int, input_data[:5])
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u, v, w = map(int, input_data[5 + 3*i : 5 + 3*i + 3])
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
        edges.append((u, v, w))
        
    if s == t:
        print("NO")
        return

    # Dijkstra to find the minimum cost to disconnect s and t
    pq = [(0, s)]
    dist = [float('inf')] * (n + 1)
    dist[s] = 0
    parent = [-1] * (n + 1)
    parent_edge = [-1] * (n + 1)
    
    head = 0
    while head < len(pq):
        d, u = pq[head]
        head += 1
        
        if d > dist[u]:
            continue
            
        if u == t:
            break
            
        for v, w, idx in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                parent[v] = u
                parent_edge[v] = idx
                pq.append((d + w, v))
                
    if dist[t] == float('inf'):
        # s and t are already disconnected
        print("YES")
        print(0)
        return
        
    if dist[t] > B:
        # We can afford to cut all paths
        print("YES")
        print(0)
        return
        
    # Reconstruct the shortest path
    path_edges = []
    curr = t
    while curr != s:
        path_edges.append(parent_edge[curr])
        curr = parent[curr]
        
    # Try cutting each edge on the shortest path
    for edge_idx in path_edges:
        u, v, w = edges[edge_idx]
        if w <= B:
            # Check if s and t are disconnected without this edge
            visited = [False] * (n + 1)
            q = deque([s])
            visited[s] = True
            found = False
            while q:
                curr = q.popleft()
                if curr == t:
                    found = True
                    break
                for nxt, _, idx in adj[curr]:
                    if idx != edge_idx and not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
            
            if not found:
                print("YES")
                print(1)
                print(u, v)
                return

    print("NO")

if __name__ == '__main__':
    solve()