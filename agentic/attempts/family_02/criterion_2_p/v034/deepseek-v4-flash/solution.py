import sys
sys.setrecursionlimit(1 << 25)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)

    for _ in range(m):
        a, b = map(int, input().split())
        # literal encoding: x_i -> 2*i, ~x_i -> 2*i+1
        def lit(x):
            if x > 0:
                return 2 * (x - 1)
            else:
                return 2 * (-x - 1) + 1

        u = lit(a)
        v = lit(b)
        # (a or b) => (~a -> b) and (~b -> a)
        add_imp(u ^ 1, v)
        add_imp(v ^ 1, u)

    # Kosaraju
    visited = [False] * N
    order = []

    def dfs1(v):
        visited[v] = True
        for to in g[v]:
            if not visited[to]:
                dfs1(to)
        order.append(v)

    for i in range(N):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * N
    def dfs2(v, cid):
        comp[v] = cid
        for to in gr[v]:
            if comp[to] == -1:
                dfs2(to, cid)

    cid = 0
    for v in reversed(order):
        if comp[v] == -1:
            dfs2(v, cid)
            cid += 1

    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return

    print("YES")
    ans = []
    for i in range(n):
        # comp[2*i] > comp[2*i+1] means x_i is true
        ans.append('1' if comp[2 * i] > comp[2 * i + 1] else '0')
    print(' '.join(ans))

if __name__ == "__main__":
    solve()