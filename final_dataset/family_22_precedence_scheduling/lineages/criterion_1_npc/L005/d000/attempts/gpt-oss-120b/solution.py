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

    if n > M * T:
        print("NO")
        return

    ready = deque([i for i in range(n) if indeg[i] == 0])
    time = [0] * n
    cur = 1
    processed = 0

    while cur <= T and ready:
        cnt = 0
        # schedule up to M tasks this slot
        while cnt < M and ready:
            v = ready.popleft()
            time[v] = cur
            processed += 1
            for nb in adj[v]:
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    ready.append(nb)
            cnt += 1
        cur += 1

    if processed == n:
        print("YES")
        print(' '.join(map(str, time)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()