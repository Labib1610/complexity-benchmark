import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # total literals
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def var_node(idx, val):
        """return node number for s[idx]=val (val 0/1)"""
        return 2 * (idx - 1) + val

    for _ in range(m):
        c1 = int(next(it)); c2 = int(next(it))
        u1 = abs(c1); u2 = abs(c2)
        b1 = 1 if c1 > 0 else 0
        b2 = 1 if c2 > 0 else 0
        a = var_node(u1, b1)          # literal A
        b = var_node(u2, b2)          # literal B
        na = a ^ 1                     # ¬A
        nb = b ^ 1                     # ¬B
        # ¬A -> B
        g[na].append(b); rg[b].append(na)
        # ¬B -> A
        g[nb].append(a); rg[a].append(nb)

    visited = [False] * N
    order = []

    def dfs(v):
        visited[v] = True
        for to in g[v]:
            if not visited[to]:
                dfs(to)
        order.append(v)

    for v in range(N):
        if not visited[v]:
            dfs(v)

    comp = [-1] * N
    cur = 0

    def rdfs(v, k):
        comp[v] = k
        for to in rg[v]:
            if comp[to] == -1:
                rdfs(to, k)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cur)
            cur += 1

    # check satisfiability
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return

    # assignment: component with larger number = false
    ans = [0] * n
    for i in range(n):
        ans[i] = 1 if comp[2*i+1] > comp[2*i] else 0

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()