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
    indeg = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        indeg[b] += 1

    # topological order, compute lo (earliest slot)
    q = deque([i for i in range(n) if indeg[i] == 0])
    lo = [1] * n
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for to in adj[v]:
            if lo[v] + 1 > lo[to]:
                lo[to] = lo[v] + 1
            indeg[to] -= 1
            if indeg[to] == 0:
                q.append(to)

    if len(order) != n:
        print("NO")
        return

    if any(lo[v] > T for v in range(n)):
        print("NO")
        return

    # sort jobs by lo
    jobs = list(range(n))
    jobs.sort(key=lambda x: lo[x])

    # capacity per slot
    free = [M] * (T + 1)          # 1‑based, ignore index 0
    slot = [0] * n
    ptr = 1

    for v in jobs:
        if ptr < lo[v]:
            ptr = lo[v]
        while ptr <= T and free[ptr] == 0:
            ptr += 1
        if ptr > T:
            print("NO")
            return
        slot[v] = ptr
        free[ptr] -= 1

    # all jobs placed
    out = ["YES"]
    out.append(" ".join(str(slot[i]) for i in range(n)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()