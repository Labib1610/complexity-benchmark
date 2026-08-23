import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)  # 0 = uncolored, 1 or 2
    for start in range(1, n + 1):
        if color[start]:
            continue
        color[start] = 1
        dq = deque([start])
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                if not color[v]:
                    color[v] = 3 - color[u]
                    dq.append(v)
                elif color[v] == color[u]:
                    sys.stdout.write("NO")
                    return
    out_lines = ["YES", " ".join(map(str, color[1:]))]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()