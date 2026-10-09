import sys
from collections import defaultdict, deque

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    return n, m, edges, adj

def isValidConfiguration(n, m, edges, adj):
    # Try to 3-color the line graph of the original graph
    # Each edge becomes a node in the line graph
    # Two nodes in line graph are connected if their corresponding edges share a vertex
    
    # But we can also think of this as orienting edges and assigning colors
    # We'll use a greedy approach with backtracking simulation
    
    # Since each vertex has degree 3, and we need each edge to get a unique color 
    # among the edges incident to each of its endpoints
    
    # This is equivalent to edge coloring with 3 colors where each vertex has degree 3
    # By Kőnig's theorem, since the graph is cubic (3-regular), it can be edge-colored with 3 colors iff it's bipartite
    # But that's not directly helpful here. Let's try a direct construction.
    
    # Actually, let's model this properly:
    # For each vertex, the 3 edges incident to it must have 3 different colors
    # So we're looking for a proper edge 3-coloring
    
    # Let's build the line graph and try to 3-color it
    # Nodes in line graph = edges in original graph
    # Edges in line graph connect if the original edges share a vertex
    
    line_adj = [[] for _ in range(m)]
    edge_index = {}
    for i, (u, v) in enumerate(edges):
        edge_index[(u, v)] = i
        edge_index[(v, u)] = i
        
    # Build adjacency in line graph
    for i, (u, v) in enumerate(edges):
        # Find all edges adjacent to u and v
        for w in adj[u]:
            if w != v:
                j = edge_index.get((u, w), edge_index.get((w, u)))
                if i != j and j is not None:
                    if j not in line_adj[i]:
                        line_adj[i].append(j)
        for w in adj[v]:
            if w != u:
                j = edge_index.get((u, w), edge_index.get((w, u)))
                if i != j and j is not None:
                    if j not in line_adj[i]:
                        line_adj[i].append(j)
                        
    # Now we need to 3-color the line graph
    # Use a greedy approach with ordering
    colors = [0] * m  # 0 means uncolored
    
    # Order vertices by decreasing degree in line graph for better performance
    order = list(range(m))
    order.sort(key=lambda x: len(line_adj[x]), reverse=True)
    
    def is_safe(node, color):
        for neighbor in line_adj[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def solve(node_index):
        if node_index == m:
            return True
            
        node = order[node_index]
        for color in [1, 2, 3]:
            if is_safe(node, color):
                colors[node] = color
                if solve(node_index + 1):
                    return True
                colors[node] = 0
        return False
    
    # For large graphs, this might be too slow. Let's check if there's a structural property.
    # Actually, let's just try the greedy approach first with a good ordering
    
    # Alternative: since the graph is 3-regular, if it's class 1 (edge chromatic number = 3),
    # then it has a proper 3-edge coloring.
    
    # Let's try a different approach - build the coloring incrementally
    result = [0] * m
    
    # For each vertex, we need to assign 3 different colors to its 3 edges
    # Let's process vertices one by one and extend the partial coloring
    
    # Use a SAT-like approach or constraint satisfaction would work but might be overkill
    # Let's stick to backtracking with good heuristics
    
    # Re-index edges for each vertex
    vertex_edges = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        vertex_edges[u].append(i)
        vertex_edges[v].append(i)
        
    colored = [False] * m
    
    def conflict(e1, e2):
        # Check if assigning colors to these edges conflicts
        return result[e1] != 0 and result[e2] != 0 and result[e1] == result[e2]
        
    def is_valid_partial():
        # Check current partial assignment for conflicts
        for i in range(m):
            if result[i] == 0:
                continue
            for j in line_adj[i]:
                if result[j] != 0 and result[i] == result[j] and i < j:
                    return False
        return True
    
    def backtrack(edge_idx):
        if edge_idx == m:
            return True
            
        # Pick next edge based on how constrained it is
        # For now, just go in order
        # Better: pick the edge that shares vertices with most already-colored edges
        
        e_idx = edge_idx  # Could optimize this choice
        u, v = edges[e_idx]
        
        used_colors_u = set()
        used_colors_v = set()
        
        for e_j in vertex_edges[u]:
            if colored[e_j] and e_j != e_idx:
                used_colors_u.add(result[e_j])
                
        for e_j in vertex_edges[v]:
            if colored[e_j] and e_j != e_idx:
                used_colors_v.add(result[e_j])
                
        forbidden = used_colors_u | used_colors_v
        
        for color in [1, 2, 3]:
            if color not in forbidden:
                result[e_idx] = color
                colored[e_idx] = True
                if is_valid_partial() and backtrack(edge_idx + 1):
                    return True
                result[e_idx] = 0
                colored[e_idx] = False
                
        return False
    
    # Sort edges to try to make the search faster
    # Put edges whose endpoints have more colored edges first
    def edge_priority(idx):
        u, v = edges[idx]
        count = 0
        for e_j in vertex_edges[u] + vertex_edges[v]:
            if colored[e_j]:
                count += 1
        return -count  # Negative for descending sort
    
    # Try iterative deepening or just simple backtracking
    if backtrack(0):
        return True, result
    else:
        return False, []

def main():
    n, m, edges, adj = read_input()
    possible, coloring = isValidConfiguration(n, m, edges, adj)
    
    if possible:
        print("YES")
        print(' '.join(map(str, coloring)))
    else:
        print("NO")

if __name__ == "__main__":
    main()