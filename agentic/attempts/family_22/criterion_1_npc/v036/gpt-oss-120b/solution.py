import sys
import heapq

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); M = int(next(it)); T = int(next(it)); m = int(next(it))
    g = [[] for _ in range(n)]
    rg = [[] for _ in range(n)]
    indeg = [0]*n
    for _ in range(m):
        a = int(next(it))-1
        b = int(next(it))-1
        g[a].append(b)
        rg[b].append(a)
        indeg[b] += 1

    # topological order
    from collections import deque
    q = deque([i for i in range(n) if indeg[i]==0])
    topo = []
    while q:
        v = q.popleft()
        topo.append(v)
        for to in g[v]:
            indeg[to] -= 1
            if indeg[to]==0:
                q.append(to)
    if len(topo)!=n:
        print("NO")
        return

    # earliest times (lower bounds)
    earliest = [1]*n
    for v in topo:
        for to in g[v]:
            if earliest[to] < earliest[v] + 1:
                earliest[to] = earliest[v] + 1

    # longest distance to a sink (for latest times)
    dist_end = [1]*n
    for v in reversed(topo):
        for pre in rg[v]:
            if dist_end[pre] < dist_end[v] + 1:
                dist_end[pre] = dist_end[v] + 1

    latest = [0]*n
    for i in range(n):
        latest[i] = T - dist_end[i] + 1
        if earliest[i] > latest[i]:
            print("NO")
            return

    # bucket tasks by earliest
    buckets = [[] for _ in range(T+2)]
    for i in range(n):
        if earliest[i] <= T:
            buckets[earliest[i]].append(i)

    ans = [0]*n
    heap = []  # (latest, node)
    for t in range(1, T+1):
        for node in buckets[t]:
            heapq.heappush(heap, (latest[node], node))
        cnt = 0
        while heap and cnt < M:
            l, node = heapq.heappop(heap)
            if l < t:   # missed its window
                print("NO")
                return
            ans[node] = t
            cnt += 1
    if heap:
        print("NO")
        return

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()