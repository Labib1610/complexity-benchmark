import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * n for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u][v] = True
        adj[v][u] = True
    
    # Build complement graph (edges where nodes can have same color)
    comp_adj = [[True] * n for _ in range(n)]
    for i in range(n):
        comp_adj[i][i] = False
    for i in range(n):
        for j in range(i + 1, n):
            if adj[i][j]:
                comp_adj[i][j] = False
                comp_adj[j][i] = False
    
    # Find connected components in complement graph
    visited = [False] * n
    components = []
    
    for start in range(n):
        if not visited[start]:
            stack = [start]
            visited[start] = True
            comp = []
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in range(n):
                    if comp_adj[u][v] and not visited[v]:
                        visited[v] = True
                        stack.append(v)
            components.append(comp)
    
    # Check if any component has more than 3 nodes
    for comp in components:
        if len(comp) > 3:
            print("NO")
            return
    
    # Check if any two components of size 3 are connected in original graph
    size3_comps = [comp for comp in components if len(comp) == 3]
    for i in range(len(size3_comps)):
        for j in range(i + 1, len(size3_comps)):
            for u in size3_comps[i]:
                for v in size3_comps[j]:
                    if adj[u][v]:
                        print("NO")
                        return
    
    # Valid assignment exists
    colors = [0] * n
    color = 1
    for comp in components:
        for u in comp:
            colors[u] = color
        color += 1
    
    print("YES")
    print(" ".join(map(str, colors)))

solve()