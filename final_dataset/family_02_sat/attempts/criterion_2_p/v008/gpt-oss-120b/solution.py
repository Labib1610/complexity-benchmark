import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    N = 2 * n
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def lit_idx(l: int) -> int:
        if l > 0:
            return 2 * (l - 1)      # true
        else:
            return 2 * (-l - 1) + 1  # false

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        ia = lit_idx(a)
        ib = lit_idx(b)
        na = ia ^ 1
        nb = ib ^ 1
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
    cid = 0
    for v in reversed(order):
        if comp[v] != -1:
            continue
        stack = [v]
        comp[v] = cid
        while stack:
            u = stack.pop()
            for to in rg[u]:
                if comp[to] == -1:
                    comp[to] = cid
                    stack.append(to)
        cid += 1

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