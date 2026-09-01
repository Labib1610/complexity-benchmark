import sys
from collections import defaultdict, deque

def compute_stress(cu, cv):
    return cu**3 + cv**3 + 7*(cu**2 + cv**2) + 2*(cu + cv) - 20*cu*cv

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # Precompute stress values
    S = {}
    for cu in [1, 2]:
        for cv in [1, 2]:
            S[(cu, cv)] = compute_stress(cu, cv)
    
    # Target total stress
    target = 10 * m
    
    # If no edges, any assignment works, choose all 1s for lex smallest
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Check if the graph is bipartite and find a valid 2-coloring
    color = [-1] * (n + 1)
    visited = [False] * (n + 1)
    
    # Try both colorings for each connected component
    components = []
    for i in range(1, n + 1):
        if not visited[i] and adj[i]:
            # BFS to get component
            comp_nodes = []
            queue = deque()
            queue.append(i)
            visited[i] = True
            comp_nodes.append(i)
            while queue:
                node = queue.popleft()
                for nei in adj[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        comp_nodes.append(nei)
                        queue.append(nei)
            components.append(comp_nodes)
    
    # For each component, try both colorings
    # Color 0 and 1
    best_coloring = {}
    
    for comp in components:
        # Try coloring the first node with 0
        color_local = {}
        queue = deque()
        start = comp[0]
        color_local[start] = 0
        queue.append(start)
        valid = True
        while queue and valid:
            node = queue.popleft()
            for nei in adj[node]:
                if nei in color_local:
                    if color_local[nei] == color_local[node]:
                        valid = False
                        break
                else:
                    color_local[nei] = 1 - color_local[node]
                    queue.append(nei)
        
        if not valid:
            print("NO")
            return
        
        # Now we have a valid 2-coloring in color_local
        # Try both assignments: (0->1, 1->2) and (0->2, 1->1)
        c1 = [1, 2]
        c2 = [2, 1]
        
        # Compute stress for first assignment
        stress1 = 0
        for u, v in edges:
            if u in color_local and v in color_local:
                cu = c1[color_local[u]]
                cv = c1[color_local[v]]
                stress1 += S[(cu, cv)]
        
        # Compute stress for second assignment
        stress2 = 0
        for u, v in edges:
            if u in color_local and v in color_local:
                cu = c2[color_local[u]]
                cv = c2[color_local[v]]
                stress2 += S[(cu, cv)]
        
        chosen = None
        if stress1 == target:
            chosen = c1
        elif stress2 == target:
            chosen = c2
        else:
            print("NO")
            return
            
        for node in comp:
            best_coloring[node] = chosen[color_local[node]]
    
    # For isolated nodes (not in any edge), assign 1 (for lex smallest)
    for i in range(1, n + 1):
        if i not in best_coloring:
            best_coloring[i] = 1
    
    # Build result in order
    result = []
    for i in range(1, n + 1):
        result.append(str(best_coloring[i]))
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()