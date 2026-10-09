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

    def lit(x: int) -> int:
        """return node index for literal x (positive -> var true, negative -> var false)"""
        v = abs(x) - 1
        if x > 0:
            return 2 * v + 1   # true
        else:
            return 2 * v       # false

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        A = lit(a)
        B = lit(b)
        NA = A ^ 1  # negation
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

    def rdfs(v: int, label: int):
        comp[v] = label
        for to in rg[v]:
            if comp[to] == -1:
                rdfs(to, label)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cur)
            cur += 1

    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        # component with larger topological order (higher label) is earlier in reverse order,
        # so variable is true if comp[true] > comp[false]
        assignment[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()