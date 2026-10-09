def solve():
    import sys
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n
    
    # Try 2-coloring first (bipartite check)
    def try_bipartite(start):
        from collections import deque
        queue = deque([start])
        color[start] = 1
        component = [start]
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - color[u]
                    queue.append(v)
                    component.append(v)
                elif color[v] == color[u]:
                    return None
        return component
    
    # 3-coloring with backtracking
    def backtrack(vertices, idx):
        if idx == len(vertices):
            return True
        u = vertices[idx]
        used = set()
        for v in adj[u]:
            if color[v] != 0:
                used.add(color[v])
        for c in [1, 2, 3]:
            if c not in used:
                color[u] = c
                if backtrack(vertices, idx + 1):
                    return True
                color[u] = 0
        return False
    
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            # Find component
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
            
            # Reset colors for this component
            for u in comp:
                color[u] = 0
            
            # Try bipartite first
            result = try_bipartite(i)
            if result is None:
                # Reset and try 3-coloring
                for u in comp:
                    color[u] = 0
                # Order by degree descending
                comp_sorted = sorted(comp, key=lambda x: -len(adj[x]))
                if not backtrack(comp_sorted, 0):
                    print("NO")
                    return
    
    print("YES")
    print(' '.join(map(str, color)))

solve()