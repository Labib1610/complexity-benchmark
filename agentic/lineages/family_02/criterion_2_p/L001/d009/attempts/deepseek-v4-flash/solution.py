import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    # Variables: 0..n-1 for x_i false, n..2n-1 for x_i true
    # Node for literal: if v > 0: (v-1)*2 + 1 (true), if v < 0: (-v-1)*2 (false)
    g = [[] for _ in range(2 * n)]
    gr = [[] for _ in range(2 * n)]

    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)

    for _ in range(m):
        a, b = map(int, input().split())
        # literal index
        def lit(x):
            if x > 0:
                return (x - 1) * 2 + 1
            else:
                return (-x - 1) * 2
        la = lit(a)
        lb = lit(b)
        # clause (la OR lb) => (!la -> lb) and (!lb -> la)
        add_imp(la ^ 1, lb)
        add_imp(lb ^ 1, la)

    # Kosaraju SCC
    visited = [False] * (2 * n)
    order = []
    def dfs1(u):
        visited[u] = True
        for v in g[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * (2 * n)
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
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return

    print("YES")
    # assignment: if comp[false] > comp[true] then true else false
    res = []
    for i in range(n):
        if comp[2 * i] > comp[2 * i + 1]:
            res.append('1')
        else:
            res.append('0')
    print(' '.join(res))

if __name__ == "__main__":
    solve()