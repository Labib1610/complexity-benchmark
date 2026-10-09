import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        g[u].append(v)
        g[v].append(u)

    color = [0] * (n + 1)          # 0 = uncolored, 1 or 2
    for start in range(1, n + 1):
        if color[start]:
            continue
        # start new component, try to color start with 1
        q = deque([start])
        color[start] = 1
        while q:
            u = q.popleft()
            cu = color[u]
            cv = 1 if cu == 2 else 2   # opposite color
            for v in g[u]:
                if not color[v]:
                    color[v] = cv
                    q.append(v)
                elif color[v] != cv:
                    print("NO")
                    return

    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()