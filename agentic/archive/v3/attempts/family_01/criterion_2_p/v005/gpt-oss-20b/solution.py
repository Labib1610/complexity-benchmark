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

    color = [-1] * (n + 1)
    res = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS to color component
        q = deque([start])
        color[start] = 0
        comp = [start]
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                    comp.append(v)
                elif color[v] == color[u]:
                    sys.stdout.write("NO")
                    return
        # choose orientation to give smallest index node shift 1
        min_node = min(comp)
        if color[min_node] == 0:
            for u in comp:
                res[u] = color[u] + 1
        else:
            for u in comp:
                res[u] = 2 - color[u]

    out_lines = ["YES", " ".join(map(str, res[1:]))]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()