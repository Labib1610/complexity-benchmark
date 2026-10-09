import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # number of vertices
    g = [[] for _ in range(N)]   # forward graph
    rg = [[] for _ in range(N)]  # reversed graph

    def lit_to_idx(v: int) -> int:
        """map literal to vertex index"""
        var = abs(v) - 1
        if v > 0:                 # true literal
            return var * 2 + 1
        else:                     # false literal
            return var * 2

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        a = lit_to_idx(l1)
        b = lit_to_idx(l2)
        na = a ^ 1                 # negation
        nb = b ^ 1
        # ¬a -> b
        g[na].append(b)
        rg[b].append(na)
        # ¬b -> a
        g[nb].append(a)
        rg[a].append(nb)

    # ---------- Kosaraju ----------
    visited = [False] * N
    order = []

    def dfs1(v: int):
        visited[v] = True
        for to in g[v]:
            if not visited[to]:
                dfs1(to)
        order.append(v)

    for v in range(N):
        if not visited[v]:
            dfs1(v)

    comp = [-1] * N
    cur = 0

    def dfs2(v: int, label: int):
        comp[v] = label
        for to in rg[v]:
            if comp[to] == -1:
                dfs2(to, label)

    for v in reversed(order):
        if comp[v] == -1:
            dfs2(v, cur)
            cur += 1

    # ---------- check satisfiability ----------
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return

    # ---------- build assignment ----------
    ans = [0] * n
    for i in range(n):
        # true component larger => true
        ans[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()