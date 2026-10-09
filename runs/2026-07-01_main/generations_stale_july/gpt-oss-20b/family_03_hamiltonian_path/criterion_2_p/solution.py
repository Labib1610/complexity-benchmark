import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [set() for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if v not in adj[u]:
            adj[u].add(v)
            indeg[v] += 1

    q = deque()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)

    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if len(order) != n:
        print("NO")
        return

    for i in range(n - 1):
        if order[i + 1] not in adj[order[i]]:
            print("NO")
            return

    print("YES")
    print(' '.join(map(str, order)))

if __name__ == "__main__":
    solve()