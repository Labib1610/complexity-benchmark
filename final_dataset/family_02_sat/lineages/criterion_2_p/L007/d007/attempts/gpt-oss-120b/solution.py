import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = n * 2                     # each variable: false node = 2*i, true node = 2*i+1
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        rg[v].append(u)

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        # literal for l1
        idx1 = abs(l1) - 1
        if l1 > 0:
            lit1 = idx1 * 2 + 1          # z_i (true)
        else:
            lit1 = idx1 * 2              # ¬z_i (false)
        # literal for l2
        idx2 = abs(l2) - 1
        if l2 > 0:
            lit2 = idx2 * 2 + 1
        else:
            lit2 = idx2 * 2

        # clause (lit1 ∨ lit2)  =>  (¬lit1 → lit2) , (¬lit2 → lit1)
        not_lit1 = lit1 ^ 1
        not_lit2 = lit2 ^ 1
        add_imp(not_lit1, lit2)
        add_imp(not_lit2, lit1)

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

    assignment = [0] * n
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
        # true component has larger number (comes earlier in topological order)
        assignment[i] = 1 if comp[2*i] < comp[2*i+1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()