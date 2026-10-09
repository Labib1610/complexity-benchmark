import sys
sys.setrecursionlimit(1 << 25)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # nodes: 0..n-1 for x, n..2n-1 for ~x

    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def idx(lit):
        # lit is int, positive => x, negative => ~x
        var = abs(lit) - 1
        if lit > 0:
            return var
        else:
            return var + n

    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)

    for _ in range(m):
        a, b = map(int, input().split())
        # clause (a OR b) => (~a -> b) and (~b -> a)
        add_imp(idx(-a), idx(b))
        add_imp(idx(-b), idx(a))

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
        if comp[i] == comp[i + n]:
            print("NO")
            return

    # Assign values: if comp[x] > comp[~x] => true
    ans = [0] * n
    for i in range(n):
        ans[i] = 1 if comp[i] > comp[i + n] else 0

    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()