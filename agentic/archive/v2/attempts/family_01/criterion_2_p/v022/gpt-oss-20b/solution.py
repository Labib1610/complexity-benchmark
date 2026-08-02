import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n + 1)
    rel_color = [0] * (n + 1)
    res = [0] * (n + 1)

    for start in range(1, n + 1):
        if visited[start]:
            continue
        queue = deque([start])
        visited[start] = True
        rel_color[start] = 0
        comp = [start]
        while queue:
            u = queue.popleft()
            cu = rel_color[u]
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    rel_color[v] = cu ^ 1
                    comp.append(v)
                    queue.append(v)
                else:
                    if rel_color[v] == cu:
                        sys.stdout.write("NO")
                        return
        # determine orientation
        min_node = min(comp)
        flip = 0 if rel_color[min_node] == 0 else 1
        for node in comp:
            res[node] = (rel_color[node] ^ flip) + 1

    out_lines = ["YES", " ".join(map(str, res[1:]))]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()