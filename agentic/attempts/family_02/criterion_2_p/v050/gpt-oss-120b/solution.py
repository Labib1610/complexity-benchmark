import sys

sys.setrecursionlimit(1_000_000)

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    N = 2 * n                     # total vertices
    g = [[] for _ in range(N)]    # forward graph
    rg = [[] for _ in range(N)]   # reversed graph

    def lit_idx(l: int) -> int:
        v = abs(l) - 1
        if l > 0:
            return v * 2          # true
        else:
            return v * 2 + 1      # false

    for _ in range(m):
        a = next(it)
        b = next(it)
        a_idx = lit_idx(a)
        b_idx = lit_idx(b)
        na = a_idx ^ 1
        nb = b_idx ^ 1
        # ¬a → b
        g[na].append(b_idx)
        rg[b_idx].append(na)
        # ¬b → a
        g[nb].append(a_idx)
        rg[a_idx].append(nb)

    visited = [False] * N
    order = []

    def dfs1(v: int):
        visited[v] = True
        for to in g[v]:
            if not visited[to]:
                dfs1(to)
        order.append(v)

    for v in range(N):
        if not visited[v]:
            dfs1(v)

    comp = [-1] * N
    label = 0

    def dfs2(v: int, lbl: int):
        stack = [v]
        comp[v] = lbl
        while stack:
            cur = stack.pop()
            for to in rg[cur]:
                if comp[to] == -1:
                    comp[to] = lbl
                    stack.append(to)

    for v in reversed(order):
        if comp[v] == -1:
            dfs2(v, label)
            label += 1

    # check for contradictions
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return

    # build assignment
    ans = [0] * n
    for i in range(n):
        ans[i] = 1 if comp[2 * i] > comp[2 * i + 1] else 0

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()