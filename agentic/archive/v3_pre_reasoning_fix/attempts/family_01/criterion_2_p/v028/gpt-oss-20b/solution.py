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

    color = [0] * (n + 1)  # 0 uncolored, 1 or 2
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        # start new component, assign 1 to smallest index vertex
        color[start] = 1
        dq = deque([start])
        while dq:
            v = dq.popleft()
            cv = color[v]
            for u in adj[v]:
                if color[u] == 0:
                    color[u] = 3 - cv  # opposite color
                    dq.append(u)
                elif color[u] == cv:
                    print("NO")
                    return

    # All vertices colored
    out = ['YES', '\n', ' '.join(str(color[i]) for i in range(1, n + 1))]
    sys.stdout.write(''.join(out))

if __name__ == "__main__":
    solve()