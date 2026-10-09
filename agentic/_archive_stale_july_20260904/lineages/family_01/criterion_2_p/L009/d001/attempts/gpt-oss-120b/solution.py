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

    col = [-1] * (n + 1)          # 0 / 1 temporary colours
    ans = [0] * (n + 1)

    for start in range(1, n + 1):
        if col[start] != -1:
            continue
        # BFS for this component
        q = deque([start])
        col[start] = 0
        comp = [start]
        mn = start
        while q:
            v = q.popleft()
            if v < mn:
                mn = v
            for to in adj[v]:
                if col[to] == -1:
                    col[to] = col[v] ^ 1
                    q.append(to)
                    comp.append(to)
                elif col[to] == col[v]:
                    sys.stdout.write("NO")
                    return
        # decide orientation: make vertex mn have shift 1
        flip = 1 if col[mn] == 1 else 0
        for v in comp:
            ans[v] = (col[v] ^ flip) + 1

    out = ["YES", " ".join(str(ans[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()