import sys
sys.setrecursionlimit(1 << 25)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # nodes: 2*i for false, 2*i+1 for true

    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)

    # literal to node: positive x -> 2*(x-1)+1, negative -x -> 2*(x-1)
    def node(lit):
        if lit > 0:
            return 2 * (lit - 1) + 1
        else:
            return 2 * (-lit - 1)

    for _ in range(m):
        a, b = map(int, input().split())
        # clause (a or b) => (!a -> b) and (!b -> a)
        na = node(-a)
        nb = node(-b)
        add_imp(na, node(b))
        add_imp(nb, node(a))

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

    # Assign values: if comp[true_node] > comp[false_node], set true
    ans = []
    for i in range(n):
        if comp[2*i+1] > comp[2*i]:
            ans.append(1)
        else:
            ans.append(0)

    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()