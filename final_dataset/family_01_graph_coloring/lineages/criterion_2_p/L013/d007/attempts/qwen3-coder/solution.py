import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        # No constraints, maximize confidence score by setting all to 1
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build graph
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # For each edge (u,v), the constraint is (p_u + p_v)/2 = 1.5 => p_u + p_v = 3
    # So p_u and p_v must be different (one 1, one 2)
    # This is equivalent to a 2-coloring problem (bipartite check)
    
    color = [0] * (n + 1)  # 0: unvisited, 1: color A, 2: color B
    
    # Check if bipartite and assign colors
    visited = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if not visited[i]:
            queue = deque()
            queue.append(i)
            color[i] = 1
            visited[i] = True
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        color[v] = 3 - color[u]  # Flip color (1->2, 2->1)
                        visited[v] = True
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    # Bipartition successful. color[i] is 1 or 2 for each node.
    # To maximize sum_{i in S} 1/i!, we want S to contain as many small indices as possible.
    # That means we prefer color 1 for smaller indices.
    # Strategy: 
    # For each connected component, decide whether to use (color=1 as tier 1) or (color=2 as tier 1)
    # based on which gives higher confidence score.
    
    # Group nodes by components using BFS/DFS again
    visited_comp = [False] * (n + 1)
    components = []
    
    for i in range(1, n + 1):
        if not visited_comp[i]:
            comp_nodes = []
            queue = deque([i])
            visited_comp[i] = True
            comp_nodes.append(i)
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if not visited_comp[v]:
                        visited_comp[v] = True
                        queue.append(v)
                        comp_nodes.append(v)
            components.append(comp_nodes)
    
    # For each component, compute score for both color mappings
    final_color = [0] * (n + 1)
    
    for comp in components:
        # Compute score if we take color 1 nodes as tier 1
        score1 = 0.0
        for node in comp:
            if color[node] == 1:
                if node <= 170:  # Prevent overflow
                    score1 += 1.0
                    for j in range(2, node+1):
                        score1 /= j
        
        # Compute score if we take color 2 nodes as tier 1
        score2 = 0.0
        for node in comp:
            if color[node] == 2:
                if node <= 170:
                    score2 += 1.0
                    for j in range(2, node+1):
                        score2 /= j
        
        # Decide mapping for this component
        if score1 >= score2:
            # color -> tier: 1->1, 2->2
            for node in comp:
                final_color[node] = color[node]
        else:
            # color -> tier: 1->2, 2->1
            for node in comp:
                final_color[node] = 3 - color[node]
    
    print("YES")
    print(" ".join(str(final_color[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    main()