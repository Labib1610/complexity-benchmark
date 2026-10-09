import sys
sys.setrecursionlimit(10**7)

def solve() -> None:
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges[u].append(v)
        edges[v].append(u)

    # compute subtree sizes and minimal possible total length
    parent = [-1] * n
    order = []
    stack = [0]
    parent[0] = -2
    while stack:
        v = stack.pop()
        order.append(v)
        for to in edges[v]:
            if parent[to] == -1:
                parent[to] = v
                stack.append(to)
    sz = [1] * n
    min_total = 0
    for v in reversed(order):
        for to in edges[v]:
            if parent[to] == v:
                sz[v] += sz[to]
                s = sz[to]
                min_total += min(s, n - s)
    if min_total > B:
        print("NO")
        return

    # construct arrangement achieving the minimal total
    # we will place the tree recursively, each subtree occupies a contiguous segment.
    # For each edge we will put the smaller side adjacent to the larger side to achieve min length.
    # We'll use a centroid decomposition to guarantee this.

    from collections import deque

    # find centroid
    def find_centroid():
        for v in order:
            ok = True
            max_part = n - sz[v]
            for to in edges[v]:
                if parent[to] == v:
                    max_part = max(max_part, sz[to])
            if max_part * 2 <= n:
                return v
        return 0

    centroid = find_centroid()

    # build layout
    pos = [0] * n
    cur = 1

    def dfs_place(v, p):
        nonlocal cur
        # place v at current position
        pos[v] = cur
        cur += 1
        # sort children so that smaller subtrees are placed first (they will be closer)
        childs = [to for to in edges[v] if to != p]
        childs.sort(key=lambda x: sz[x])
        for to in childs:
            dfs_place(to, v)

    # re-root tree at centroid to get correct subtree sizes
    parent = [-1] * n
    order = []
    stack = [centroid]
    parent[centroid] = -2
    while stack:
        v = stack.pop()
        order.append(v)
        for to in edges[v]:
            if parent[to] == -1:
                parent[to] = v
                stack.append(to)
    sz = [1] * n
    for v in reversed(order):
        for to in edges[v]:
            if parent[to] == v:
                sz[v] += sz[to]

    dfs_place(centroid, -1)

    # verify total length (optional, can be omitted for speed)
    total = 0
    for v in range(n):
        for to in edges[v]:
            if v < to:
                total += abs(pos[v] - pos[to])
    if total > B:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(pos[i]) for i in range(n)))

if __name__ == "__main__":
    solve()