import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        indeg[b] += 1

    # Kahn's algorithm with layers (longest path from sources)
    q = deque()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)

    day = [0] * (n + 1)
    processed = 0
    while q:
        u = q.popleft()
        processed += 1
        for v in adj[u]:
            if day[v] < day[u] + 1:
                day[v] = day[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if processed != n:
        print("NO")
        return

    max_day = max(day[1:]) if n > 0 else 0
    if max_day >= T:
        print("NO")
        return

    # Check capacity constraint: count crates per day
    cnt = [0] * (T + 1)
    for i in range(1, n + 1):
        cnt[day[i] + 1] += 1  # shift to 1-indexed days

    for d in range(1, T + 1):
        if cnt[d] > M:
            print("NO")
            return

    out = [str(day[i] + 1) for i in range(1, n + 1)]
    print("YES")
    print(" ".join(out))

solve()