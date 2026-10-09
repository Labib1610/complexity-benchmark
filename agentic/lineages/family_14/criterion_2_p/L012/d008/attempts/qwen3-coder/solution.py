import sys
from collections import defaultdict
import heapq

def find_root(parent, x):
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find_root(parent, x)
    root_y = find_root(parent, y)
    
    if root_x == root_y:
        return False
    
    if rank[root_x] < rank[root_y]:
        root_x, root_y = root_y, root_x
    
    parent[root_y] = root_x
    if rank[root_x] == rank[root_y]:
        rank[root_x] += 1
    return True

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx+1])
    t = int(data[idx+2])
    idx += 3
    
    target_dims = list(map(int, data[idx:idx+t]))
    idx += t
    
    # Convert to 0-indexed
    target_set = set(x - 1 for x in target_dims)
    
    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        w = int(data[idx+2])
        idx += 3
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    # Create a graph with only target nodes and find MST that connects all targets
    # We use a modified Kruskal's algorithm
    
    parent = list(range(n))
    rank = [0] * n
    
    # Sort edges by weight
    edges.sort()
    
    total_cost = 0
    connected_components = len(target_set)
    
    for weight, u, v in edges:
        # Check if this edge connects two different components
        root_u = find_root(parent, u)
        root_v = find_root(parent, v)
        
        if root_u != root_v:
            # Check if either u or v is a target node
            u_is_target = u in target_set
            v_is_target = v in target_set
            
            # Union the sets
            union(parent, rank, u, v)
            
            # If both were in different components and at least one was a target,
            # we might have connected two target components
            if u_is_target or v_is_target:
                new_root = find_root(parent, u)
                # Recalculate number of connected target components
                target_groups = {}
                for node in target_set:
                    root = find_root(parent, node)
                    if root not in target_groups:
                        target_groups[root] = []
                    target_groups[root].append(node)
                
                # If all targets are in one component, we're done
                if len(target_groups) == 1:
                    break
    
    # Better approach: create a complete graph between target nodes where edge weights
    # are the shortest path distances in the original graph
    # But that's expensive. Let's think differently.
    
    # The key insight: we want the minimum cost to connect all target dimensions
    # This is a Steiner tree problem, but we can solve it using the fact that 
    # we're looking for a subtree of the given tree that spans all targets
    
    # Since the given edges form a spanning tree of the complete graph (as they span the n-1 dim space)
    # we can use the fact that the minimum cost to connect all targets is the cost of the 
    # minimal subtree that contains all targets
    
    # Build adjacency list representation
    adj = [[] for _ in range(n)]
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Find the minimum subtree that spans all target nodes
    # This is essentially finding the Steiner tree, but we can do it efficiently
    # by running Kruskal's algorithm and stopping when all targets are connected
    
    parent = list(range(n))
    rank = [0] * n
    
    total_cost = 0
    edges.sort()
    
    # Count how many distinct components contain targets
    def count_target_components():
        components = {}
        for node in target_set:
            root = find_root(parent, node)
            components[root] = True
        return len(components)
    
    initial_components = count_target_components()
    
    for weight, u, v in edges:
        if union(parent, rank, u, v):
            total_cost += weight
            if count_target_components() == 1:
                break
                
    print(total_cost)

if __name__ == "__main__":
    main()