import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # nodes: 0..n-1 for x_i, n..2n-1 for ¬x_i

    def node(var):
        # var > 0 -> x_var, var < 0 -> ¬x_var
        if var > 0:
            return (var - 1) * 2
        else:
            return (-var - 1) * 2 + 1

    def neg_node(u):
        return u ^ 1

    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    for _ in range(m):
        a, b = map(int, input().split())
        u = node(a)
        v = node(b)
        # ¬a -> b
        g[neg_node(u)].append(v)
        rg[v].append(neg_node(u))
        # ¬b -> a
        g[neg_node(v)].append(u)
        rg[u].append(neg_node(v))

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
        for w in rg[u]:
            if comp[w] == -1:
                dfs2(w, cid)

    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1

    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return

    print("YES")
    # assignment: if comp[x] > comp[¬x] then True else False
    ans = []
    for i in range(n):
        if comp[2*i] > comp[2*i+1]:
            ans.append(1)
        else:
            ans.append(0)
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()