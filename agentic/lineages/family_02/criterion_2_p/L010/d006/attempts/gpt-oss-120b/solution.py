import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        rg[v].append(u)

    def var(i):          # literal xi (true)
        return i
    def neg(i):          # literal ¬xi
        return i + n

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        a = abs(l1) - 1
        b = abs(l2) - 1
        s1 = 1 if l1 > 0 else -1
        s2 = 1 if l2 > 0 else -1

        if a == b:
            # same variable
            if s1 == s2:
                if s1 == 1:
                    # xa = 1
                    add_imp(neg(var(a)), var(a))
                else:
                    # xa = 0
                    add_imp(var(a), neg(var(a)))
            # opposite signs give no restriction
            continue

        # different variables
        if s1 == 1 and s2 == 1:
            # xa ∨ xb
            add_imp(neg(var(a)), var(b))
            add_imp(neg(var(b)), var(a))
        elif s1 == -1 and s2 == -1:
            # ¬xa ∨ ¬xb
            add_imp(var(a), neg(var(b)))
            add_imp(var(b), neg(var(a)))
        elif s1 == 1 and s2 == -1:
            # xb -> xa
            add_imp(var(b), var(a))
            add_imp(neg(var(a)), neg(var(b)))
        elif s1 == -1 and s2 == 1:
            # xa -> xb
            add_imp(var(a), var(b))
            add_imp(neg(var(b)), neg(var(a)))

    # Kosaraju
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
    cid = 0

    def rdfs(v, k):
        comp[v] = k
        for to in rg[v]:
            if comp[to] == -1:
                rdfs(to, k)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cid)
            cid += 1

    assignment = [0] * n
    for i in range(n):
        if comp[var(i)] == comp[neg(var(i))]:
            print("NO")
            return
        assignment[i] = 1 if comp[var(i)] > comp[neg(var(i))] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()