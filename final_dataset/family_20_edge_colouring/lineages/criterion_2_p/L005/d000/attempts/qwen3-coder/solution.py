import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    nL, nR, m = map(int, sys.stdin.readline().split())
    
    # Build graph: vertices are people (drivers and inspectors)
    # Edges are drives
    adj = defaultdict(list)
    edges = []
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        # Convert to 0-based indexing
        u -= 1
        v -= 1
        # Inspector indices offset by nL
        v += nL
        adj[u].append((v, i))
        adj[v].append((u, i))
        edges.append((u, v))
    
    # Find maximum degree
    max_degree = 0
    for node in adj:
        max_degree = max(max_degree, len(adj[node]))
    
    if max_degree == 0:
        print("YES")
        return
    
    # Color the edges with max_degree colors using BFS for each component
    color = [0] * m  # Colors are 1-indexed
    
    visited_nodes = [False] * (nL + nR)
    
    for start_node in range(nL + nR):
        if visited_nodes[start_node] or not adj[start_node]:
            continue
            
        # BFS to find the component
        component_edges = []
        queue = deque()
        queue.append(start_node)
        visited_nodes[start_node] = True
        local_nodes = {start_node}
        
        while queue:
            node = queue.popleft()
            for neighbor, edge_idx in adj[node]:
                component_edges.append(edge_idx)
                if not visited_nodes[neighbor]:
                    visited_nodes[neighbor] = True
                    queue.append(neighbor)
                    local_nodes.add(neighbor)
        
        # For this component, assign colors to edges
        # We'll do a greedy edge coloring based on node degrees
        
        # For bipartite graphs, we can do a proper edge coloring with Δ colors
        # We simulate this by going through nodes and assigning unused colors
        
        used_colors_on_node = [set() for _ in range(nL + nR)]
        
        for edge_idx in component_edges:
            u, v = edges[edge_idx]
            # Find a color not used by either u or v
            used = used_colors_on_node[u] | used_colors_on_node[v]
            c = 1
            while c in used:
                c += 1
            color[edge_idx] = c
            used_colors_on_node[u].add(c)
            used_colors_on_node[v].add(c)
    
    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    main()