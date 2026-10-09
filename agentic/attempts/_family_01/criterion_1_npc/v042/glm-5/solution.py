import sys

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
    
    # Check if any node has degree >= 3 (needs 4 colors)
    for i in range(n):
        if len(adj[i]) >= 3:
            print("NO")
            return
    
    # Find connected components
    visited = [False] * n
    components = []
    
    for i in range(n):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            comp = []
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            components.append(comp)
    
    color = [0] * n
    
    for comp in components:
        # Find a node with degree 2 (or any node if all have degree < 2)
        start = -1
        for u in comp:
            if len(adj[u]) == 2:
                start = u
                break
        if start == -1:
            start = comp[0]
        
        # BFS from start
        order = []
        q = [start]
        visited_bfs = [False] * n
        visited_bfs[start] = True
        while q:
            u = q.pop(0)
            order.append(u)
            for v in adj[u]:
                if not visited_bfs[v]:
                    visited_bfs[v] = True
                    q.append(v)
        
        for u in order:
            used = set()
            for v in adj[u]:
                if color[v] != 0:
                    used.add(color[v])
            for c in range(1, 4):
                if c not in used:
                    color[u] = c
                    break
    
    # Verify solution
    for u in range(n):
        for v in adj[u]:
            if v > u and color[u] == color[v]:
                print("NO")
                return
    
    print("YES")
    print(' '.join(map(str, color)))

solve()