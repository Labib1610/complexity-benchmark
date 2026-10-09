import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(10000)
    
    n, m = map(int, sys.stdin.readline().split())
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
        degree[u] += 1
        degree[v] += 1
    
    # Check if all degrees are equal
    d = degree[1]
    for i in range(1, n + 1):
        if degree[i] != d:
            print("NO")
            return
    
    # We need to edge-color the graph with d colors
    # This is equivalent to finding a proper edge coloring
    
    # Since m = 3*n/2 and each vertex has degree d, we have m = n*d/2
    # So 3*n/2 = n*d/2 => d = 3
    # So we're dealing with a 3-regular graph and need to 3-edge-color it
    
    # A 3-regular graph is 3-edge-colorable if and only if it's class 1
    # For 3-regular graphs, this is always possible if the graph has a perfect matching
    
    # Try to find a perfect matching first
    matched = [False] * (n + 1)
    matching = [-1] * (n + 1)
    edge_index = [-1] * m
    
    def dfs(u, visited):
        for v, idx in adj[u]:
            if v not in visited:
                visited.add(v)
                if matching[v] == -1 or dfs(matching[v], visited):
                    matching[v] = u
                    matching[u] = v
                    edge_index[idx] = 1  # First color for matching edges
                    return True
        return False
    
    # Find maximum matching
    match_count = 0
    for u in range(1, n + 1):
        if not matched[u]:
            visited = set()
            if dfs(u, visited):
                match_count += 1
                matched[u] = True
                for v, idx in adj[u]:
                    if matching[u] == v:
                        matched[v] = True
                        break
    
    # Check if it's a perfect matching
    if match_count * 2 != n:
        print("NO")
        return
    
    # Now we have colored all matching edges with color 1
    # Remaining edges form a 2-regular graph (union of cycles)
    # We can 2-color each cycle
    
    result = [0] * m
    for i in range(m):
        if edge_index[i] == 1:
            result[i] = 1
    
    # Build the graph without matching edges
    adj_rem = [[] for _ in range(n + 1)]
    rem_edges = []
    for i in range(m):
        u, v = edges[i]
        if edge_index[i] != 1:
            adj_rem[u].append((v, i))
            adj_rem[v].append((u, i))
            rem_edges.append(i)
    
    # Each component in adj_rem is a cycle (since it's 2-regular)
    visited_v = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if visited_v[start] or len(adj_rem[start]) == 0:
            continue
            
        # Find the cycle
        cycle_edges = []
        current = start
        prev = -1
        
        while True:
            visited_v[current] = True
            next_vertex = -1
            next_edge_idx = -1
            
            for v, idx in adj_rem[current]:
                if v != prev:
                    next_vertex = v
                    next_edge_idx = idx
                    break
            
            if next_vertex == -1:
                break
                
            cycle_edges.append(next_edge_idx)
            
            if next_vertex == start:
                break
                
            prev = current
            current = next_vertex
        
        # Color the cycle with 2 colors (2 and 3)
        for i in range(len(cycle_edges)):
            color = 2 if i % 2 == 0 else 3
            result[cycle_edges[i]] = color
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()