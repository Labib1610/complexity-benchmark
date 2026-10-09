import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # each var has two nodes: 2*i for false, 2*i+1 for true
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)

    def node(var, val):
        # var: 1..n, val: True/False
        if val:
            return 2 * (var - 1) + 1
        else:
            return 2 * (var - 1)

    for _ in range(m):
        l1, l2 = map(int, input().split())
        # literal representation:
        # var = abs, is_true = (l > 0)
        def lit(l):
            var = abs(l)
            val = (l > 0)
            return node(var, val)
        a = lit(l1)
        b = lit(l2)
        # clause: a OR b => (not a -> b) and (not b -> a)
        add_imp(a ^ 1, b)
        add_imp(b ^ 1, a)

    # Kosaraju SCC
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

    # Check satisfiability
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return

    print("YES")
    assignment = [0] * n
    for i in range(n):
        # if true node comes after false node in topological order of SCC
        assignment[i] = 1 if comp[2*i] < comp[2*i+1] else 0
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    solve()