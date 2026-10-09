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
    indeg = [0] * n
    outdeg = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        g[a].append(b)
        rg[b].append(a)
        indeg[b] += 1
        outdeg[a] += 1

    # topological order
    from collections import deque
    q = deque([i for i in range(n) if indeg[i] == 0])
    topo = []
    while q:
        v = q.popleft()
        topo.append(v)
        for to in g[v]:
            indeg[to] -= 1
            if indeg[to] == 0:
                q.append(to)
    if len(topo) != n:
        print("NO")
        return

    # earliest L
    L = [1] * n
    for v in topo:
        mx = 0
        for p in rg[v]:
            if L[p] > mx:
                mx = L[p]
        L[v] = mx + 1

    # latest R
    R = [T] * n
    for v in reversed(topo):
        mn = T + 1
        for to in g[v]:
            if R[to] - 1 < mn:
                mn = R[to] - 1
        if mn <= T:
            R[v] = mn
        else:
            R[v] = T

    for i in range(n):
        if L[i] > R[i] or L[i] > T or R[i] < 1:
            print("NO")
            return

    # sort vertices by L
    order = list(range(n))
    order.sort(key=lambda x: L[x])

    assign = [0] * n
    heap = []          # (R, vertex)
    ptr = 0
    for day in range(1, T + 1):
        while ptr < n and L[order[ptr]] <= day:
            v = order[ptr]
            heapq.heappush(heap, (R[v], v))
            ptr += 1
        cnt = 0
        while cnt < M and heap:
            r, v = heapq.heappop(heap)
            if r < day:
                print("NO")
                return
            assign[v] = day
            cnt += 1

    if any(a == 0 for a in assign):
        print("NO")
        return

    print("YES")
    print(' '.join(map(str, assign)))

if __name__ == "__main__":
    solve()