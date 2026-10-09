import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    seen = set()
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        if u > v:
            u, v = v, u
        if (u, v) in seen:
            continue
        seen.add((u, v))
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n
    comp_id = [-1] * n
    comps = []
    for i in range(n):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            comp = []
            while stack:
                x = stack.pop()
                comp_id[x] = len(comps)
                comp.append(x)
                for y in adj[x]:
                    if not visited[y]:
                        visited[y] = True
                        stack.append(y)
            comps.append(sorted(comp))

    answer = [0] * n

    for comp in comps:
        k = len(comp)
        local_index = {v: idx for idx, v in enumerate(comp)}
        local_adj = [[] for _ in range(k)]
        for idx, v in enumerate(comp):
            for u in adj[v]:
                local_adj[idx].append(local_index[u])

        colors = [0] * k
        domains = [7] * k
        history = []

        def propagate(v, c):
            # assign color c to v and do unit propagation
            history.append((v, domains[v]))
            colors[v] = c
            domains[v] = 1 << (c - 1)
            queue = deque([v])
            mask_remove = ~(1 << (c - 1)) & 7
            while queue:
                x = queue.popleft()
                cx = colors[x]
                bit = 1 << (cx - 1)
                for y in local_adj[x]:
                    if colors[y] != 0:
                        if colors[y] == cx:
                            return False
                        continue
                    if domains[y] & bit:
                        history.append((y, domains[y]))
                        domains[y] &= ~bit
                        if domains[y] == 0:
                            return False
                        # single remaining color -> force
                        if domains[y] & (domains[y] - 1) == 0:
                            cy = domains[y].bit_length()
                            colors[y] = cy
                            queue.append(y)
            return True

        def dfs():
            v = -1
            for i in range(k):
                if colors[i] == 0:
                    v = i
                    break
            if v == -1:
                return True
            d = domains[v]
            for c in (1, 2, 3):
                if d & (1 << (c - 1)):
                    mark = len(history)
                    if propagate(v, c):
                        if dfs():
                            return True
                    while len(history) > mark:
                        node, old = history.pop()
                        domains[node] = old
                        colors[node] = 0
            return False

        if not dfs():
            print("NO")
            return
        for idx, v in enumerate(comp):
            answer[v] = colors[idx]

    print("YES")
    print(' '.join(map(str, answer)))

solve()