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
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n
    dq = deque()
    for i in range(n):
        if color[i] != -1:
            continue
        color[i] = 0
        dq.append(i)
        while dq:
            v = dq.popleft()
            cv = color[v]
            for w in adj[v]:
                if color[w] == -1:
                    color[w] = cv ^ 1
                    dq.append(w)
                elif color[w] == cv:
                    sys.stdout.write("NO")
                    return

    out = ["YES", " ".join(str(c + 1) for c in color)]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()