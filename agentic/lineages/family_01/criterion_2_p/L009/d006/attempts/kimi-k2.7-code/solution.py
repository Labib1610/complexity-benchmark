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
    ok = True
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            ok = False
        else:
            adj[u].append(v)
            adj[v].append(u)
    if not ok:
        sys.stdout.write("NO")
        return

    color = [0] * n
    dq = deque()
    for i in range(n):
        if color[i]:
            continue
        color[i] = 1
        dq.append(i)
        while dq:
            u = dq.popleft()
            cu = color[u]
            need = 3 - cu
            for v in adj[u]:
                cv = color[v]
                if cv == 0:
                    color[v] = need
                    dq.append(v)
                elif cv != need:
                    sys.stdout.write("NO")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()