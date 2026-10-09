import sys
sys.setrecursionlimit(1 << 25)

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
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        radj[b].append(a)
        indeg[b] += 1

    # Kahn topological order
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

    # longest path to end (len_to_end)
    len_to_end = [1] * n
    for v in reversed(topo):
        for to in adj[v]:
            if len_to_end[v] < len_to_end[to] + 1:
                len_to_end[v] = len_to_end[to] + 1

    latest = [0] * n
    for v in range(n):
        latest[v] = T - (len_to_end[v] - 1)
        if earliest[v] > latest[v]:
            print("NO")
            return

    # jobs list
    jobs = [(latest[i], earliest[i], i) for i in range(n)]
    jobs.sort()  # by latest

    # DSU for next free time
    parent = list(range(T + 2))   # 1..T, T+1 sentinel
    cap = [M] * (T + 2)

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    assign = [0] * n
    for dl, el, idx in jobs:
        t = find(el)
        if t > dl or t > T:
            print("NO")
            return
        assign[idx] = t
        cap[t] -= 1
        if cap[t] == 0:
            parent[t] = find(t + 1)

    print("YES")
    print(' '.join(str(assign[i]) for i in range(n)))

if __name__ == "__main__":
    solve()