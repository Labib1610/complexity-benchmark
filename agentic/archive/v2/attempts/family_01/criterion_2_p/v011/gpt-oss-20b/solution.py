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

    color = [-1] * (n + 1)  # -1 unvisited, 0 or 1 relative color
    res = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS for component
        q = deque([start])
        color[start] = 0
        comp_nodes = [start]
        min_idx = start
        min_color = 0
        ok = True
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                cv = color[v]
                if cv == -1:
                    color[v] = 1 - cu
                    q.append(v)
                    comp_nodes.append(v)
                    if v < min_idx:
                        min_idx = v
                        min_color = color[v]
                else:
                    if cv != 1 - cu:
                        ok = False
                        break
            if not ok:
                break
        if not ok:
            sys.stdout.write("NO")
            return
        # Determine mapping: make node with min_idx color 1
        if min_color == 0:
            # 0 -> 1, 1 -> 2
            for u in comp_nodes:
                res[u] = color[u] + 1
        else:
            # 1 -> 1, 0 -> 2
            for u in comp_nodes:
                res[u] = 3 - color[u]

    out_lines = ["YES", " ".join(map(str, res[1:]))]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()