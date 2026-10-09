import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # nodes: 0..n-1 for x_i, n..2n-1 for ¬x_i

    def node(var):
        # var > 0 => x_var, var < 0 => ¬x_|var|
        v = abs(var) - 1
        if var > 0:
            return v
        else:
            return v + n

    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    for _ in range(m):
        a, b = map(int, input().split())
        na = node(-a)
        nb = node(b)
        g[na].append(nb)
        rg[nb].append(na)

        nb2 = node(-b)
        na2 = node(a)
        g[nb2].append(na2)
        rg[na2].append(nb2)

    # Kosaraju's algorithm
    visited = [False] * N
    order = []

    def dfs1(u):
        visited[u] = True
        for v in g[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(N):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * N
    def dfs2(u, cid):
        comp[u] = cid
        for v in rg[u]:
            if comp[v] == -1:
                dfs2(v, cid)

    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1

    # Check satisfiability
    for i in range(n):
        if comp[i] == comp[i + n]:
            print("NO")
            return

    # Assign values: if comp[x] > comp[¬x] then x = True
    res = [0] * n
    for i in range(n):
        if comp[i] > comp[i + n]:
            res[i] = 1
        else:
            res[i] = 0

    print("YES")
    print(" ".join(map(str, res)))

if __name__ == "__main__":
    solve()