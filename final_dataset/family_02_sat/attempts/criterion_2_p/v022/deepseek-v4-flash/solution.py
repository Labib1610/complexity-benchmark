import sys
sys.setrecursionlimit(1 << 20)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def node(var, val):
        # var: 1-based, val: 0 or 1
        # returns node index for (var == val)
        return (var - 1) * 2 + val

    for _ in range(m):
        a, b = map(int, input().split())
        # a: literal, positive means var=1, negative means var=0
        # clause: (a) OR (b)
        # implication: not a -> b, not b -> a
        va = abs(a)
        va_val = 1 if a > 0 else 0
        vb = abs(b)
        vb_val = 1 if b > 0 else 0

        na = node(va, va_val ^ 1)
        nb = node(vb, vb_val)
        g[na].append(nb)
        rg[nb].append(na)

        na2 = node(vb, vb_val ^ 1)
        nb2 = node(va, va_val)
        g[na2].append(nb2)
        rg[nb2].append(na2)

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
        for v in rg[u]:
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
        # In Kosaraju, comp id order is topological for SCC DAG
        # If comp[2*i] > comp[2*i+1], then var is true
        assignment[i] = 1 if comp[2*i] > comp[2*i+1] else 0

    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    main()