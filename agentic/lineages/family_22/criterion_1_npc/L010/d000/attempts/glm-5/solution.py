import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    d = int(next(it))
    p = int(next(it))
    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for _ in range(p):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        radj[b].append(a)
        indeg[b] += 1

    # earliest feasible slot respecting precedence
    earliest = [1] * (n + 1)
    q = deque(i for i in range(1, n + 1) if indeg[i] == 0)
    indeg_work = indeg[:]
    while q:
        u = q.popleft()
        for v in adj[u]:
            if earliest[u] + 1 > earliest[v]:
                earliest[v] = earliest[u] + 1
            indeg_work[v] -= 1
            if indeg_work[v] == 0:
                q.append(v)

    # latest feasible slot respecting precedence and deadline
    latest = [d] * (n + 1)
    outdeg = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in adj[u]:
            outdeg[u] += 1
    q = deque(i for i in range(1, n + 1) if outdeg[i] == 0)
    while q:
        u = q.popleft()
        for v in radj[u]:
            if latest[u] - 1 < latest[v]:
                latest[v] = latest[u] - 1
            outdeg[v] -= 1
            if outdeg[v] == 0:
                q.append(v)

    for i in range(1, n + 1):
        if earliest[i] > latest[i]:
            print("NO")
            return

    # group jobs by earliest slot
    by_earliest = [[] for _ in range(d + 2)]
    for i in range(1, n + 1):
        by_earliest[earliest[i]].append(i)

    slot = [0] * (n + 1)
    ready = []
    for t in range(1, d + 1):
        for j in by_earliest[t]:
            ready.append((latest[j], j))
        ready.sort()
        take = min(m, len(ready))
        chosen = ready[:take]
        ready = ready[take:]
        for _, j in chosen:
            slot[j] = t

    if any(slot[i] == 0 for i in range(1, n + 1)):
        print("NO")
        return

    print("YES")
    print(' '.join(str(slot[i]) for i in range(1, n + 1)))

solve()