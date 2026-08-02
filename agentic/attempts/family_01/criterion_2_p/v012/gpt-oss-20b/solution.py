import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
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
    res = [0] * n             # final 1 or 2

    for start in range(n):
        if color[start] != -1:
            continue
        # BFS component
        q = deque([start])
        color[start] = 0
        comp_nodes = [start]
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp_nodes.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # Determine orientation: ensure smallest node gets 1
        min_node = min(comp_nodes)
        if color[min_node] == 0:
            # 0 -> 1, 1 -> 2
            for v in comp_nodes:
                res[v] = 1 if color[v] == 0 else 2
        else:
            # 0 -> 2, 1 -> 1
            for v in comp_nodes:
                res[v] = 2 if color[v] == 0 else 1

    print("YES")
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()