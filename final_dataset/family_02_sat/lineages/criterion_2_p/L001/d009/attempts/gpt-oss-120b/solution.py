import sys

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    N = 2 * n                     # total vertices
    g = [[] for _ in range(N)]    # forward graph
    rg = [[] for _ in range(N)]   # reverse graph

    def lit_node(v: int) -> int:
        """return vertex index of literal v (v>0 -> x_v, v<0 -> ¬x_|v|)"""
        if v > 0:
            return 2 * (v - 1) + 1   # true literal
        else:
            return 2 * (-v - 1)       # false literal

    for _ in range(m):
        a = next(it)
        b = next(it)
        A = lit_node(a)
        B = lit_node(b)
        NA = A ^ 1          # complement
        NB = B ^ 1
        # ¬A -> B
        g[NA].append(B)
        rg[B].append(NA)
        # ¬B -> A
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

    def rdfs(v: int, k: int):
        comp[v] = k
        for to in rg[v]:
            if comp[to] == -1:
                rdfs(to, k)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cur)
            cur += 1

    # check satisfiability
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return

    # build assignment
    ans = [0] * n
    for i in range(n):
        # true node index = 2*i+1, false = 2*i
        if comp[2 * i + 1] > comp[2 * i]:
            ans[i] = 1
        else:
            ans[i] = 0

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()