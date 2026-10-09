import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # nodes: 0..n-1 for x_i, n..2n-1 for ¬x_i

    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)

    # literal mapping: positive x -> index (x-1), negative -> n + (abs(x)-1)
    for _ in range(m):
        a, b = map(int, input().split())
        # (a OR b)
        # ¬a -> b
        # ¬b -> a
        ua = a - 1 if a > 0 else n + (-a) - 1
        ub = b - 1 if b > 0 else n + (-b) - 1
        na = n + (a - 1) if a > 0 else (-a) - 1
        nb = n + (b - 1) if b > 0 else (-b) - 1
        add_imp(na, ub)
        add_imp(nb, ua)

    # Kosaraju
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
        for v in gr[u]:
            if comp[v] == -1:
                dfs2(v, cid)

    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1

    for i in range(n):
        if comp[i] == comp[i + n]:
            print("NO")
            return

    # Assign values: if comp[x] > comp[¬x] then x = True
    ans = [0] * n
    for i in range(n):
        ans[i] = 1 if comp[i] > comp[i + n] else 0

    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    solve()