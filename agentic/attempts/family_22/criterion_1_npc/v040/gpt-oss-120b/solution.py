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
    indeg = [0] * n
    rev = [[] for _ in range(n)]          # predecessors
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        rev[b].append(a)
        indeg[b] += 1

    # Kahn topological sort
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

    # Union‑find structure to skip full layers
    parent = list(range(T + 2))   # 1..T, T+1 is sentinel

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def occupy(x):
        # mark layer x as full, link to next
        parent[x] = find(x + 1)

    cap = [M] * (T + 1)   # 1‑based
    layer = [0] * n

    max_pred = [0] * n  # store max layer of predecessors processed so far

    for v in topo:
        need = max_pred[v] + 1
        if need > T:
            print("NO")
            return
        pos = find(need)
        if pos > T:
            print("NO")
            return
        # assign
        layer[v] = pos
        cap[pos] -= 1
        if cap[pos] == 0:
            occupy(pos)
        # update successors' max_pred
        for to in adj[v]:
            if layer[v] > max_pred[to]:
                max_pred[to] = layer[v]

    # all assigned
    print("YES")
    print(' '.join(str(layer[i]) for i in range(n)))

if __name__ == "__main__":
    solve()