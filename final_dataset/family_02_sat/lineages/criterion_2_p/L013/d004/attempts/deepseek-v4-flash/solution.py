import sys
sys.setrecursionlimit(1 << 25)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # nodes: 0..n-1 for s_i=1, n..2n-1 for s_i=0

    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def node(var, val):
        # var: 0-based switch index, val: 0 or 1
        if val == 1:
            return var
        else:
            return n + var

    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)

    for _ in range(m):
        l1, l2 = map(int, input().split())
        a = abs(l1) - 1
        b = abs(l2) - 1
        t1 = 1 if l1 > 0 else 0
        t2 = 1 if l2 > 0 else 0

        x = node(a, t1)
        y = node(b, t2)

        # (x OR y) => (!x -> y) and (!y -> x)
        # !x is the opposite node of x
        nx = node(a, 1 - t1)
        ny = node(b, 1 - t2)

        add_imp(nx, y)
        add_imp(ny, x)

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

    # Check contradiction
    for i in range(n):
        if comp[i] == comp[n + i]:
            print("NO")
            return

    # Assign values: if comp[true_node] > comp[false_node], set true
    ans = []
    for i in range(n):
        if comp[i] > comp[n + i]:
            ans.append(1)
        else:
            ans.append(0)

    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()