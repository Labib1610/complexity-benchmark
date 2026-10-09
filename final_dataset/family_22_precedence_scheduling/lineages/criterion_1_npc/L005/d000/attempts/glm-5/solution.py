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

    # earliest possible time for each operation
    earliest = [0] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            earliest[i] = 1
            q.append(i)

    cnt = 0
    while q:
        u = q.popleft()
        cnt += 1
        for v in adj[u]:
            if earliest[u] + 1 > earliest[v]:
                earliest[v] = earliest[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                if earliest[v] == 0:
                    earliest[v] = 1
                q.append(v)

    if cnt != n:
        print("NO")
        return

    # check feasibility of earliest times
    for i in range(1, n + 1):
        if earliest[i] > T:
            print("NO")
            return

    # count how many operations have earliest time >= t
    cnt_ge = [0] * (T + 2)
    for i in range(1, n + 1):
        cnt_ge[earliest[i]] += 1
    for t in range(T - 1, 0, -1):
        cnt_ge[t] += cnt_ge[t + 1]

    # latest feasible time for each operation
    latest = [0] * (n + 1)
    for i in range(1, n + 1):
        lo = earliest[i]
        hi = T
        ans = lo
        while lo <= hi:
            mid = (lo + hi) // 2
            ok = True
            for t in range(earliest[i], mid + 1):
                if cnt_ge[t] > (T - t + 1) * M:
                    ok = False
                    break
            if ok:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        latest[i] = ans

    # assign times greedily from earliest to latest
    ops_by_earliest = [[] for _ in range(T + 1)]
    for i in range(1, n + 1):
        ops_by_earliest[earliest[i]].append(i)

    # for each operation, maintain a pointer to its current candidate time
    ptr = [0] * (n + 1)
    for i in range(1, n + 1):
        ptr[i] = earliest[i]

    # for each time, maintain a heap of operations available (by latest time)
    import heapq
    avail = []
    assigned = [0] * (n + 1)
    remaining = n

    for t in range(1, T + 1):
        for op in ops_by_earliest[t]:
            heapq.heappush(avail, (latest[op], op))
        slots = M
        while slots > 0 and avail:
            lt, op = heapq.heappop(avail)
            if lt < t:
                print("NO")
                return
            assigned[op] = t
            slots -= 1
            remaining -= 1

    if remaining > 0:
        print("NO")
        return

    print("YES")
    print(' '.join(str(assigned[i]) for i in range(1, n + 1)))

solve()