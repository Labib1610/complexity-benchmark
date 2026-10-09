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

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        radj[b].append(a)
        indeg[b] += 1

    # earliest feasible slot respecting precedence
    earliest = [1] * (n + 1)
    q = deque()
    for v in range(1, n + 1):
        if indeg[v] == 0:
            q.append(v)

    processed = 0
    while q:
        u = q.popleft()
        processed += 1
        for v in adj[u]:
            if earliest[u] + 1 > earliest[v]:
                earliest[v] = earliest[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if processed != n:
        print("NO")
        return

    if any(earliest[v] > T for v in range(1, n + 1)):
        print("NO")
        return

    # latest feasible slot respecting precedence
    latest = [T] * (n + 1)
    outdeg = [0] * (n + 1)
    for u in range(1, n + 1):
        outdeg[u] = len(adj[u])

    q = deque()
    for v in range(1, n + 1):
        if outdeg[v] == 0:
            q.append(v)

    cnt = 0
    while q:
        v = q.popleft()
        cnt += 1
        for u in radj[v]:
            if latest[v] - 1 < latest[u]:
                latest[u] = latest[v] - 1
            outdeg[u] -= 1
            if outdeg[u] == 0:
                q.append(u)

    if cnt != n:
        print("NO")
        return

    if any(latest[v] < earliest[v] for v in range(1, n + 1)):
        print("NO")
        return

    # group jobs by earliest slot
    by_earliest = [[] for _ in range(T + 2)]
    for v in range(1, n + 1):
        by_earliest[earliest[v]].append(v)

    slot = [0] * (n + 1)
    avail = list(range(1, T + 2))  # min-heap of available slots
    import heapq
    heapq.heapify(avail)

    # active jobs sorted by latest slot (min-heap of (latest, job))
    active = []

    for t in range(1, T + 1):
        for v in by_earliest[t]:
            heapq.heappush(active, (latest[v], v))

        used = 0
        while used < M and active:
            lt, v = heapq.heappop(active)
            if lt < t:
                print("NO")
                return
            slot[v] = t
            used += 1

        if used > 0:
            # remove t from available slots
            # we lazily skip stale entries when popping
            heapq.heappush(avail, t + 1)  # placeholder; we actually need to remove t
            # Instead, rebuild is expensive; use a different approach below.

    # The above slot removal logic is flawed; rewrite cleanly.
    # We'll recompute with a correct available-slot management.

    # Reset and redo assignment with proper slot capacity tracking.
    slot = [0] * (n + 1)
    active = []
    for t in range(1, T + 1):
        for v in by_earliest[t]:
            heapq.heappush(active, (latest[v], v))
        cap = M
        tmp = []
        while cap > 0 and active:
            lt, v = heapq.heappop(active)
            if lt < t:
                print("NO")
                return
            slot[v] = t
            cap -= 1
        # push back remaining
        while active:
            tmp.append(heapq.heappop(active))
        for item in tmp:
            heapq.heappush(active, item)

    if any(slot[v] == 0 for v in range(1, n + 1)):
        print("NO")
        return

    # verify precedence
    ok = True
    for u in range(1, n + 1):
        for v in adj[u]:
            if slot[u] >= slot[v]:
                ok = False
                break
        if not ok:
            break

    if not ok:
        print("NO")
        return

    # verify capacity
    cnt_slot = [0] * (T + 2)
    for v in range(1, n + 1):
        cnt_slot[slot[v]] += 1
    if any(cnt_slot[t] > M for t in range(1, T + 1)):
        print("NO")
        return

    print("YES")
    print(" ".join(str(slot[v]) for v in range(1, n + 1)))

solve()