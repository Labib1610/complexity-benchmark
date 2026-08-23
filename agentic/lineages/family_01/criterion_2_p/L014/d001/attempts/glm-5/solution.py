import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    possible = True
    
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        # Try to color this component with start as 1
        color[start] = 1
        stack = [start]
        ok = True
        while stack:
            u = stack.pop()
            cu = color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - cu
                    stack.append(v)
                elif color[v] == cu:
                    ok = False
        if not ok:
            possible = False
            break
    
    if not possible:
        sys.stdout.write("NO\n")
        return
    
    # Now we have a valid coloring. We need the lexicographically smallest.
    # For each component, we can flip colors. We want as many leading 1's as possible.
    # Process components in order of their first vertex.
    visited = [False] * (n + 1)
    comp_first = []
    comp_vertices = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            comp_first.append(i)
            comp = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            comp_vertices.append(comp)
    
    # For each component, decide orientation.
    # We want the first vertex of the component to be 1 if possible.
    # Since color[i] is already 1 for the first vertex of each component (by our BFS/DFS above),
    # we just need to check if flipping would make it 1. But it's already 1.
    # Wait, the initial coloring already set color[start]=1 for each component's first vertex.
    # So the current coloring is already the lexicographically smallest? 
    # Let's verify: for each component, the first vertex (smallest index in that component) is colored 1.
    # Any valid coloring of the component must assign either 1 or 2 to this first vertex.
    # To make the sequence lexicographically smallest, we want this first vertex to be 1.
    # Since our coloring already does that, and the rest of the component is determined by this choice,
    # our coloring is optimal for each component.
    # But wait: the first vertex of a component might not be the globally smallest uncolored vertex
    # at the time we process it. Actually, we process vertices in order 1..n, so the first vertex
    # of each component IS the smallest vertex in that component. And we set it to 1.
    # So yes, this is lexicographically smallest.
    
    # However, there's a subtlety: what if a component's first vertex is already forced to be 2
    # by some previous component? No, components are independent.
    
    # Actually, let me double-check. The initial coloring sets color[start]=1 for the smallest
    # vertex in each component. This is exactly what we want for lexicographically smallest.
    
    result = [str(color[i]) for i in range(1, n + 1)]
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(result) + "\n")

solve()