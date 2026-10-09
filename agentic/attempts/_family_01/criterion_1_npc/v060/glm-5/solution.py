import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    # Check if any vertex has degree >= 3 (cannot be 3-colored)
    for i in range(n):
        if bin(adj[i]).count('1') >= 3:
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
                mask = adj[u]
                v = 0
                while mask:
                    if mask & 1:
                        if not visited[v]:
                            visited[v] = True
                            stack.append(v)
                    mask >>= 1
                    v += 1
            components.append(comp)
    
    assignment = [0] * n
    
    for comp in components:
        size = len(comp)
        if size == 1:
            assignment[comp[0]] = 1
            continue
        
        # Find a vertex with degree 1 (must exist in a path)
        start = -1
        for u in comp:
            if bin(adj[u]).count('1') == 1:
                start = u
                break
        if start == -1:
            start = comp[0]
        
        # BFS to order vertices
        order = []
        seen = [False] * n
        queue = [start]
        seen[start] = True
        while queue:
            u = queue.pop(0)
            order.append(u)
            mask = adj[u]
            v = 0
            while mask:
                if mask & 1:
                    if not seen[v]:
                        seen[v] = True
                        queue.append(v)
                mask >>= 1
                v += 1
        
        # Greedy assignment
        for u in order:
            used = 0
            mask = adj[u]
            v = 0
            while mask:
                if mask & 1:
                    if assignment[v] != 0:
                        used |= 1 << assignment[v]
                mask >>= 1
                v += 1
            for c in range(1, 4):
                if not (used & (1 << c)):
                    assignment[u] = c
                    break
    
    print("YES")
    print(' '.join(map(str, assignment)))

solve()