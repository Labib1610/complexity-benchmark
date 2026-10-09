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

    def var_idx(x: int) -> int:
        # x in 1..n for true, -x for false
        v = abs(x) - 1
        if x > 0:
            return v * 2      # true literal
        else:
            return v * 2 + 1  # false literal

    def neg(u: int) -> int:
        return u ^ 1

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        u = var_idx(a)
        v = var_idx(b)
        # (u OR v) => (~u -> v) and (~v -> u)
        gu = neg(u)
        gv = neg(v)
        g[gu].append(v)
        g[gv].append(u)
        rg[v].append(gu)
        rg[u].append(gv)

    sys.setrecursionlimit(1 << 25)
    visited = [False] * N
    order = []

    def dfs(v: int):
        stack = [(v, 0)]
        while stack:
            node, state = stack.pop()
            if state == 0:
                if visited[node]:
                    continue
                visited[node] = True
                stack.append((node, 1))
                for to in g[node]:
                    if not visited[to]:
                        stack.append((to, 0))
            else:
                order.append(node)

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
                node = stack.pop()
                for to in rg[node]:
                    if comp[to] == -1:
                        comp[to] = cur
                        stack.append(to)
            cur += 1

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