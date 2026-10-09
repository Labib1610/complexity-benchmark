import sys

sys.setrecursionlimit(1_000_000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # total vertices
    g = [[] for _ in range(N)]   # forward graph
    rg = [[] for _ in range(N)]  # reversed graph

    def lit(x: int) -> int:
        """return vertex index of literal x (positive -> true, negative -> false)"""
        v = abs(x) - 1
        if x > 0:
            return 2 * v          # true
        else:
            return 2 * v + 1      # false

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        A = lit(a)
        B = lit(b)
        NA = A ^ 1                 # negation
        NB = B ^ 1
        # ¬a → b
        g[NA].append(B)
        rg[B].append(NA)
        # ¬b → a
        g[NB].append(A)
        rg[A].append(NB)

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

    def rdfs(v: int, cid: int):
        comp[v] = cid
        for to in rg[v]:
            if comp[to] == -1:
                rdfs(to, cid)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cur)
            cur += 1

    assignment = [0] * n
    for i in range(n):
        t = 2 * i
        f = t + 1
        if comp[t] == comp[f]:
            print("NO")
            return
        assignment[i] = 1 if comp[t] > comp[f] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()