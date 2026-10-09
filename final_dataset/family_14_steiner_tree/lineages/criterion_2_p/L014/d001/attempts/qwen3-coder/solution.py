import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    required = set(map(int, sys.stdin.readline().split()))
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    # Sort edges by weight
    edges.sort()
    
    # Union-Find data structure
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
    
    # Kruskal's algorithm
    total_cost = 0
    connected_required = 0
    
    for w, u, v in edges:
        if union(u, v):
            total_cost += w
            # Check if both u and v are required and were in different components
            pu, pv = find(u), find(v)
            # We need to check if this edge connects required nodes
            # A better approach: count how many required nodes are connected
            
    # Actually, we need to run Kruskal until all required nodes are in the same component
    # Reset Union-Find
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
    
    # Count how many required nodes are in each component
    required_in_component = {}
    for r in required:
        required_in_component[r] = 1
    
    total_cost = 0
    components_with_required = len(required)
    
    for w, u, v in edges:
        pu, pv = find(u), find(v)
        if pu != pv:
            # Union the components
            # Update the count of required nodes in the new component
            req_u = required_in_component.get(pu, 0)
            req_v = required_in_component.get(pv, 0)
            
            # Perform union
            if rank[pu] < rank[pv]:
                pu, pv = pv, pu
            parent[pv] = pu
            if rank[pu] == rank[pv]:
                rank[pu] += 1
                
            # Update required count in the component
            required_in_component[pu] = req_u + req_v
            if pv in required_in_component:
                del required_in_component[pv]
                
            total_cost += w
            
            # If all required nodes are in one component, we're done
            if required_in_component[pu] == t:
                break
    
    print(total_cost)

threading.Thread(target=main).start()