import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        t = int(next(iterator))
    except StopIteration:
        return
    
    critical = []
    for _ in range(t):
        critical.append(int(next(iterator)))
    
    edges = []
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        edges.append((u, v, w))
    
    # Special case: t <= 1, no edges needed to connect critical elements
    if t <= 1:
        print(0)
        return
    
    # Build adjacency list for the tree
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # BFS to find parent, depth, and max edge weight to parent for each node
    parent = [0] * (n + 1)
    parent_edge_weight = [0] * (n + 1)
    depth = [0] * (n + 1)
    
    # Start BFS from node 1 (arbitrary root)
    queue = [1]
    parent[1] = 0
    depth[1] = 0
    
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_edge_weight[v] = w
                depth[v] = depth[u] + 1
                queue.append(v)
    
    # Function to find LCA and max edge weight on path
    def get_max_on_path(u, v):
        max_w = 0
        # Bring u and v to same depth
        while depth[u] > depth[v]:
            max_w = max(max_w, parent_edge_weight[u])
            u = parent[u]
        while depth[v] > depth[u]:
            max_w = max(max_w, parent_edge_weight[v])
            v = parent[v]
        # Now u and v at same depth, move up together
        while u != v:
            max_w = max(max_w, parent_edge_weight[u])
            max_w = max(max_w, parent_edge_weight[v])
            u = parent[u]
            v = parent[v]
        return max_w
    
    # Sort critical elements to process in order
    critical.sort()
    
    total_cost = 0
    for i in range(len(critical) - 1):
        u = critical[i]
        v = critical[i + 1]
        total_cost += get_max_on_path(u, v)
    
    print(total_cost)

if __name__ == "__main__":
    solve()