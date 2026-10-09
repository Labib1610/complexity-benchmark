import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)          # 0 = uncolored, 1 or 2 otherwise
    for start in range(1, n + 1):
        if color[start]:
            continue
        # start new component, assign smallest index node color 1
        color[start] = 1
        dq = deque([start])
        while dq:
            u = dq.popleft()
            cu = color[u]
            for v in adj[u]:
                if not color[v]:
                    color[v] = 3 - cu   # opposite color (1<->2)
                    dq.append(v)
                elif color[v] == cu:
                    print("NO")
                    return

    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()