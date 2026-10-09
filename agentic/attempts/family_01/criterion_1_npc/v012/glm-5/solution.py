import sys
sys.setrecursionlimit(100000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n
    
    # Check if graph is bipartite and color components
    is_bipartite = True
    for i in range(n):
        if color[i] == 0:
            color[i] = 1
            stack = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break
    
    if not is_bipartite:
        print("NO")
        return
    
    # Group vertices by their bipartite color within each connected component
    comp_id = [-1] * n
    components = []
    for i in range(n):
        if comp_id[i] == -1:
            comp_id[i] = len(components)
            queue = [i]
            comp_vertices = [i]
            for u in queue:
                for v in adj[u]:
                    if comp_id[v] == -1:
                        comp_id[v] = comp_id[i]
                        queue.append(v)
                        comp_vertices.append(v)
            components.append(comp_vertices)
    
    num_components = len(components)
    comp_sizes = [[0, 0] for _ in range(num_components)]
    
    for idx, comp in enumerate(components):
        for u in comp:
            if color[u] == 1:
                comp_sizes[idx][0] += 1
            else:
                comp_sizes[idx][1] += 1
    
    # DP to find subset of components with total size n/3
    target = n // 3
    dp = [[False] * (target + 1) for _ in range(num_components + 1)]
    dp[0][0] = True
    
    for i in range(num_components):
        for j in range(target + 1):
            if dp[i][j]:
                if j + comp_sizes[i][0] <= target:
                    dp[i+1][j + comp_sizes[i][0]] = True
                if j + comp_sizes[i][1] <= target:
                    dp[i+1][j + comp_sizes[i][1]] = True
    
    if not dp[num_components][target]:
        print("NO")
        return
    
    # Backtrack to find which components are in set A
    in_set_a = [False] * num_components
    j = target
    for i in range(num_components, 0, -1):
        if j - comp_sizes[i-1][0] >= 0 and dp[i-1][j - comp_sizes[i-1][0]]:
            in_set_a[i-1] = True
            j -= comp_sizes[i-1][0]
        else:
            in_set_a[i-1] = False
            j -= comp_sizes[i-1][1]
    
    # Assign final colors
    final_color = [0] * n
    for idx, comp in enumerate(components):
        for u in comp:
            if in_set_a[idx]:
                final_color[u] = 1 if color[u] == 1 else 2
            else:
                final_color[u] = 2 if color[u] == 1 else 3
    
    print("YES")
    print(' '.join(map(str, final_color)))

solve()