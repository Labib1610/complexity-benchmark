import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    N = n * 2
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def var_index(x: int) -> int:
        v = abs(x) - 1
        if x > 0:
            return v * 2      # true literal
        else:
            return v * 2 + 1  # false literal

    def neg(idx: int) -> int:
        return idx ^ 1

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        ia = var_index(a)
        ib = var_index(b)
        # (a OR b) => (~a -> b) and (~b -> a)
        na = neg(ia)
        nb = neg(ib)
        g[na].append(ib)
        g[nb].append(ia)
        rg[ib].append(na)
        rg[ia].append(nb)

    sys.setrecursionlimit(1 << 25)
    visited = [False] * N
    order = []

    def dfs(v: int):
        visited[v] = True
        for to in g[v]:
            if not visited[to]:
                dfs(to)
        order.append(v)

    for v in range(N):
        if not visited[v]:
            dfs(v)

    comp = [-1] * N
    label = 0

    def rdfs(v: int, k: int):
        comp[v] = k
        for to in rg[v]:
            if comp[to] == -1:
                rdfs(to, k)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, label)
            label += 1

    assignment = [0] * n
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
        assignment[i] = 1 if comp[2*i] > comp[2*i+1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()