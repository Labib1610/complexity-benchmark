import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def node(var):
        # var > 0: drone var is True -> node 2*var+1
        # var < 0: drone -var is False -> node 2*(-var)
        if var > 0:
            return 2 * var + 1
        else:
            return 2 * (-var)

    def neg_node(var):
        if var > 0:
            return 2 * var
        else:
            return 2 * (-var) + 1

    for _ in range(m):
        a, b = map(int, input().split())
        # (a OR b) => (¬a -> b) and (¬b -> a)
        u = neg_node(a)
        v = node(b)
        g[u].append(v)
        rg[v].append(u)

        u = neg_node(b)
        v = node(a)
        g[u].append(v)
        rg[v].append(u)

    # Kosaraju's SCC
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

    # Check satisfiability
    for i in range(1, n + 1):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return

    # Assign values: in SCC order, if comp[true] < comp[false] => true
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        # comp[2*i] is false node, comp[2*i+1] is true node
        res[i] = 1 if comp[2 * i + 1] < comp[2 * i] else 0

    print("YES")
    print(" ".join(map(str, res[1:])))

if __name__ == "__main__":
    solve()