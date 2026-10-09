import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    # 2-SAT: variable i (0-index) -> node 2*i (false), 2*i+1 (true)
    N = 2 * n
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)

    def add_clause(a, va, b, vb):
        # (a == va) OR (b == vb)
        # equivalent to (a != va) -> (b == vb) and (b != vb) -> (a == va)
        # node for x is 2*x + (1 if true else 0)
        na = 2 * a + (1 if va else 0)
        nb = 2 * b + (1 if vb else 0)
        # not a -> b
        add_imp(na ^ 1, nb)
        # not b -> a
        add_imp(nb ^ 1, na)

    for _ in range(m):
        l1, l2 = map(int, input().split())
        a = abs(l1) - 1
        b = abs(l2) - 1
        va = 1 if l1 > 0 else 0
        vb = 1 if l2 > 0 else 0
        add_clause(a, va, b, vb)

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

    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return

    # Assign values: if comp[2*i] > comp[2*i+1] then true
    res = []
    for i in range(n):
        if comp[2*i] > comp[2*i+1]:
            res.append(1)
        else:
            res.append(0)

    print("YES")
    print(" ".join(map(str, res)))

if __name__ == "__main__":
    solve()