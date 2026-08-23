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

    color = [0] * n
    for i in range(n):
        if color[i] != 0:
            continue
        color[i] = 1
        dq = deque([i])
        while dq:
            u = dq.popleft()
            cu = color[u]
            cv = 3 - cu
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = cv
                    dq.append(v)
                elif color[v] != cv:
                    sys.stdout.write("NO\n")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color)))
    sys.stdout.write("\n")

if __name__ == "__main__":
    solve()