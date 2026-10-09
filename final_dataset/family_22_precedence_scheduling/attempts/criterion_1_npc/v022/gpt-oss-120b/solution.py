import sys
from collections import deque, defaultdict

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
    indeg = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        indeg[b] += 1

    # Kahn to get topological order and compute longest path rank
    q = deque([i for i in range(n) if indeg[i] == 0])
    rank = [1] * n
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        ru = rank[u]
        for v in adj[u]:
            if rank[v] < ru + 1:
                rank[v] = ru + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if len(topo) != n:
        print("NO")
        return

    if max(rank) > T or n > M * T:
        print("NO")
        return

    buckets = [[] for _ in range(T + 2)]
    for i, r in enumerate(rank):
        buckets[r].append(i)

    pending = deque()
    day_of = [0] * n
    scheduled = 0

    for day in range(1, T + 1):
        # add newly available tasks
        for v in buckets[day]:
            pending.append(v)
        # schedule up to M tasks
        cnt = 0
        while pending and cnt < M:
            v = pending.popleft()
            day_of[v] = day
            cnt += 1
            scheduled += 1
        # continue

    if scheduled == n:
        print("YES")
        print(' '.join(str(day_of[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()