import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # node count
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def node(var: int, val: int) -> int:
        """literal node: var in [0..n-1], val in {0,1}"""
        return var * 2 + val

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        a = abs(l1) - 1
        b = abs(l2) - 1
        f1 = 1 if l1 < 0 else 0
        f2 = 1 if l2 < 0 else 0
        # clause: (s[a] = not f1) OR (s[b] = not f2)
        va = 1 - f1
        vb = 1 - f2

        # (a = not va) -> (b = vb)
        u = node(a, 1 - va)
        v = node(b, vb)
        g[u].append(v)
        rg[v].append(u)

        # (b = not vb) -> (a = va)
        u = node(b, 1 - vb)
        v = node(a, va)
        g[u].append(v)
        rg[v].append(u)

    # Kosaraju
    visited = [False] * N
    order = []

    def dfs(v: int):
        visited[v] = True
        for to in g[v]:
            if not visited[to]:
                dfs(to)
        order.append(v)

    for v in range(N):
        if not visited[v]:
            dfs(v)

    comp = [-1] * N
    cur = 0

    def rdfs(v: int, k: int):
        comp[v] = k
        for to in rg[v]:
            if comp[to] == -1:
                rdfs(to, k)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cur)
            cur += 1

    assignment = [0] * n
    for i in range(n):
        if comp[node(i, 0)] == comp[node(i, 1)]:
            print("NO")
            return
        assignment[i] = 1 if comp[node(i, 1)] > comp[node(i, 0)] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()