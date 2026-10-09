import sys

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # total vertices
    g = [[] for _ in range(N)]    # forward graph
    rg = [[] for _ in range(N)]   # reversed graph

    def idx(var: int, val: int) -> int:
        """return vertex index for variable var (1‑based) with value val (0/1)"""
        return 2 * (var - 1) + val

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))

        # literal a
        var_a = abs(a)
        val_a = 1 if a > 0 else 0          # a is true when variable = val_a
        lit_a = idx(var_a, val_a)
        not_a = idx(var_a, 1 - val_a)

        # literal b
        var_b = abs(b)
        val_b = 1 if b > 0 else 0
        lit_b = idx(var_b, val_b)
        not_b = idx(var_b, 1 - val_b)

        # add implications ¬a → b , ¬b → a
        g[not_a].append(lit_b)
        rg[lit_b].append(not_a)

        g[not_b].append(lit_a)
        rg[lit_a].append(not_b)

    # ---------- Kosaraju ----------
    visited = [False] * N
    order = []

    sys.setrecursionlimit(1 << 25)

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

    # ---------- check satisfiability ----------
    assignment = [0] * n
    for var in range(1, n + 1):
        f = idx(var, 0)
        t = idx(var, 1)
        if comp[f] == comp[t]:
            print("NO")
            return
        # component with larger number appears earlier in topological order
        assignment[var - 1] = 1 if comp[t] > comp[f] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()