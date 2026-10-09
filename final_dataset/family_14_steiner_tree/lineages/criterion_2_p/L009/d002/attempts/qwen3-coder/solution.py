import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    N, E, F = map(int, sys.stdin.readline().split())
    critical = set(map(int, sys.stdin.readline().split()))
    
    edges = []
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    edges.sort()
    
    parent = list(range(N + 1))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    total_weight = 0
    connected_critical = 0
    
    for w, u, v in edges:
        if union(u, v):
            total_weight += w
            # Check if both u and v are critical
            critical_u = u in critical
            critical_v = v in critical
            
            if critical_u and critical_v:
                connected_critical += 2
            elif critical_u or critical_v:
                connected_critical += 1
                
            # Early termination: if all critical nodes are connected
            if connected_critical >= 2 * F - 2:
                break
    
    # Actually we need to compute the MST that connects all critical nodes
    # Let's use a different approach: build a MST of the whole graph and then 
    # find the minimal subtree that connects all critical nodes (Steiner tree)
    # But since this is a tree, the Steiner tree is just the union of paths between critical nodes
    # We can do this by building the MST and then finding the minimal connected subtree containing all critical nodes
    
    # Simpler approach: Build the MST and then calculate the total weight of edges needed to connect all critical nodes
    
    # Reset Union-Find
    parent = list(range(N + 1))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    # Kruskal's algorithm to build MST
    mst_edges = []
    for w, u, v in edges:
        if union(u, v):
            mst_edges.append((w, u, v))
            
    # Now we have the MST, we need to find the minimum subtree connecting all critical nodes
    # In a tree, this is equivalent to finding the union of all paths between pairs of critical nodes
    # Which is the same as finding the minimal connected subgraph containing all critical nodes
    
    # Build adjacency list of MST
    adj = [[] for _ in range(N + 1)]
    for w, u, v in mst_edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    # If there's only one critical node, cost is 0
    if F <= 1:
        print(0)
        return
        
    # Find all critical nodes
    critical_list = list(critical)
    
    # We'll use the fact that in a tree, the minimal connected subgraph containing a set of vertices
    # is the union of paths between them. This is equivalent to finding the "Steiner tree" for the set.
    # A simple way: mark all nodes and do a DFS to find the minimal subtree
    
    # Mark critical nodes
    is_critical = [False] * (N + 1)
    for c in critical:
        is_critical[c] = True
        
    visited = [False] * (N + 1)
    total_cost = [0]
    
    # DFS to find the minimal subtree spanning all critical nodes
    def dfs(u):
        visited[u] = True
        # Count critical nodes in subtree rooted at u
        count = 1 if is_critical[u] else 0
        for v, w in adj[u]:
            if not visited[v]:
                sub_count = dfs(v)
                if sub_count > 0:  # There are critical nodes in the subtree
                    count += sub_count
                    total_cost[0] += w
        return count
    
    # Start DFS from first critical node
    dfs(critical_list[0])
    
    print(total_cost[0])

# Threading is used to increase recursion limit
threading.Thread(target=main).start()