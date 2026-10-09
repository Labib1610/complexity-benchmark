import sys
sys.setrecursionlimit(1 << 25)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # nodes: 0..n-1 for x_i, n..2n-1 for ¬x_i

    def node(lit):
        # lit is int, positive means x, negative means ¬x
        if lit > 0:
            return (lit - 1) * 2      # even index for x
        else:
            return (-lit - 1) * 2 + 1 # odd index for ¬x

    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    for _ in range(m):
        a, b = map(int, input().split())
        u = node(a)
        v = node(b)
        # ¬a -> b
        g[u ^ 1].append(v)
        gr[v].append(u ^ 1)
        # ¬b -> a
        g[v ^ 1].append(u)
        gr[u].append(v ^ 1)

    # Kosaraju
    visited = [False] * N
    order = []

    def dfs1(v):
        visited[v] = True
        for to in g[v]:
            if not visited[to]:
                dfs1(to)
        order.append(v)

    for i in range(N):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * N
    def dfs2(v, cid):
        comp[v] = cid
        for to in gr[v]:
            if comp[to] == -1:
                dfs2(to, cid)

    cid = 0
    for v in reversed(order):
        if comp[v] == -1:
            dfs2(v, cid)
            cid += 1

    # Check contradiction
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return

    # Assign values: if comp[x] > comp[¬x] then x = True
    ans = [0] * n
    for i in range(n):
        ans[i] = 1 if comp[2*i] > comp[2*i+1] else 0

    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    solve()