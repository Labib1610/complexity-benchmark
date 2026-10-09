import sys
sys.setrecursionlimit(1 << 20)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # each variable x has two nodes: 2*i for False, 2*i+1 for True

    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def node(lit):
        # lit > 0: variable lit must be True -> node 2*(lit-1)+1
        # lit < 0: variable -lit must be False -> node 2*(-lit-1)
        if lit > 0:
            return 2 * (lit - 1) + 1
        else:
            return 2 * (-lit - 1)

    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)

    for _ in range(m):
        a, b = map(int, input().split())
        # (a OR b) => (!a -> b) and (!b -> a)
        na = -a
        nb = -b
        add_imp(node(na), node(b))
        add_imp(node(nb), node(a))

    # Kosaraju's SCC
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

    # Build assignment
    assignment = [0] * n
    for i in range(n):
        # If True node has higher comp id, set True
        assignment[i] = 1 if comp[2*i+1] > comp[2*i] else 0

    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    main()