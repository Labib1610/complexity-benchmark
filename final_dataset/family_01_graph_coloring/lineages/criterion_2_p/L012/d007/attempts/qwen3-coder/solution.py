import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = [[] for _ in range(n+1)]
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        if u != v:
            edges.append((u, v))
            adj[u].append(v)
            adj[v].append(u)
    
    # If no edges, we can just assign all 1s
    if m == 0:
        print("YES")
        print(' '.join(['1']*n))
        return
    
    # For each edge (u,v), the perimeter condition is:
    # 2*|u-v| + 2*|h_u - h_v| = 2*|u-v| + 2
    # This simplifies to |h_u - h_v| = 1
    # Since h_u, h_v ∈ {1,2}, this means h_u ≠ h_v
    
    # So we need to 2-color the graph where each edge enforces that endpoints have different colors
    # Color 1 represents h=1, Color 2 represents h=2 (or vice versa, but we'll fix the first node to minimize)
    
    color = [0] * (n+1)  # 0 means unvisited, 1 and 2 are the two colors
    
    # Check each connected component
    visited = [False] * (n+1)
    
    for start in range(1, n+1):
        if visited[start] or not adj[start]:
            continue
        # BFS to check bipartiteness and assign colors
        queue = deque()
        queue.append(start)
        color[start] = 1
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            c_u = color[u]
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = 3 - c_u  # flips 1->2, 2->1
                    queue.append(v)
                else:
                    if color[v] == c_u:
                        print("NO")
                        return
    
    # Now we need to assign heights. We want the lexicographically smallest sequence in base 3.
    # That means we prefer h_i = 1 over h_i = 2.
    # So among the two colors, we should map the one that gives smaller lex sequence to 1.
    
    # For each component, we can choose which color maps to 1.
    # To get minimum lex sequence, for each component, 
    # we see what happens if we map color 1 to h=1 vs h=2 for the first node in that component,
    # and pick the one that gives smaller lex.
    
    # Actually simpler approach:
    # For each connected component, we have two valid colorings (swap colors).
    # We try both and see which gives smaller lex sequence.
    
    # Let's build components
    visited_comp = [False] * (n+1)
    components = []
    
    for i in range(1, n+1):
        if visited_comp[i]:
            continue
        if not adj[i]:
            continue
        # BFS to get component
        comp = []
        queue = deque()
        queue.append(i)
        visited_comp[i] = True
        comp.append(i)
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited_comp[v]:
                    visited_comp[v] = True
                    queue.append(v)
                    comp.append(v)
        components.append(comp)
    
    # For isolated nodes (not in any edge), we can set h=1
    h = [1] * (n+1)
    
    # Process each component
    for comp in components:
        # Try mapping color[comp[0]] to 1 and 2, see which gives better lex
        c0 = color[comp[0]]
        
        # Option 1: color c0 -> 1, color (3-c0) -> 2
        h1 = [0] * (n+1)
        for u in comp:
            if color[u] == c0:
                h1[u] = 1
            else:
                h1[u] = 2
                
        # Option 2: color c0 -> 2, color (3-c0) -> 1
        h2 = [0] * (n+1)
        for u in comp:
            if color[u] == c0:
                h2[u] = 2
            else:
                h2[u] = 1
        
        # Compare h1 and h2 for this component
        # We compare the sequences restricted to indices in comp
        use_h1 = True
        for u in sorted(comp):
            if h1[u] < h2[u]:
                use_h1 = True
                break
            elif h1[u] > h2[u]:
                use_h1 = False
                break
        # If equal, doesn't matter, use h1
        
        chosen_h = h1 if use_h1 else h2
        for u in comp:
            h[u] = chosen_h[u]
            
    # Isolated nodes (not part of any component) can remain 1
    # But actually, they might be part of the graph but just degree 0.
    # Let's make sure all nodes are assigned
    for i in range(1, n+1):
        if h[i] == 0:  # Not assigned yet, meaning it's isolated
            h[i] = 1
            
    print("YES")
    print(' '.join(map(str, h[1:])))

if __name__ == "__main__":
    main()