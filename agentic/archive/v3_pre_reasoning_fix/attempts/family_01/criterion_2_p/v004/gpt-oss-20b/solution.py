import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    parity = [-1] * (n + 1)   # -1 unvisited, 0 or 1 relative to component root
    final_color = [0] * (n + 1)  # 1 or 2
    for start in range(1, n + 1):
        if parity[start] != -1:
            continue
        # BFS to process component
        q = deque([start])
        parity[start] = 0
        comp = [start]
        ok = True
        while q:
            v = q.popleft()
            for nb in adj[v]:
                if parity[nb] == -1:
                    parity[nb] = 1 - parity[v]
                    q.append(nb)
                    comp.append(nb)
                elif parity[nb] == parity[v]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            sys.stdout.write("NO")
            return
        # Determine orientation
        min_vertex = min(comp)
        p = parity[min_vertex]
        root_color = 1 if p == 0 else 2
        for v in comp:
            final_color[v] = root_color if parity[v] == 0 else 3 - root_color

    out_lines = ["YES", " ".join(str(final_color[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()