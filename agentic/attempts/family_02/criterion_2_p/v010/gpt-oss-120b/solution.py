import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def idx(lit: int) -> int:
        """map literal to vertex index (0‑based)"""
        if lit > 0:
            return lit - 1          # x_i
        else:
            return (-lit - 1) + n   # ¬x_i

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        a_idx = idx(a)
        b_idx = idx(b)
        na = a_idx ^ n   # opposite literal (toggle between i and i+n)
        nb = b_idx ^ n
        # ¬a -> b
        g[na].append(b_idx)
        rg[b_idx].append(na)
        # ¬b -> a
        g[nb].append(a_idx)
        rg[a_idx].append(nb)

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

    def rdfs(v: int, label: int):
        comp[v] = label
        for to in rg[v]:
            if comp[to] == -1:
                rdfs(to, label)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cur)
            cur += 1

    # check satisfiability
    for i in range(n):
        if comp[i] == comp[i + n]:
            print("NO")
            return

    # build assignment
    ans = [0] * n
    for i in range(n):
        ans[i] = 1 if comp[i] > comp[i + n] else 0

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()