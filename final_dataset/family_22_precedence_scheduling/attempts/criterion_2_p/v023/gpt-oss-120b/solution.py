import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for _ in range(m):
        x = int(next(it))
        y = int(next(it))
        adj[x].append(y)
        indeg[y] += 1

    q = deque(i for i in range(1, n + 1) if indeg[i] == 0)
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for to in adj[v]:
            indeg[to] -= 1
            if indeg[to] == 0:
                q.append(to)

    if len(order) == n:
        out = ["YES", " ".join(map(str, order))]
    else:
        out = ["NO"]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()