import sys
sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def idx(var):
        # var: positive -> primary (True), negative -> secondary (False)
        # node for literal: 2*(abs(var)-1) + (0 if var>0 else 1)
        if var > 0:
            return 2 * (var - 1)
        else:
            return 2 * (-var - 1) + 1

    def add_imp(u, v):
        g[u].append(v)
        rg[v].append(u)

    for _ in range(m):
        a, b = map(int, input().split())
        # clause (a or b) => (!a -> b) and (!b -> a)
        na = idx(-a)
        nb = idx(-b)
        add_imp(na, idx(b))
        add_imp(nb, idx(a))

    # Kosaraju's SCC
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
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return

    # Build assignment
    assignment = [0] * n
    for i in range(n):
        # If comp[2*i] > comp[2*i+1], set True (primary)
        assignment[i] = 1 if comp[2*i] > comp[2*i+1] else 0

    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    solve()