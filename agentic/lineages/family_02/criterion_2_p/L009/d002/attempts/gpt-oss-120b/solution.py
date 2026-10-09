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

    def lit_to_node(l: int) -> int:
        v = abs(l) - 1
        if l > 0:
            return 2 * v          # xi = True
        else:
            return 2 * v + 1      # xi = False (¬xi)

    def add_imp(u: int, v: int):
        g[u].append(v)
        rg[v].append(u)

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        u = lit_to_node(a)
        v = lit_to_node(b)
        nu = u ^ 1
        nv = v ^ 1
        add_imp(nu, v)   # ¬a -> b
        add_imp(nv, u)   # ¬b -> a

    visited = [False] * N
    order = []

    def dfs(v: int):
        visited[v] = True
        for to in g[v]:
            if not visited[to]:
                dfs(to)
        order.append(v)

    for i in range(N):
        if not visited[i]:
            dfs(i)

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
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        assignment[i] = 1 if comp[2 * i] > comp[2 * i + 1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()