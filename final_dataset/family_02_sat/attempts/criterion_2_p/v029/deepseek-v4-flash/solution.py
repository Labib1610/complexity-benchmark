import sys
sys.setrecursionlimit(1 << 20)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # nodes: 2*i = false, 2*i+1 = true

    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)

    for _ in range(m):
        a, b = map(int, input().split())
        # a: if a > 0 then var = a-1 must be true, else var = -a-1 must be false
        # clause: (a) OR (b)
        # implication: not a -> b, not b -> a
        def lit(x):
            if x > 0:
                return 2 * (x - 1) + 1  # true
            else:
                return 2 * (-x - 1)     # false

        la = lit(a)
        lb = lit(b)
        # not a -> b
        add_imp(la ^ 1, lb)
        # not b -> a
        add_imp(lb ^ 1, la)

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
    comp_id = 0

    def dfs2(u):
        comp[u] = comp_id
        for v in gr[u]:
            if comp[v] == -1:
                dfs2(v)

    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u)
            comp_id += 1

    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return

    print("YES")
    # assignment: if comp[true] > comp[false] then true
    res = []
    for i in range(n):
        if comp[2 * i + 1] > comp[2 * i]:
            res.append('1')
        else:
            res.append('0')
    print(' '.join(res))

if __name__ == "__main__":
    main()