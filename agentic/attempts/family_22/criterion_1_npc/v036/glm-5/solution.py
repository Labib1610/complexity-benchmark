import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        indeg[b] += 1

    # earliest possible stage for each compound (longest path from a source)
    earliest = [0] * (n + 1)
    q = deque()
    for v in range(1, n + 1):
        if indeg[v] == 0:
            earliest[v] = 1
            q.append(v)

    cnt = 0
    while q:
        u = q.popleft()
        cnt += 1
        for v in adj[u]:
            if earliest[v] < earliest[u] + 1:
                earliest[v] = earliest[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if cnt != n:
        print("NO")
        return

    if any(earliest[v] > T for v in range(1, n + 1)):
        print("NO")
        return

    # latest possible stage for each compound
    latest = [T] * (n + 1)
    radj = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in adj[u]:
            radj[v].append(u)

    q = deque()
    for v in range(1, n + 1):
        if not radj[v]:
            latest[v] = T
            q.append(v)

    while q:
        v = q.popleft()
        for u in radj[v]:
            if latest[u] > latest[v] - 1:
                latest[u] = latest[v] - 1
                q.append(u)

    if any(earliest[v] > latest[v] for v in range(1, n + 1)):
        print("NO")
        return

    # assign greedily: process stages left to right, fill each stage with
    # available compounds whose latest stage is smallest (EDF)
    stage = [0] * (n + 1)
    rem_indeg = [0] * (n + 1)
    for v in range(1, n + 1):
        rem_indeg[v] = len(radj[v])

    avail = []
    for v in range(1, n + 1):
        if rem_indeg[v] == 0:
            avail.append(v)

    for s in range(1, T + 1):
        # keep only compounds that can still be placed at stage >= s
        avail = [v for v in avail if latest[v] >= s]
        # those that must be placed now (latest == s) go first
        avail.sort(key=lambda x: (latest[x], earliest[x]))
        placed = 0
        new_avail = []
        for v in avail:
            if placed < M and latest[v] >= s:
                stage[v] = s
                placed += 1
                for w in adj[v]:
                    rem_indeg[w] -= 1
                    if rem_indeg[w] == 0:
                        new_avail.append(w)
            else:
                new_avail.append(v)
        avail = new_avail

    if any(stage[v] == 0 for v in range(1, n + 1)):
        print("NO")
        return

    print("YES")
    print(" ".join(str(stage[v]) for v in range(1, n + 1)))

solve()