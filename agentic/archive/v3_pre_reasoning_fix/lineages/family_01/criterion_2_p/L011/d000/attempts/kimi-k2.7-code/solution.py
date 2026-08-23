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

    color = [0] * (n + 1)  # 0 unvisited, 1 or 2 assigned

    for i in range(1, n + 1):
        if color[i] != 0:
            continue
        dq = deque([i])
        color[i] = 1
        while dq:
            u = dq.popleft()
            cu = color[u]
            other = 3 - cu
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = other
                    dq.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO")
                    return

    out = ["YES"]
    out.append(" ".join(str(color[i]) for i in range(1, n + 1)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()