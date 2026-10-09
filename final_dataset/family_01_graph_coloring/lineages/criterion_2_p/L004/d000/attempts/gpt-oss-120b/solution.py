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
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)  # 0 uncolored, 1 or 2
    for i in range(1, n + 1):
        if color[i]:
            continue
        # start new component, assign smallest index node to 1
        color[i] = 1
        q = deque([i])
        while q:
            u = q.popleft()
            cu = color[u]
            cv = 3 - cu
            for v in adj[u]:
                if not color[v]:
                    color[v] = cv
                    q.append(v)
                elif color[v] != cv:
                    sys.stdout.write("NO")
                    return
    # all good
    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()