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
        a = int(next(it)); b = int(next(it))
        adj[a].append(b)
        indeg[b] += 1

    q = deque(i for i in range(1, n + 1) if indeg[i] == 0)
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for nb in adj[v]:
            indeg[nb] -= 1
            if indeg[nb] == 0:
                q.append(nb)

    if len(order) == n:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, order)))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()