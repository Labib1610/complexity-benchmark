import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)
    
    # Check if graph is bipartite
    color = [-1] * n
    is_bipartite = True
    for i in range(n):
        if color[i] == -1:
            stack = [i]
            color[i] = 0
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
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
    
    # Find connected components
    visited = [False] * n
    components = []
    for i in range(n):
        if not visited[i]:
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
            components.append(comp)
    
    # For each component, find the lexicographically smallest assignment
    # Component can be colored with 2 colors (1,2) or (1,3) or (2,3)
    # We need to pick the one that gives smallest overall sequence
    
    # For each component, precompute which color pair gives smaller result
    # color_pair options: (1,2), (1,3), (2,3)
    color_pairs = [(1, 2), (1, 3), (2, 3)]
    
    # For each component, compute the assignment for each color pair
    comp_assignments = []
    for comp in components:
        assignments = []
        for pair in color_pairs:
            # BFS to assign colors
            local_color = {}
            start = comp[0]
            local_color[start] = pair[0]
            queue = [start]
            idx = 0
            valid = True
            while idx < len(queue):
                u = queue[idx]
                idx += 1
                for v in adj[u]:
                    if v not in local_color:
                        # v should have opposite color from u
                        if local_color[u] == pair[0]:
                            local_color[v] = pair[1]
                        else:
                            local_color[v] = pair[0]
                        queue.append(v)
                    else:
                        # Check consistency
                        if local_color[u] == local_color[v]:
                            valid = False
                            break
                if not valid:
                    break
            if valid:
                assign = [0] * n
                for node in comp:
                    assign[node] = local_color[node]
                assignments.append(assign)
        comp_assignments.append(assignments)
    
    # DP to find lexicographically smallest combination
    num_comp = len(components)
    # dp[i] = best assignment for first i components (as tuple), or None if impossible
    best = [None] * (num_comp + 1)
    best[0] = tuple()
    
    for i in range(num_comp):
        if best[i] is None:
            continue
        for assign in comp_assignments[i]:
            new_assign = best[i] + tuple(assign[j] for j in range(n) if assign[j] != 0)
            if best[i+1] is None or new_assign < best[i+1]:
                best[i+1] = new_assign
    
    if best[num_comp] is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, best[num_comp])))

solve()