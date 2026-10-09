import sys
sys.setrecursionlimit(1 << 25)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # nodes: 2*i for x_i false, 2*i+1 for x_i true

    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)

    def node(var):
        # var > 0: x_var, var < 0: not x_|var|
        v = abs(var) - 1
        if var > 0:
            return 2 * v + 1  # true
        else:
            return 2 * v      # false

    for _ in range(m):
        a, b = map(int, input().split())
        # clause: (a_lit OR b_lit)
        # implication: ¬a -> b, ¬b -> a
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

    # Build assignment: choose value based on SCC order
    assignment = [0] * n
    for i in range(n):
        # If comp[false] > comp[true], then false is "later" in topological order => assign true
        assignment[i] = 1 if comp[2*i] > comp[2*i+1] else 0

    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    solve()