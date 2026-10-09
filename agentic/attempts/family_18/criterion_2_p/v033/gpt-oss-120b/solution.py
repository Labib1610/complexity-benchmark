import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); B = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # find centroid
    size = [0] * n
    parent = [-1] * n
    order = []
    stack = [0]
    parent[0] = -2
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            stack.append(v)
    for u in reversed(order):
        sz = 1
        for v in adj[u]:
            if v == parent[u]:
                continue
            sz += size[v]
        size[u] = sz

    centroid = 0
    best = n
    for u in range(n):
        max_part = n - size[u]
        for v in adj[u]:
            if v == parent[u]:
                continue
            max_part = max(max_part, size[v])
        if max_part < best:
            best = max_part
            centroid = u

    # BFS order starting from centroid
    from collections import deque
    bfs = []
    q = deque([centroid])
    seen = [False] * n
    seen[centroid] = True
    while q:
        u = q.popleft()
        bfs.append(u)
        for v in adj[u]:
            if not seen[v]:
                seen[v] = True
                q.append(v)

    # rotate so centroid is at middle (floor((n+1)/2) position, 1‑based)
    target_idx = (n - 1) // 2  # 0‑based
    cur_idx = bfs.index(centroid)
    shift = target_idx - cur_idx
    bfs = bfs[shift:] + bfs[:shift] if shift >= 0 else bfs[shift:] + bfs[:shift]

    pos = [0] * n
    for idx, node in enumerate(bfs):
        pos[node] = idx + 1  # positions are 1‑based

    total = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                total += abs(pos[u] - pos[v])
    if total <= B:
        print("YES")
        print(' '.join(str(pos[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()