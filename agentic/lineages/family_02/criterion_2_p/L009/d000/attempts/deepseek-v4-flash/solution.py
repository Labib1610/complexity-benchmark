import sys
sys.setrecursionlimit(1 << 20)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # nodes: 0..n-1 for x_i true, n..2n-1 for x_i false

    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)

    def node(var):
        # var > 0: x_var true -> index var-1
        # var < 0: x_var false -> index n + (-var) - 1
        if var > 0:
            return var - 1
        else:
            return n + (-var) - 1

    def neg_node(u):
        # negate the literal
        if u < n:
            return u + n
        else:
            return u - n

    for _ in range(m):
        a, b = map(int, input().split())
        u = node(a)
        v = node(b)
        # (a OR b) => (!a -> b) and (!b -> a)
        add_imp(neg_node(u), v)
        add_imp(neg_node(v), u)

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

    # Assign values: if comp[x] > comp[!x] then x = True
    ans = [0] * n
    for i in range(n):
        ans[i] = 1 if comp[i] > comp[i + n] else 0

    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()