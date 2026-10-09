import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    nL, nR, m = map(int, sys.stdin.readline().split())
    
    # We will build a graph where each port is a node and edges represent cables
    # Left ports: 0 to nL-1
    # Right ports: nL to nL + nR - 1
    adj = defaultdict(list)
    edges = []
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        v += nL
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Find maximum degree
    max_degree = 0
    for i in range(nL + nR):
        max_degree = max(max_degree, len(adj[i]))
    
    if max_degree == 0:
        print("YES")
        return
    
    # Color the edges such that no two edges incident to the same vertex have the same color
    # This is edge coloring, and since the graph is bipartite, we can do it with Δ colors
    # We use a greedy algorithm with BFS for each connected component
    
    result = [-1] * m
    used_colors = [set() for _ in range(nL + nR)]
    
    # For each connected component
    visited = [False] * (nL + nR)
    
    for start in range(nL + nR):
        if visited[start] or not adj[start]:
            continue
            
        # BFS to traverse the component
        queue = deque([start])
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            
            # For each edge from u
            for v, edge_idx in adj[u]:
                if result[edge_idx] != -1:
                    continue
                    
                # Find a color not used by u or v
                color = 1
                while color in used_colors[u] or color in used_colors[v]:
                    color += 1
                
                result[edge_idx] = color
                used_colors[u].add(color)
                used_colors[v].add(color)
                
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()