import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # nodes: 0..n-1 for x_i, n..2n-1 for not x_i

    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def node(lit):
        # lit > 0 => x_lit, lit < 0 => not x_|lit|
        v = abs(lit) - 1
        if lit > 0:
            return v
        else:
            return v + n

    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)

    for _ in range(m):
        a, b = map(int, input().split())
        # (a OR b) => (!a -> b) and (!b -> a)
        add_imp(node(-a), node(b))
        add_imp(node(-b), node(a))

    # Kosaraju SCC
    visited = [False] * N
    order = []

    def dfs1(u):
        visited[u] = True
        for w in g[u]:
            if not visited[w]:
                dfs1(w)
        order.append(u)

    for i in range(N):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * N
    def dfs2(u, cid):
        comp[u] = cid
        for w in gr[u]:
            if comp[w] == -1:
                dfs2(w, cid)

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

    # Assign values: if comp[x_i] > comp[not x_i], then x_i = True
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