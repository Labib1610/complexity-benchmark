import sys
sys.setrecursionlimit(1 << 20)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # nodes: 0..n-1 for x_i false, n..2n-1 for x_i true

    # variable mapping:
    # literal i (positive) -> node (i-1) + n
    # literal -i (negative) -> node (i-1)
    def node(lit):
        if lit > 0:
            return (lit - 1) + n
        else:
            return (-lit - 1)

    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    for _ in range(m):
        a, b = map(int, input().split())
        u = node(a)
        v = node(b)
        # clause (a OR b) => (!a -> b) and (!b -> a)
        # negation of literal a:
        na = node(-a)
        nb = node(-b)
        g[na].append(v)
        gr[v].append(na)
        g[nb].append(u)
        gr[u].append(nb)

    # Kosaraju SCC
    visited = [False] * N
    order = []

    def dfs1(v):
        visited[v] = True
        for w in g[v]:
            if not visited[w]:
                dfs1(w)
        order.append(v)

    for v in range(N):
        if not visited[v]:
            dfs1(v)

    comp = [-1] * N
    def dfs2(v, cid):
        comp[v] = cid
        for w in gr[v]:
            if comp[w] == -1:
                dfs2(w, cid)

    cid = 0
    for v in reversed(order):
        if comp[v] == -1:
            dfs2(v, cid)
            cid += 1

    # Check satisfiability
    for i in range(n):
        if comp[i] == comp[i + n]:
            print("NO")
            return

    # Assign values: in Kosaraju, comp id order is reverse topological of SCC DAG.
    # If comp[true_i] > comp[false_i], set true; else false.
    res = [0] * n
    for i in range(n):
        # true node = i+n, false node = i
        if comp[i + n] > comp[i]:
            res[i] = 1
        else:
            res[i] = 0

    print("YES")
    print(" ".join(map(str, res)))

if __name__ == "__main__":
    main()