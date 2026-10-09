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

    # topological order (Kahn)
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
        if earliest[i] > latest[i]:
            print("NO")
            return

    jobs = [(latest[i], earliest[i], i) for i in range(n)]
    jobs.sort()                     # by latest

    # DSU for next free minute
    parent = list(range(T + 2))     # 1..T, T+1 sentinel
    cap = [M] * (T + 2)             # capacity, extra element unused

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    ans = [0] * n
    for latest_v, earliest_v, idx in jobs:
        t = find(earliest_v)
        if t > latest_v or t > T:
            print("NO")
            return
        ans[idx] = t
        cap[t] -= 1
        if cap[t] == 0:
            parent[t] = find(t + 1)

    print("YES")
    print(' '.join(str(x) for x in ans))

if __name__ == "__main__":
    solve()