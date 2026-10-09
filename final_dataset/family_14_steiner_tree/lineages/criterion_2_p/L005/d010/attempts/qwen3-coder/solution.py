import sys
from collections import defaultdict, deque

sys.setrecursionlimit(300000)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx+1])
    t = int(data[idx+2])
    idx += 3
    
    essential = list(map(int, data[idx:idx+t]))
    idx += t
    
    # If t <= 1, no pairs, so cost is 0
    if t <= 1:
        print(0)
        return
    
    # Build graph
    adj = [[] for _ in range(n+1)]
    edges = []
    edge_map = {}
    
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        w = int(data[idx+2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        edge_idx = len(edges)
        edges.append((u, v, w))
        edge_map[(u,v)] = edge_idx
        edge_map[(v,u)] = edge_idx
    
    # Root the tree at node 1 (or any node)
    parent = [-1] * (n+1)
    depth = [0] * (n+1)
    subtree_size = [1] * (n+1)
    visited = [False] * (n+1)
    
    # BFS to compute parent, depth, subtree sizes
    queue = deque([1])
    visited[1] = True
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                depth[v] = depth[u] + 1
                queue.append(v)
    
    # Compute subtree sizes
    order = []
    visited = [False] * (n+1)
    stack = [1]
    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            order.append(u)
            for v, w in adj[u]:
                if not visited[v] and v != parent[u]:
                    stack.append(v)
    
    for u in reversed(order):
        if parent[u] != -1:
            subtree_size[parent[u]] += subtree_size[u]
    
    # Count how many times each edge is used
    count = [0] * m
    essential_set = set(essential)
    
    # For each pair of essential nodes, we need the path between them
    # But since we want the union of all paths, we can use the fact that 
    # the number of paths going through an edge (u,v) where u is parent of v
    # is equal to the number of essential nodes in subtree of v multiplied 
    # by the number of essential nodes outside subtree of v
    
    # So for each node v (not root), the edge to its parent contributes:
    # (number of essential nodes in subtree of v) * (total essential - that)
    
    # First, mark which nodes are essential
    is_essential = [0] * (n+1)
    for node in essential:
        is_essential[node] = 1
        
    # Propagate counts up the tree using DFS
    # We'll compute for each node, how many essential nodes are in its subtree
    subtree_essential = [0] * (n+1)
    for u in reversed(order):
        subtree_essential[u] = is_essential[u]
        for v, w in adj[u]:
            if v != parent[u]:
                subtree_essential[u] += subtree_essential[v]
                
    # Now for each edge, calculate how many essential pairs use it
    total_essential = len(essential)
    result = 0
    
    # For each node v (except root), look at edge to parent
    for v in range(2, n+1):
        u = parent[v]  # u is parent of v
        # How many essential nodes in subtree of v?
        in_subtree = subtree_essential[v]
        # How many essential nodes outside subtree of v?
        out_subtree = total_essential - in_subtree
        # Number of pairs that use this edge
        num_pairs = in_subtree * out_subtree
        # Find the edge index
        edge_idx = edge_map.get((u, v), edge_map.get((v, u)))
        if edge_idx is not None:
            w = edges[edge_idx][2]
            result += num_pairs * w
            
    print(result)

if __name__ == "__main__":
    main()