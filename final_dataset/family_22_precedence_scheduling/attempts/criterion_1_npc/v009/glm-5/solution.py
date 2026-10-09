import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    outdeg = [0] * (n + 1)

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        radj[b].append(a)
        indeg[b] += 1
        outdeg[a] += 1

    INF = T + 1
    earliest = [1] * (n + 1)
    q = deque()
    for v in range(1, n + 1):
        if indeg[v] == 0:
            q.append(v)
    seen = 0
    while q:
        u = q.popleft()
        seen += 1
        for w in adj[u]:
            if earliest[u] + 1 > earliest[w]:
                earliest[w] = earliest[u] + 1
            indeg[w] -= 1
            if indeg[w] == 0:
                q.append(w)
    if seen != n:
        print("NO")
        return

    latest = [T] * (n + 1)
    q = deque()
    for v in range(1, n + 1):
        if outdeg[v] == 0:
            q.append(v)
    while q:
        u = q.popleft()
        for w in radj[u]:
            if latest[u] - 1 < latest[w]:
                latest[w] = latest[u] - 1
            outdeg[w] -= 1
            if outdeg[w] == 0:
                q.append(w)

    for v in range(1, n + 1):
        if earliest[v] > latest[v]:
            print("NO")
            return

    nodes = list(range(1, n + 1))
    nodes.sort(key=lambda v: (earliest[v], latest[v]))

    cap = [0] * (T + 2)
    slot = [0] * (n + 1)
    for v in nodes:
        t = earliest[v]
        while t <= latest[v] and cap[t] >= M:
            t += 1
        if t > latest[v]:
            print("NO")
            return
        slot[v] = t
        cap[t] += 1

    print("YES")
    print(' '.join(str(slot[v]) for v in range(1, n + 1)))

if __name__ == "__main__":
    solve()