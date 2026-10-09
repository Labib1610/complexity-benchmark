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

    if n > T * M:
        print("NO")
        return

    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        indeg[v] += 1

    # DSU for days 1..T+1 (indexing 1-based for days)
    parent = list(range(T + 2))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> None:
        x = find(x)
        y = find(y)
        if x != y:
            parent[x] = y

    used = [0] * (T + 2)          # used[day]
    pred_max = [0] * n            # max day of processed predecessors
    day = [0] * n                 # answer

    from collections import deque
    q = deque([i for i in range(n) if indeg[i] == 0])

    processed = 0
    while q:
        v = q.popleft()
        earliest = pred_max[v] + 1
        d = find(earliest)
        if d > T:
            print("NO")
            return
        day[v] = d
        used[d] += 1
        if used[d] == M:
            union(d, d + 1)

        for w in adj[v]:
            if d > pred_max[w]:
                pred_max[w] = d
            indeg[w] -= 1
            if indeg[w] == 0:
                q.append(w)
        processed += 1

    if processed != n:
        # cycle
        print("NO")
        return

    print("YES")
    print(' '.join(str(day[i]) for i in range(n)))

if __name__ == "__main__":
    solve()