import sys
import threading
def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    indeg = [0]*n
    outdeg = [0]*n
    for _ in range(m):
        a = int(next(it))-1
        b = int(next(it))-1
        adj[a].append(b)
        radj[b].append(a)
        indeg[b] += 1
        outdeg[a] += 1

    # topological order
    from collections import deque
    q = deque([i for i in range(n) if indeg[i]==0])
    topo = []
    while q:
        v = q.popleft()
        topo.append(v)
        for nb in adj[v]:
            indeg[nb] -= 1
            if indeg[nb]==0:
                q.append(nb)
    if len(topo)!=n:
        print("NO")
        return

    # forward longest path (L)
    L = [1]*n
    for v in topo:
        lv = L[v]
        for nb in adj[v]:
            if L[nb] < lv + 1:
                L[nb] = lv + 1

    # backward longest path (R)
    R = [1]*n
    for v in reversed(topo):
        rv = R[v]
        for p in radj[v]:
            if R[p] < rv + 1:
                R[p] = rv + 1

    U = [T - R[i] + 1 for i in range(n)]

    for i in range(n):
        if L[i] > U[i] or L[i] > T or U[i] < 1:
            print("NO")
            return

    # bucket jobs by release time
    buckets = [[] for _ in range(T+2)]
    for i in range(n):
        buckets[L[i]].append(i)

    import heapq
    heap = []          # (deadline, job)
    slot_of = [0]*n
    assigned = 0
    t = 1
    while t <= T and assigned < n:
        for job in buckets[t]:
            heapq.heappush(heap, (U[job], job))
        cnt = 0
        while cnt < M and heap:
            deadline, job = heapq.heappop(heap)
            if deadline < t:
                print("NO")
                return
            slot_of[job] = t
            assigned += 1
            cnt += 1
        t += 1

    if assigned < n:
        print("NO")
        return

    print("YES")
    print(' '.join(str(slot_of[i]) for i in range(n)))

if __name__ == "__main__":
    threading.Thread(target=solve).start()