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

    color = [0] * (n + 1)  # 0 unassigned, 1 or 2 assigned

    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        color[start] = 1
        q = deque([start])
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - cu
                    q.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO")
                    return

    out = ["YES", "\n", " ".join(str(color[i]) for i in range(1, n + 1))]
    sys.stdout.write("".join(out))

if __name__ == "__main__":
    solve()