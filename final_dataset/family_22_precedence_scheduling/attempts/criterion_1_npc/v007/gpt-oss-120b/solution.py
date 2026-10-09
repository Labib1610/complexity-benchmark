import sys
import heapq

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
    indeg = [0] * n
    outdeg = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        radj[b].append(a)
        indeg[b] += 1
        outdeg[a] += 1

    # topological order
    from collections import deque
    q = deque([i for i in range(n) if indeg[i] == 0])
    topo = []
    while q:
        v = q.popleft()
        topo.append(v)
        for to in adj[v]:
            indeg[to] -= 1
            if indeg[to] == 0:
                q.append(to)
    if len(topo) != n:
        print("NO")
        return

    # earliest
    earliest = [1] * n
    for v in topo:
        for to in adj[v]:
            if earliest[to] < earliest[v] + 1:
                earliest[to] = earliest[v] + 1

    # latest
    latest = [T] * n
    for v in reversed(topo):
        for pre in radj[v]:
            if latest[pre] > latest[v] - 1:
                latest[pre] = latest[v] - 1

    for i in range(n):
        if earliest[i] > latest[i] or earliest[i] > T or latest[i] < 1:
            print("NO")
            return

    # bucket jobs by earliest
    bucket = [[] for _ in range(T + 2)]
    for i in range(n):
        bucket[earliest[i]].append(i)

    heap = []          # (latest, job)
    slot_of = [0] * n
    for s in range(1, T + 1):
        for job in bucket[s]:
            heapq.heappush(heap, (latest[job], job))
        cnt = 0
        while cnt < M and heap:
            lat, job = heapq.heappop(heap)
            if lat < s:          # missed deadline
                print("NO")
                return
            slot_of[job] = s
            cnt += 1

    if heap:
        print("NO")
        return

    # all jobs scheduled
    print("YES")
    print(' '.join(str(slot_of[i]) for i in range(n)))

if __name__ == "__main__":
    solve()