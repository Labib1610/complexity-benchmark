import sys

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # 0..2n-1, even = false, odd = true
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def lit(l):
        """return node id of literal that is true when displacement = +1"""
        idx = abs(l) - 1
        if l > 0:                 # need s_i = 1  -> true literal
            return 2 * idx + 1
        else:                     # need s_i = 0  -> false literal
            return 2 * idx

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        a = lit(l1)
        b = lit(l2)
        na = a ^ 1          # negation
        nb = b ^ 1
        # (a ∨ b)  => (¬a → b) , (¬b → a)
        g[na].append(b)
        rg[b].append(na)
        g[nb].append(a)
        rg[a].append(nb)

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
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        # component with larger number appears earlier in topological order
        assignment[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()