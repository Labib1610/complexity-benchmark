import sys
sys.setrecursionlimit(10000)

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
    best_solution = None
    
    adjSets = [set(nei) for nei in adj]
    
    def dfs(pos):
        nonlocal best_solution
        if best_solution is not None:
            return
        if pos == n:
            best_solution = color[:]
            return
        if color[pos] != 0:
            dfs(pos + 1)
            return
        neigh = adjSets[pos]
        used_colors = set()
        for nei in adj[pos]:
            if color[nei] != 0:
                used_colors.add(color[nei])
        for c in (1, 2, 3):
            if c not in used_colors:
                color[pos] = c
                dfs(pos + 1)
                if best_solution is not None:
                    return
        color[pos] = 0
        return
    
    def can_color_component(start):
        q = [start]
        comp = []
        visited_in_bfs = {start}
        while q:
            u = q.pop()
            comp.append(u)
            for v in adj[u]:
                if v not in visited_in_bfs:
                    visited_in_bfs.add(v)
                    q.append(v)
        sub_adj = {}
        for u in comp:
            sub_adj[u] = [v for v in adj[u] if v in visited_in_bfs]
        degs = [(len(sub_adj[u]), u) for u in comp]
        degs.sort(reverse=True)
        order = [u for _, u in degs]
        col_local = {}
        
        def dfs_local(i):
            if i == len(order):
                return True
            u = order[i]
            used = set()
            for v in sub_adj[u]:
                if v in col_local:
                    used.add(col_local[v])
            for c in (1, 2, 3):
                if c not in used:
                    col_local[u] = c
                    if dfs_local(i + 1):
                        return True
                    del col_local[u]
            return False
        
        result = dfs_local(0)
        if result:
            for u, c in col_local.items():
                color[u] = c
            return True
        return False

    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            comp_nodes = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp_nodes.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            degs = [(len(adj[u]), u) for u in comp_nodes]
            degs.sort(reverse=True)
            order = [u for _, u in degs]
            col_local = {}
            
            def dfs_comp(idx):
                if idx == len(order):
                    return True
                u = order[idx]
                used = set()
                for v in adj[u]:
                    if v in col_local:
                        used.add(col_local[v])
                for c in (1, 2, 3):
                    if c not in used:
                        col_local[u] = c
                        if dfs_comp(idx + 1):
                            return True
                        del col_local[u]
                return False
            
            if not dfs_comp(0):
                print("NO")
                return
            for u, c in col_local.items():
                color[u] = c
    
    print("YES")
    print(' '.join(map(str, color)))

solve()