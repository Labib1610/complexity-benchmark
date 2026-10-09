import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
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
    
    def dfs(u, c):
        color[u] = c
        for v in adj[u]:
            if color[v] == 0:
                if not dfs(v, 3 - c):
                    return False
            elif color[v] == c:
                return False
        return True
    
    for i in range(n):
        if color[i] == 0:
            if not dfs(i, 1):
                print("NO")
                return
    
    # Group vertices by their bipartite component
    comp_id = [-1] * n
    comp_vertices = []
    current_comp = 0
    for i in range(n):
        if comp_id[i] == -1:
            comp_vertices.append([])
            stack = [i]
            comp_id[i] = current_comp
            while stack:
                u = stack.pop()
                comp_vertices[current_comp].append(u)
                for v in adj[u]:
                    if comp_id[v] == -1:
                        comp_id[v] = current_comp
                        stack.append(v)
            current_comp += 1
    
    num_comps = len(comp_vertices)
    # For each component, compute size of each bipartition
    comp_size = []
    for comp in comp_vertices:
        cnt1 = sum(1 for u in comp if color[u] == 1)
        cnt2 = len(comp) - cnt1
        comp_size.append((cnt1, cnt2))
    
    # DP to find subset of components with total size n/3
    target = n // 3
    # dp[i][j] = True if we can achieve sum j using first i components
    # parent[i][j] = choice: 0 (use cnt1), 1 (use cnt2), -1 (not reached)
    dp = [[False] * (target + 1) for _ in range(num_comps + 1)]
    parent = [[-1] * (target + 1) for _ in range(num_comps + 1)]
    dp[0][0] = True
    
    for i in range(num_comps):
        cnt1, cnt2 = comp_size[i]
        for j in range(target + 1):
            if dp[i][j]:
                if j + cnt1 <= target:
                    dp[i+1][j+cnt1] = True
                    parent[i+1][j+cnt1] = 0
                if j + cnt2 <= target:
                    dp[i+1][j+cnt2] = True
                    parent[i+1][j+cnt2] = 1
    
    if not dp[num_comps][target]:
        print("NO")
        return
    
    # Reconstruct choices
    choice = [0] * num_comps
    j = target
    for i in range(num_comps, 0, -1):
        ch = parent[i][j]
        choice[i-1] = ch
        cnt1, cnt2 = comp_size[i-1]
        if ch == 0:
            j -= cnt1
        else:
            j -= cnt2
    
    # Assign colors
    result = [0] * n
    for i in range(num_comps):
        cnt1, cnt2 = comp_size[i]
        for u in comp_vertices[i]:
            if color[u] == 1:
                # This vertex is in partition 1 of its component
                if choice[i] == 0:
                    result[u] = 1
                else:
                    result[u] = 2
            else:
                # This vertex is in partition 2 of its component
                if choice[i] == 0:
                    result[u] = 2
                else:
                    result[u] = 1
    
    # Remaining vertices get color 3
    for i in range(n):
        if result[i] == 0:
            result[i] = 3
    
    print("YES")
    print(' '.join(map(str, result)))

solve()