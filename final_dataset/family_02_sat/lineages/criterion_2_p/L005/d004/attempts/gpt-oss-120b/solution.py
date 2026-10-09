import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    N = n * 2
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def var(i: int, val: bool) -> int:
        # val=True -> x_i, False -> ¬x_i
        return (i - 1) * 2 + (0 if val else 1)

    def add_imp(u: int, v: int):
        g[u].append(v)
        rg[v].append(u)

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        # literal conversion
        if l1 > 0:
            lit1 = (l1, True)   # x_l1
        else:
            lit1 = (-l1, False)  # ¬x_|l1|
        if l2 > 0:
            lit2 = (l2, True)
        else:
            lit2 = (-l2, False)

        a = var(lit1[0], lit1[1])
        na = var(lit1[0], not lit1[1])
        b = var(lit2[0], lit2[1])
        nb = var(lit2[0], not lit2[1])

        # clause (a OR b): add (¬a → b) and (¬b → a)
        add_imp(na, b)
        add_imp(nb, a)

    sys.setrecursionlimit(1 << 25)
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

    def rdfs(v: int, k: int):
        comp[v] = k
        for to in rg[v]:
            if comp[to] == -1:
                rdfs(to, k)

    k = 0
    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, k)
            k += 1

    assignment = [False] * (n + 1)
    for i in range(1, n + 1):
        if comp[var(i, True)] == comp[var(i, False)]:
            print("NO")
            return
        assignment[i] = comp[var(i, True)] > comp[var(i, False)]

    # output
    print("YES")
    print(' '.join('1' if assignment[i] else '0' for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()