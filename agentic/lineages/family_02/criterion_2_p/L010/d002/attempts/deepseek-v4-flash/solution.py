import sys
sys.setrecursionlimit(1 << 20)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # nodes: 0..n-1 for x_i, n..2n-1 for ¬x_i

    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def node(lit):
        # lit > 0: x_lit, lit < 0: ¬x_(-lit)
        v = abs(lit) - 1
        if lit > 0:
            return v
        else:
            return v + n

    def add_imp(u, v):
        g[u].append(v)
        rg[v].append(u)

    for _ in range(m):
        a, b = map(int, input().split())
        # (¬a -> b) and (¬b -> a)
        add_imp(node(-a), node(b))
        add_imp(node(-b), node(a))

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
    for i in range(n):
        if comp[i] == comp[i + n]:
            print("NO")
            return

    # Assign values: comp id order gives topological order (reverse)
    val = [False] * n
    for i in range(n):
        # If ¬x_i appears later in topological order (higher comp id), set x_i True
        val[i] = comp[i] > comp[i + n]

    print("YES")
    print(" ".join("1" if v else "0" for v in val))

if __name__ == "__main__":
    main()