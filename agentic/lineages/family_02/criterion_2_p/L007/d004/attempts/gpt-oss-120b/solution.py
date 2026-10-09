import sys

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

    def lit_node(lit: int) -> int:
        """return node index for literal lit (positive means true, negative means false)"""
        v = abs(lit) - 1
        if lit > 0:
            return 2 * v + 1          # true
        else:
            return 2 * v               # false

    def add_imp(u: int, v: int) -> None:
        g[u].append(v)
        rg[v].append(u)

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        na = lit_node(a)
        nb = lit_node(b)
        na_neg = na ^ 1
        nb_neg = nb ^ 1
        # (a ∨ b) => (¬a → b) and (¬b → a)
        add_imp(na_neg, nb)
        add_imp(nb_neg, na)

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

    def rdfs(v: int, cid: int):
        comp[v] = cid
        for to in rg[v]:
            if comp[to] == -1:
                rdfs(to, cid)

    cid = 0
    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cid)
            cid += 1

    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        # component with larger id comes earlier in topological order
        assignment[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()