import sys

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

    def idx(lit: int) -> int:
        v = abs(lit) - 1
        return 2 * v + (0 if lit > 0 else 1)

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        na = idx(-a)
        nb = idx(-b)
        ia = idx(a)
        ib = idx(b)
        g[na].append(ib)
        g[nb].append(ia)
        rg[ib].append(na)
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
    for v in reversed(order):
        if comp[v] == -1:
            stack = [v]
            comp[v] = cur
            while stack:
                u = stack.pop()
                for to in rg[u]:
                    if comp[to] == -1:
                        comp[to] = cur
                        stack.append(to)
            cur += 1

    ans = None
    for i in range(1, n + 1):
        if comp[2 * (i - 1)] == comp[2 * (i - 1) + 1]:
            ans = i
            break
    print(ans if ans is not None else 1)


if __name__ == "__main__":
    solve()