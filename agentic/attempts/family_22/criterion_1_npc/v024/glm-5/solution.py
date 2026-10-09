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
    
    # earliest cycle: longest path from any source
    earliest = [1] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)
    
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            if earliest[v] < earliest[u] + 1:
                earliest[v] = earliest[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if len(topo) != n:
        print("NO")
        return
    
    if any(earliest[i] > T for i in range(1, n + 1)):
        print("NO")
        return
    
    # latest cycle
    latest = [T] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if outdeg[i] == 0:
            q.append(i)
    
    while q:
        u = q.popleft()
        for v in radj[u]:
            if latest[v] > latest[u] - 1:
                latest[v] = latest[u] - 1
            outdeg[v] -= 1
            if outdeg[v] == 0:
                q.append(v)
    
    if any(latest[i] < 1 for i in range(1, n + 1)):
        print("NO")
        return
    
    # group by latest
    by_latest = [[] for _ in range(T + 1)]
    for i in range(1, n + 1):
        by_latest[latest[i]].append(i)
    
    # assign greedily
    assign = [0] * (n + 1)
    active = []
    for t in range(1, T + 1):
        # remove expired
        active = [x for x in active if x > t]
        # add new
        active.extend(by_latest[t])
        # sort by latest
        active.sort()
        if len(active) > M:
            print("NO")
            return
        for x in active:
            assign[x] = t
        active = [x for x in active if earliest[x] > t]
    
    print("YES")
    print(" ".join(str(assign[i]) for i in range(1, n + 1)))

solve()