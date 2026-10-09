import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Find connected components
    visited = [False] * (n + 1)
    components = []
    for i in range(1, n + 1):
        if not visited[i]:
            comp = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in range(1, n + 1):
                    if (adj[u] >> v) & 1 and not visited[v]:
                        visited[v] = True
                        stack.append(v)
            components.append(comp)

    color = [0] * (n + 1)

    for comp in components:
        # Try to 2-color this component
        bip = True
        col = {}
        start = comp[0]
        col[start] = 0
        stack = [start]
        while stack and bip:
            u = stack.pop()
            for v in comp:
                if (adj[u] >> v) & 1:
                    if v not in col:
                        col[v] = col[u] ^ 1
                        stack.append(v)
                    elif col[v] == col[u]:
                        bip = False
                        break

        if bip:
            for u in comp:
                color[u] = col[u] + 1
        else:
            # Try to 3-color this component
            comp_idx = {v: i for i, v in enumerate(comp)}
            k = len(comp)
            adj_comp = [0] * k
            for i in range(k):
                u = comp[i]
                for j in range(k):
                    v = comp[j]
                    if (adj[u] >> v) & 1:
                        adj_comp[i] |= 1 << j

            found = False
            assignment = [0] * k

            def backtrack(pos, used):
                nonlocal found, assignment
                if found:
                    return
                if pos == k:
                    found = True
                    return
                u = pos
                avail = 7  # bits 0,1,2
                for v in range(u):
                    if (adj_comp[u] >> v) & 1:
                        avail &= ~(1 << assignment[v])
                c = 0
                while c < 3 and not found:
                    if (avail >> c) & 1:
                        assignment[u] = c
                        backtrack(pos + 1, used)
                        if found:
                            return
                    c += 1

            backtrack(0, 0)
            if not found:
                print("NO")
                return
            for i, u in enumerate(comp):
                color[u] = assignment[i] + 1

    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

solve()