import sys
from collections import deque

def solve():
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

    color = [0] * (n + 1)
    dq = deque()

    for i in range(1, n + 1):
        if color[i]:
            continue
        color[i] = 1
        dq.append(i)
        while dq:
            u = dq.popleft()
            cu = color[u]
            opp = 3 - cu
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = opp
                    dq.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(map(str, color[1:])))

if __name__ == "__main__":
    solve()