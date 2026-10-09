import sys

sys.setrecursionlimit(1_000_000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # number of vertices
    g = [[] for _ in range(N)]    # implication graph
    rg = [[] for _ in range(N)]   # reversed graph

    def lit_to_node(l: int) -> int:
        v = abs(l) - 1            # 0‑based variable index
        if l > 0:
            return 2 * v + 1      # x_v  (true)
        else:
            return 2 * v          # ¬x_v (false)

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        a_node = lit_to_node(a)
        b_node = lit_to_node(b)
        na = a_node ^ 1           # negation of a
        nb = b_node ^ 1           # negation of b

        # ¬a → b
        g[na].append(b_node)
        rg[b_node].append(na)

        # ¬b → a
        g[nb].append(a_node)
        rg[a_node].append(nb)

    # ---------- Kosaraju ----------
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
    label = 0

    def rdfs(v: int, lbl: int):
        comp[v] = lbl
        for to in rg[v]:
            if comp[to] == -1:
                rdfs(to, lbl)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, label)
            label += 1

    # ---------- Check satisfiability ----------
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return

    # ---------- Build assignment ----------
    ans = [0] * n
    for i in range(n):
        ans[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    print("YES")
    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    solve()