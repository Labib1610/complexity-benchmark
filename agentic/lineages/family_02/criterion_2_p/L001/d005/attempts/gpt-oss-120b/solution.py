import sys

sys.setrecursionlimit(1 << 25)

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

    def var(i: int) -> int:
        """return index of literal y_i (True)"""
        return 2 * (i - 1)

    def neg(x: int) -> int:
        return x ^ 1

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        a = abs(l1)
        b = abs(l2)
        # literal for l1
        lit1 = var(a) if l1 > 0 else neg(var(a))
        # literal for l2
        lit2 = var(b) if l2 > 0 else neg(var(b))
        # clause (lit1 OR lit2) => (~lit1 -> lit2) and (~lit2 -> lit1)
        g[neg(lit1)].append(lit2)
        rg[lit2].append(neg(lit1))
        g[neg(lit2)].append(lit1)
        rg[lit1].append(neg(lit2))

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

    assignment = [0] * n
    for i in range(1, n + 1):
        if comp[var(i)] == comp[neg(var(i))]:
            print("NO")
            return
        assignment[i - 1] = 1 if comp[var(i)] > comp[neg(var(i))] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()