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

    def lit_to_idx(x: int) -> int:
        v = abs(x) - 1
        # true literal -> even index, false literal -> odd index
        return (v << 1) ^ (0 if x > 0 else 1)

    def neg(idx: int) -> int:
        return idx ^ 1

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        ia = lit_to_idx(a)
        ib = lit_to_idx(b)
        na = neg(ia)
        nb = neg(ib)
        # (!a -> b)
        g[na].append(ib)
        rg[ib].append(na)
        # (!b -> a)
        g[nb].append(ia)
        rg[ia].append(nb)

    sys.setrecursionlimit(1 << 25)
    visited = [False] * N
    order = []

    def dfs(v: int):
        stack = [(v, 0)]
        while stack:
            v, state = stack.pop()
            if state == 0:
                if visited[v]:
                    continue
                visited[v] = True
                stack.append((v, 1))
                for to in g[v]:
                    if not visited[to]:
                        stack.append((to, 0))
            else:
                order.append(v)

    for v in range(N):
        if not visited[v]:
            dfs(v)

    comp = [-1] * N
    cur = 0

    def rdfs(v: int, label: int):
        stack = [v]
        while stack:
            v = stack.pop()
            if comp[v] != -1:
                continue
            comp[v] = label
            for to in rg[v]:
                if comp[to] == -1:
                    stack.append(to)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cur)
            cur += 1

    assignment = [0] * n
    for i in range(n):
        if comp[i << 1] == comp[(i << 1) ^ 1]:
            print("NO")
            return
        assignment[i] = 1 if comp[i << 1] > comp[(i << 1) ^ 1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()