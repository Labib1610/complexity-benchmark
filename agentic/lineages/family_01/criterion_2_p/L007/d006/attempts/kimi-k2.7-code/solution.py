import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
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

    color = [-1] * n
    ans = [0] * n

    for start in range(n):
        if color[start] != -1:
            continue
        # BFS/DFS component
        comp = []
        dq = deque([start])
        color[start] = 0
        min_vertex = start
        while dq:
            v = dq.popleft()
            comp.append(v)
            if v < min_vertex:
                min_vertex = v
            cv = color[v]
            for to in adj[v]:
                if color[to] == -1:
                    color[to] = cv ^ 1
                    dq.append(to)
                elif color[to] == cv:
                    print("NO")
                    return
        # Assign lexicographically smallest for this component:
        # the minimum vertex in the component gets value 1.
        if color[min_vertex] == 0:
            val0, val1 = 1, 2
        else:
            val0, val1 = 2, 1
        for v in comp:
            ans[v] = val0 if color[v] == 0 else val1

    print("YES")
    print(' '.join(map(str, ans)))

solve()