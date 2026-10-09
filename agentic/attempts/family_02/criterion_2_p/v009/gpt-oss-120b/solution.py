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

    def lit_node(l: int) -> int:
        v = abs(l) - 1
        return 2 * v + (1 if l > 0 else 0)

    for _ in range(m):
        a = int(next(it)); b = int(next(it))
        na = lit_node(-a)
        nb = lit_node(-b)
        a_node = lit_node(a)
        b_node = lit_node(b)
        # ~a -> b
        g[na].append(b_node)
        rg[b_node].append(na)
        # ~b -> a
        g[nb].append(a_node)
        rg[a_node].append(nb)

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
        assignment[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()