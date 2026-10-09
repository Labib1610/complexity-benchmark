import sys
from collections import defaultdict, deque

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find_parent(parent, x), find_parent(parent, y)
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
    
    mandated = set()
    for _ in range(t):
        mandated.add(int(data[idx]))
        idx += 1
    
    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((w, u, v))
    
    # Sort edges by weight in descending order for Kruskal's algorithm variant
    edges.sort(reverse=True)
    
    # We want to find the maximum spanning forest that keeps mandated nodes connected
    # This is equivalent to finding the maximum weight edges we can remove
    # So we find the minimal cost to keep mandated nodes connected
    
    # Build the graph
    graph = defaultdict(list)
    for w, u, v in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Find connected components using Union-Find
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # First, connect all mandated nodes with zero-cost edges to a dummy node 0
    dummy_edges = []
    for node in mandated:
        dummy_edges.append((0, node, 0))
    
    # Combine real edges and dummy edges
    all_edges = edges + dummy_edges
    all_edges.sort()  # Sort by weight ascending for standard MST
    
    # Apply Kruskal's algorithm to find the minimum spanning tree
    total_cost = 0
    edges_in_mst = 0
    
    for w, u, v in all_edges:
        if union(parent, rank, u, v):
            total_cost += w
            edges_in_mst += 1
            if edges_in_mst == n:  # Since we have n+1 nodes (including dummy)
                break
    
    # The answer is the total cost of edges not in the MST
    sum_all_weights = sum(w for w, _, _ in edges)
    result = sum_all_weights - total_cost
    print(result)

if __name__ == "__main__":
    main()