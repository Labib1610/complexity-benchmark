import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)
    res = [0] * (n + 1)

    for i in range(1, n + 1):
        if color[i] != -1:
            continue
        queue = deque([i])
        color[i] = 0
        comp = [i]
        while queue:
            v = queue.popleft()
            cv = color[v]
            for nb in adj[v]:
                cn = color[nb]
                if cn == -1:
                    color[nb] = cv ^ 1
                    queue.append(nb)
                    comp.append(nb)
                elif cn == cv:
                    print("NO")
                    return
        for u in comp:
            res[u] = color[u] + 1

    out = ['YES', '\n', ' '.join(map(str, res[1:]))]
    sys.stdout.write(''.join(out))

if __name__ == "__main__":
    solve()