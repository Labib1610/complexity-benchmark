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
    
    if t <= 1:
        print(0)
        return
    
    priority = list(map(int, data[idx:idx+t]))
    idx += t
    
    # Convert to 0-indexed for convenience
    priority_set = set(x - 1 for x in priority)
    
    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((w, u, v))
    
    # Sort edges by weight
    edges.sort()
    
    # Initialize Union-Find
    parent = list(range(n))
    rank = [0] * n
    
    total_cost = 0
    connected_components = t
    
    for w, u, v in edges:
        # Check if u and v are in different components
        if find(parent, u) != find(parent, v):
            # Check if either u or v is a priority node
            u_is_priority = u in priority_set
            v_is_priority = v in priority_set
            
            # If both are priority nodes, we definitely want to connect them
            if u_is_priority and v_is_priority:
                if union(parent, rank, u, v):
                    total_cost += w
                    connected_components -= 1
                    if connected_components == 1:
                        break
            # If exactly one is priority, we also want to connect
            elif u_is_priority or v_is_priority:
                if union(parent, rank, u, v):
                    total_cost += w
                    # We don't decrement connected_components here because 
                    # we're connecting a priority node to a non-priority component
            # If neither is priority, we still might want to connect if it helps connect priority nodes
            else:
                if union(parent, rank, u, v):
                    total_cost += w
    
    # Now we need to make sure all priority nodes are connected
    # We'll do another pass to connect any remaining disconnected priority components
    for w, u, v in edges:
        if find(parent, u) != find(parent, v):
            u_priority_component = any(find(parent, p) == find(parent, u) for p in priority_set)
            v_priority_component = any(find(parent, p) == find(parent, v) for p in priority_set)
            
            # If both components contain priority nodes, connect them
            if u_priority_component and v_priority_component:
                if union(parent, rank, u, v):
                    total_cost += w
                    connected_components -= 1
                    if connected_components == 1:
                        break
    
    print(total_cost)

if __name__ == "__main__":
    main()