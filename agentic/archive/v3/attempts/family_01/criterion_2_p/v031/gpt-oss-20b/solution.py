import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n          # 0 or 1
    final = [0] * n           # 0 or 1 after possible flip
    visited = [False] * n

    for start in range(n):
        if visited[start]:
            continue
        # BFS to build component
        queue = deque([start])
        visited[start] = True
        comp_vertices = [start]
        color[start] = 0
        min_vertex = start
        ok = True
        while queue:
            u = queue.popleft()
            cu = color[u]
            if u < min_vertex:
                min_vertex = u
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = cu ^ 1
                    queue.append(v)
                    comp_vertices.append(v)
                else:
                    if color[v] == cu:
                        print("NO")
                        return
        # decide flip
        if color[min_vertex] == 1:
            for v in comp_vertices:
                final[v] = color[v] ^ 1
        else:
            for v in comp_vertices:
                final[v] = color[v]
    # Output
    print("YES")
    print(' '.join(str(x + 1) for x in final))

if __name__ == "__main__":
    solve()