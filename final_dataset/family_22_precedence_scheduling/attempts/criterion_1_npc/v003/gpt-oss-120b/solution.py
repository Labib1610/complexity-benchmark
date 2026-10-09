import sys
import threading
def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); M = int(next(it)); T = int(next(it)); m = int(next(it))
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

    # earliest
    earliest = [1]*n
    for v in topo:
        for nb in adj[v]:
            if earliest[nb] < earliest[v] + 1:
                earliest[nb] = earliest[v] + 1

    # latest using reverse topo
    dist_end = [0]*n
    for v in reversed(topo):
        maxd = 0
        for nb in adj[v]:
            if dist_end[nb] + 1 > maxd:
                maxd = dist_end[nb] + 1
        dist_end[v] = maxd
    latest = [T - dist_end[i] for i in range(n)]

    for i in range(n):
        if earliest[i] > latest[i] or earliest[i] > T or latest[i] < 1:
            print("NO")
            return

    # bucket tasks by earliest
    buckets = [[] for _ in range(T+2)]
    for i in range(n):
        e = earliest[i]
        if e<=T:
            buckets[e].append(i)

    import heapq
    heap = []  # (latest, task)
    slot_of = [0]*n
    assigned = 0
    for t in range(1, T+1):
        for task in buckets[t]:
            heapq.heappush(heap, (latest[task], task))
        cap = M
        while cap and heap:
            l, task = heapq.heappop(heap)
            if l < t:   # missed deadline
                print("NO")
                return
            slot_of[task] = t
            assigned += 1
            cap -= 1
        # continue
    if assigned != n:
        # some tasks left with earliest > T (should not happen) or impossible
        print("NO")
        return
    print("YES")
    print(' '.join(str(slot_of[i]) for i in range(n)))

if __name__ == "__main__":
    threading.Thread(target=solve).start()