import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # nodes: 2*i = false, 2*i+1 = true

    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)

    # variable i: 0..n-1
    # node for x_i true: 2*i+1
    # node for x_i false: 2*i

    for _ in range(m):
        l1, l2 = map(int, input().split())
        a = abs(l1) - 1
        b = abs(l2) - 1
        sign1 = 1 if l1 > 0 else 0
        sign2 = 1 if l2 > 0 else 0

        # Clause: (x_a == sign1) OR (x_b == sign2)
        # Equivalent implications:
        # (x_a != sign1) -> (x_b == sign2)
        # (x_b != sign2) -> (x_a == sign1)

        # node for (x == val): 2*var + val
        # node for (x != val): 2*var + (1-val)

        na = 2*a + sign1
        nb = 2*b + sign2
        not_na = 2*a + (1 - sign1)
        not_nb = 2*b + (1 - sign2)

        add_imp(not_na, nb)
        add_imp(not_nb, na)

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

    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return

    print("YES")
    res = []
    for i in range(n):
        # If false node has higher comp id, assign true (standard 2-SAT assignment)
        if comp[2*i] > comp[2*i+1]:
            res.append('1')
        else:
            res.append('0')
    print(' '.join(res))

if __name__ == "__main__":
    solve()