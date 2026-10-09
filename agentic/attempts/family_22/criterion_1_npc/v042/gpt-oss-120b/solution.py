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

    # earliest
    earliest = [1]*n
    for v in topo:
        for to in g[v]:
            if earliest[to] < earliest[v] + 1:
                earliest[to] = earliest[v] + 1

    # latest
    latest = [T]*n
    for v in reversed(topo):
        for pre in rg[v]:
            # v must be after pre, so pre <= latest[v]-1
            if latest[pre] > latest[v] - 1:
                latest[pre] = latest[v] - 1

    for i in range(n):
        if earliest[i] > latest[i] or earliest[i] > T or latest[i] < 1:
            print("NO")
            return

    # bucket vertices by earliest
    bucket = [[] for _ in range(T+2)]
    for i in range(n):
        bucket[earliest[i]].append(i)

    ans = [0]*n
    heap = []  # (latest, vertex)
    for t in range(1, T+1):
        for v in bucket[t]:
            heapq.heappush(heap, (latest[v], v))
        cnt = 0
        while heap and cnt < M:
            dl, v = heapq.heappop(heap)
            if dl < t:          # missed deadline
                print("NO")
                return
            ans[v] = t
            cnt += 1
    if heap:
        print("NO")
        return

    print("YES")
    print(' '.join(str(x) for x in ans))

if __name__ == "__main__":
    solve()