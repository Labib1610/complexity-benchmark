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
    out = [0] * n

    for i in range(n):
        if color[i] != -1:
            continue
        q = deque([i])
        color[i] = 0
        comp = [i]
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == color[u]:
                    ok = False
        if not ok:
            print("NO")
            return

        mn = min(comp)
        flip = 1 if color[mn] == 1 else 0
        for v in comp:
            out[v] = (color[v] ^ flip) + 1

    print("YES")
    sys.stdout.write(" ".join(map(str, out)))

if __name__ == "__main__":
    solve()