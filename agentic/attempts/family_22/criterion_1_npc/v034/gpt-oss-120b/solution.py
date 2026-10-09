import sys
from collections import deque

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
    indeg = [0]*n
    for _ in range(m):
        a = int(next(it))-1
        b = int(next(it))-1
        adj[a].append(b)
        indeg[b] += 1

    # topological order
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

    # earliest possible time (lower bound)
    earliest = [1]*n
    for v in topo:
        for nb in adj[v]:
            if earliest[nb] < earliest[v]+1:
                earliest[nb] = earliest[v]+1

    # schedule using list scheduling respecting earliest
    slots = [[] for _ in range(T+1)]  # 1-indexed
    ready = []
    indeg = [0]*n
    for a in range(n):
        indeg[a] = len([p for p in range(n) if a in adj[p]])  # recompute slower but n small
    # better compute reverse adjacency
    rev = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            rev[v].append(u)

    # initial ready set
    for i in range(n):
        if not rev[i]:
            ready.append(i)

    import heapq
    heap = []
    for v in ready:
        heapq.heappush(heap, (earliest[v], v))

    assigned = [0]*n
    for t in range(1, T+1):
        cnt = 0
        next_heap = []
        while heap and cnt < M:
            e, v = heapq.heappop(heap)
            if e > t:   # not yet eligible
                next_heap.append((e, v))
                continue
            assigned[v] = t
            cnt += 1
            for nb in adj[v]:
                rev[nb].remove(v)
                if not rev[nb]:
                    heapq.heappush(heap, (earliest[nb], nb))
        # push back those not eligible
        for item in next_heap:
            heapq.heappush(heap, item)
        # if heap empty break
        if not heap and cnt==0:
            break

    if any(a==0 for a in assigned):
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, assigned)))

if __name__ == "__main__":
    solve()