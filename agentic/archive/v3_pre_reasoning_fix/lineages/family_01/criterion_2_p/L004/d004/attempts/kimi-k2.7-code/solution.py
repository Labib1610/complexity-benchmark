import sys
from collections import deque

def solve():
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
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n

    for i in range(n):
        if color[i]:
            continue
        dq = deque([i])
        color[i] = 1
        comp = []
        while dq:
            v = dq.popleft()
            comp.append(v)
            cv = color[v]
            other = 3 - cv
            for w in adj[v]:
                if color[w] == 0:
                    color[w] = other
                    dq.append(w)
                elif color[w] == cv:
                    print("NO")
                    return
        if color[i] == 2:
            for v in comp:
                color[v] = 3 - color[v]

    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()