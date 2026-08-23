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

    color = [0] * n  # 0 unvisited, 1 or 2

    for start in range(n):
        if color[start] != 0:
            continue
        color[start] = 1
        q = deque([start])
        while q:
            u = q.popleft()
            cu = color[u]
            other = 3 - cu
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = other
                    q.append(v)
                elif color[v] == cu:
                    print("NO")
                    return
    print("YES")
    out = ' '.join(str(c) for c in color)
    print(out)

if __name__ == "__main__":
    solve()