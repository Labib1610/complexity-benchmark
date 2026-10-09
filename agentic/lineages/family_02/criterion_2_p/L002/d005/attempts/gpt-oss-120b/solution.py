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
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def var_true(i):   # i is 0‑based
        return 2 * i + 1
    def var_false(i):
        return 2 * i

    def add_imp(u, v):
        g[u].append(v)
        rg[v].append(u)

    for _ in range(m):
        c1 = int(next(it))
        c2 = int(next(it))

        # literal for c: (var, is_true)
        def lit(c):
            idx = abs(c) - 1
            if c > 0:
                return var_true(idx)   # need true
            else:
                return var_false(idx)  # need false

        a = lit(c1)
        b = lit(c2)

        # clause (a OR b)  ->  (¬a → b) , (¬b → a)
        na = a ^ 1   # toggle last bit: true<->false
        nb = b ^ 1
        add_imp(na, b)
        add_imp(nb, a)

    # Kosaraju
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
        # component with larger number is earlier in topological order
        assignment[i] = 1 if comp[var_true(i)] > comp[var_false(i)] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()