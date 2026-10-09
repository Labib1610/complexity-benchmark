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

    def var_id(v: int, val: int) -> int:
        """return node index for variable v (1‑based) being val (0/1)"""
        return (v - 1) * 2 + (0 if val == 0 else 1)

    def add_imp(u: int, v: int):
        g[u].append(v)
        rg[v].append(u)

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        i = abs(l1)
        j = abs(l2)
        t1 = 1 if l1 > 0 else 0
        t2 = 1 if l2 > 0 else 0

        # clause: (x_i == t1) OR (x_j == t2)
        # literals:
        a = var_id(i, t1)          # A
        nota = var_id(i, 1 - t1)   # ¬A
        b = var_id(j, t2)          # B
        notb = var_id(j, 1 - t2)   # ¬B

        # add (¬A → B) and (¬B → A)
        add_imp(nota, b)
        add_imp(notb, a)

    # Kosaraju
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

    assignment = [0] * n
    for i in range(1, n + 1):
        if comp[var_id(i, 0)] == comp[var_id(i, 1)]:
            print("NO")
            return
        assignment[i - 1] = 1 if comp[var_id(i, 1)] > comp[var_id(i, 0)] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()