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
    B = int(next(it))
    
    hubs = set()
    for _ in range(k):
        hubs.add(int(next(it)))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w, i))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # BFS from each hub to find edges on shortest paths to other hubs
    edge_on_sp = [False] * m
    hub_list = list(hubs)
    
    for h in hub_list:
        dist = [-1] * (n + 1)
        parent = [[] for _ in range(n + 1)]
        q = deque([h])
        dist[h] = 0
        
        while q:
            u = q.popleft()
            for v, eid in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v].append((u, eid))
                    q.append(v)
                elif dist[v] == dist[u] + 1:
                    parent[v].append((u, eid))
        
        # Mark edges on shortest paths to other hubs
        for other in hub_list:
            if other == h:
                continue
            # BFS backwards from other
            visited = [False] * (n + 1)
            q = deque([other])
            visited[other] = True
            while q:
                v = q.popleft()
                for pu, eid in parent[v]:
                    edge_on_sp[eid] = True
                    if not visited[pu]:
                        visited[pu] = True
                        q.append(pu)
    
    candidate_edges = []
    for i, (u, v, w, _) in enumerate(edges):
        if edge_on_sp[i]:
            candidate_edges.append((w, u, v, i))
    
    candidate_edges.sort()
    
    # Check if we can isolate all hubs
    # Use DSU to check connectivity
    parent_dsu = list(range(n + 1))
    rank = [0] * (n + 1)
    
    def find(x):
        if parent_dsu[x] != x:
            parent_dsu[x] = find(parent_dsu[x])
        return parent_dsu[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent_dsu[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    # First, add all non-candidate edges
    for i, (u, v, w, _) in enumerate(edges):
        if not edge_on_sp[i]:
            union(u, v)
    
    # Check if any two hubs are already connected without candidate edges
    hub_roots = set()
    for h in hub_list:
        r = find(h)
        if r in hub_roots:
            # Already connected - need to seal some candidate edges
            break
        hub_roots.add(r)
    else:
        # All hubs already isolated
        print("YES")
        print(0)
        return
    
    # Greedy: add candidate edges in order of increasing weight
    # until all hubs are isolated
    total_cost = 0
    sealed = []
    
    # Reset DSU
    parent_dsu = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # Add all non-candidate edges
    for i, (u, v, w, _) in enumerate(edges):
        if not edge_on_sp[i]:
            union(u, v)
    
    # Now try to add candidate edges, but skip if it connects two hubs
    for w, u, v, i in candidate_edges:
        pu, pv = find(u), find(v)
        # Check if adding this edge would connect two hubs
        connects_hubs = False
        for h1 in hub_list:
            if find(h1) == pu:
                for h2 in hub_list:
                    if h1 != h2 and find(h2) == pv:
                        connects_hubs = True
                        break
                if connects_hubs:
                    break
        
        if connects_hubs:
            # Seal this edge
            if total_cost + w > B:
                print("NO")
                return
            total_cost += w
            sealed.append((u, v))
        else:
            # Add this edge to the graph
            union(u, v)
    
    # Verify all hubs are isolated
    hub_roots = set()
    for h in hub_list:
        hub_roots.add(find(h))
    
    if len(hub_roots) == k:
        print("YES")
        print(len(sealed))
        for u, v in sealed:
            print(u, v)
    else:
        print("NO")

if __name__ == "__main__":
    solve()