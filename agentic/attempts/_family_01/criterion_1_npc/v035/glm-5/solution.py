import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

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
                for v in range(n):
                    if (adj[u] >> v) & 1 and not visited[v]:
                        visited[v] = True
                        stack.append(v)
            components.append(comp)

    color = [0] * n

    for comp in components:
        size = len(comp)
        if size == 1:
            color[comp[0]] = 1
            continue

        # Map component vertices to indices 0..size-1
        idx_map = {v: i for i, v in enumerate(comp)}
        comp_adj = [0] * size
        for u in comp:
            iu = idx_map[u]
            for v in comp:
                if (adj[u] >> v) & 1:
                    comp_adj[iu] |= 1 << idx_map[v]

        # Try all 3^size colorings
        total = 1
        for _ in range(size):
            total *= 3
            if total > 43046721:
                total = 43046721
                break

        found = False
        # Iterate 3^size
        max_mask = 1 << size
        # We'll iterate c from 0 to 3^size - 1
        # But size can be up to 40, so we can't do 3^40.
        # However, for 3-coloring, each component must be small enough.
        # Actually, we need a smarter approach for large components.
        # Let's use backtracking with pruning.
        
        # Backtracking approach
        comp_color = [0] * size
        def backtrack(pos):
            nonlocal found
            if found:
                return
            if pos == size:
                found = True
                return
            used = 0
            for v in range(size):
                if (comp_adj[pos] >> v) & 1 and v < pos:
                    used |= 1 << comp_color[v]
            for c in range(3):
                if not (used >> c) & 1:
                    comp_color[pos] = c
                    backtrack(pos + 1)
                    if found:
                        return
            comp_color[pos] = 0
        
        backtrack(0)
        
        if not found:
            print("NO")
            return
        
        for i, v in enumerate(comp):
            color[v] = comp_color[i] + 1

    print("YES")
    print(" ".join(map(str, color)))

solve()