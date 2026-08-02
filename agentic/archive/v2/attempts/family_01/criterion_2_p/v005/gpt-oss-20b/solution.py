import sys
from collections import deque

def solve() -> None:
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

    color = [-1] * n   # -1 unvisited, 0 or 1
    res = [0] * n

    for start in range(n):
        if color[start] != -1:
            continue
        # BFS to color component
        q = deque([start])
        color[start] = 0
        comp_nodes = [start]
        ok = True
        while q and ok:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                    comp_nodes.append(v)
                elif color[v] == cu:
                    ok = False
                    break
        if not ok:
            sys.stdout.write("NO")
            return
        # Determine mapping for lexicographically smallest
        first = min(comp_nodes)
        if color[first] == 0:
            # color 0 -> shift 1, color 1 -> shift 2
            for node in comp_nodes:
                res[node] = 1 if color[node] == 0 else 2
        else:
            # color 0 -> shift 2, color 1 -> shift 1
            for node in comp_nodes:
                res[node] = 2 if color[node] == 0 else 1

    out_lines = ["YES", " ".join(map(str, res))]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()