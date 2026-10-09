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

    def var_true(i):   # node for x_i = True
        return 2 * i + 1

    def var_false(i):  # node for x_i = False
        return 2 * i

    def add_imp(u, v):
        g[u].append(v)
        rg[v].append(u)

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))

        # convert to literals (node index) representing "manifold active"
        # L positive -> B manifold -> active when x_i = 0 -> literal ¬x_i
        # L negative -> A manifold -> active when x_i = 1 -> literal x_i
        def literal(l):
            idx = abs(l) - 1
            if l < 0:          # A manifold -> x_i
                return var_true(idx)
            else:              # B manifold -> ¬x_i
                return var_false(idx)

        L1 = literal(l1)
        L2 = literal(l2)

        # ¬L1 node:
        notL1 = L1 ^ 1
        notL2 = L2 ^ 1

        # clauses: (¬L1) ∨ (¬L2)  =>  L1 -> ¬L2 , L2 -> ¬L1
        add_imp(L1, notL2)
        add_imp(L2, notL1)

    visited = [False] * N
    order = []

    def dfs(v):
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

    def rdfs(v, k):
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
        if comp[var_true(i)] == comp[var_false(i)]:
            print("NO")
            return
        # component with larger id comes earlier in topological order
        assignment[i] = 1 if comp[var_true(i)] > comp[var_false(i)] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()