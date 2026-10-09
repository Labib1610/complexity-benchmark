import sys
sys.setrecursionlimit(1 << 25)

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
        if x > 0:          # literal is x = True
            return v * 2
        else:              # literal is ¬x = True  (i.e., x is False)
            return v * 2 + 1

    def neg(idx: int) -> int:
        return idx ^ 1

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        a_idx = var_index(a)
        b_idx = var_index(b)
        na = neg(a_idx)
        nb = neg(b_idx)
        # (!a -> b)
        g[na].append(b_idx)
        rg[b_idx].append(na)
        # (!b -> a)
        g[nb].append(a_idx)
        rg[a_idx].append(nb)

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
    cur = 0

    def rdfs(v: int, label: int):
        comp[v] = label
        for to in rg[v]:
            if comp[to] == -1:
                rdfs(to, label)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cur)
            cur += 1

    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        assignment[i] = 1 if comp[2 * i] > comp[2 * i + 1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()