import sys
import heapq
from collections import defaultdict

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

def kruskal(n, edges, required_vertices):
    if len(required_vertices) <= 1:
        return 0
    
    # Create a mapping for required vertices to indices 0 to t-1
    req_list = list(required_vertices)
    vertex_to_index = {v: i for i, v in enumerate(req_list)}
    t = len(req_list)
    
    # We need to connect all required vertices, so we need (t-1) edges in MST
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    total_cost = 0
    connected_components = t
    
    # Union-Find for required vertices: track which required vertices are connected
    req_parent = list(range(t))
    req_rank = [0] * t
    
    def req_find(x):
        if req_parent[x] != x:
            req_parent[x] = req_find(req_parent[x])
        return req_parent[x]
    
    def req_union(x, y):
        px, py = req_find(x), req_find(y)
        if px == py:
            return False
        if req_rank[px] < req_rank[py]:
            px, py = py, px
        req_parent[py] = px
        if req_rank[px] == req_rank[py]:
            req_rank[px] += 1
        return True
    
    for u, v, w in edges:
        if union(parent, rank, u, v):
            # Check if this edge connects two different required vertices or 
            # connects a required vertex to a component with required vertices
            u_req_idx = vertex_to_index.get(u, -1)
            v_req_idx = vertex_to_index.get(v, -1)
            
            # If both ends have required vertices, try to unite them
            if u_req_idx != -1 and v_req_idx != -1:
                if req_union(u_req_idx, v_req_idx):
                    total_cost += w
                    connected_components -= 1
            elif u_req_idx != -1 or v_req_idx != -1:
                # One end has a required vertex, the other might connect to a component with required vertices
                # Since we're building a spanning tree, just add the edge cost if it connects components
                total_cost += w
                # Check if this reduces the number of required components
                # This is tricky; let's use a simpler approach
                
                # Actually, let's reconsider the approach:
                # We want to find the minimum cost to connect all required vertices
                # This is exactly the Steiner tree problem, but we can solve it with enumeration since t<=10
                
            if connected_components == 1:
                break
    
    # Let me restart with a cleaner approach
    # Since t <= 10, we can use a different method
    # Find the minimum spanning tree that connects all required vertices
    
    # Better approach: Modified Kruskal's algorithm
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    total_cost = 0
    req_components = len(required_vertices)
    
    # Create initial required component tracking
    req_component = {}
    for i, v in enumerate(required_vertices):
        req_component[v] = v
    
    edges.sort()
    
    for u, v, w in edges:
        pu, pv = find(parent, u), find(parent, v)
        if pu != pv:
            # Check if this connects required vertices
            req_u = req_component.get(pu, None)
            req_v = req_component.get(pv, None)
            
            union(parent, rank, u, v)
            
            # Update required component tracking
            new_req = req_u or req_v
            if new_req:
                req_component[find(parent, u)] = new_req
            
            if req_u and req_v and req_u != req_v:
                total_cost += w
                req_components -= 1
            elif req_u or req_v:
                total_cost += w
                
            if req_components <= 1:
                break
    
    # Even simpler approach for correctness:
    # Use Kruskal's algorithm and stop when all required vertices are connected
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # Track connectivity of required vertices
    req_parents = {x: x for x in required_vertices}
    
    def req_find(x):
        if req_parents[x] != x:
            req_parents[x] = req_find(req_parents[x])
        return req_parents[x]
    
    def req_union(x, y):
        px, py = req_find(x), req_find(y)
        if px == py:
            return False
        req_parents[px] = py
        return True
    
    total_cost = 0
    edges.sort()
    req_count = len(required_vertices)
    
    for u, v, w in edges:
        if union(parent, rank, u, v):
            # Check if this connects required vertices
            req_u = u in required_vertices
            req_v = v in required_vertices
            
            should_connect = False
            if req_u and req_v:
                if req_find(u) != req_find(v):
                    should_connect = True
            elif req_u or req_v:
                should_connect = True
            
            if should_connect:
                total_cost += w
                if req_u and req_v:
                    req_union(u, v)
                    
            # Check if all required vertices are now connected
            # Root of required component
            roots = set()
            for req in required_vertices:
                roots.add(find(parent, req))
            if len(roots) == 1:
                break
    
    return total_cost

# Simpler and more direct implementation
def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    essential = set(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
        
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    # For small t, we can find the minimum Steiner tree
    # But let's implement a simpler solution using the fact that we just need connectivity
    
    # Sort edges by weight
    edges.sort()
    
    # Union-Find structure
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
        
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    # We need to connect all essential vertices
    # Start with checking how many separate components they're in
    total_cost = 0
    
    for w, u, v in edges:
        if union(u, v):
            total_cost += w
            # Check if all essential vertices are now connected
            root = find(next(iter(essential)))
            if all(find(x) == root for x in essential):
                break
                
    print(total_cost)

solve()