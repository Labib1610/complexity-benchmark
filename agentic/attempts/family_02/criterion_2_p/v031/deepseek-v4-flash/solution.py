import sys
sys.setrecursionlimit(1 << 20)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # nodes: 0..n-1 for x_i, n..2n-1 for ¬x_i

    def node(lit):
        # lit > 0: x_lit -> index lit-1
        # lit < 0: ¬x_|lit| -> index n + |lit| - 1
        if lit > 0:
            return lit - 1
        else:
            return n + (-lit) - 1

    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    for _ in range(m):
        a, b = map(int, input().split())
        # (a OR b)
        # ¬a -> b
        u = node(-a)
        v = node(b)
        g[u].append(v)
        gr[v].append(u)
        # ¬b -> a
        u = node(-b)
        v = node(a)
        g[u].append(v)
        gr[v].append(u)

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
        for w in gr[u]:
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

    # Assign values: in Kosaraju, comp id order is reverse topological.
    # If comp[x] > comp[¬x], then x is true.
    ans = [0] * n
    for i in range(n):
        ans[i] = 1 if comp[i] > comp[i + n] else 0

    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()