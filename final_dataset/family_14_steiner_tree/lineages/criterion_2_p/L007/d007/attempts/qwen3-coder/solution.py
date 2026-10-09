import sys
from collections import defaultdict
import heapq

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

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    T = list(map(int, data[idx:idx+t]))
    idx += t
    
    # Convert to 0-indexed
    target_set = set(x-1 for x in T)
    
    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((w, u, v))
    
    # If t <= 1, we need no transpositions
    if t <= 1:
        print(0)
        return
    
    # Sort edges by weight
    edges.sort()
    
    # We need to connect all nodes in T
    # This is essentially finding the minimum spanning tree that connects all nodes in T
    # We can use a modified Kruskal's algorithm
    
    parent = list(range(n))
    rank = [0] * n
    
    total_cost = 0
    connected_components = len(target_set)
    
    for weight, u, v in edges:
        # Check if this edge connects two different components
        pu = find(parent, u)
        pv = find(parent, v)
        
        if pu != pv:
            # Check if either u or v is in target_set
            u_in_target = u in target_set
            v_in_target = v in target_set
            
            # Union the components
            union(parent, rank, u, v)
            
            # If both u and v were in target_set and they were in different components,
            # we've connected two target nodes
            if u_in_target and v_in_target and pu != pv:
                connected_components -= 1
                if connected_components == 1:
                    # All target nodes are connected
                    break
            
            # If exactly one of u or v is in target_set, 
            # and the other component contains target nodes,
            # we might have connected more target nodes
            elif (u_in_target or v_in_target) and pu != pv:
                # Check if the merged component now contains more target nodes
                # This is a bit tricky, but since we're building a tree,
                # each union either connects a new target node or not
                pass
            
            total_cost += weight
    
    print(total_cost)

if __name__ == "__main__":
    main()