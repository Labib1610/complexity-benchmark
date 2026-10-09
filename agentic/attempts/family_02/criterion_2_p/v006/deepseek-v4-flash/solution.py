import sys
sys.setrecursionlimit(1 << 25)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def node(lit):
        # lit is nonzero int
        if lit > 0:
            return 2 * (lit - 1)       # x_i
        else:
            return 2 * (-lit - 1) + 1  # ¬x_i

    def neg(u):
        return u ^ 1

    for _ in range(m):
        a, b = map(int, input().split())
        u = node(a)
        v = node(b)
        # (a OR b) => (¬a -> b) and (¬b -> a)
        g[neg(u)].append(v)
        gr[v].append(neg(u))
        g[neg(v)].append(u)
        gr[u].append(neg(v))

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

    # Assign values: in topological order, if comp[x] > comp[¬x] then x is true
    ans = [0] * n
    for i in range(n):
        # comp[2*i] is x_i, comp[2*i+1] is ¬x_i
        ans[i] = 1 if comp[2*i] > comp[2*i+1] else 0

    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()