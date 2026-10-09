import sys
sys.setrecursionlimit(1 << 25)

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

    def lit_index(x: int) -> int:
        """return vertex index for literal x (positive -> xi, negative -> ¬xi)"""
        v = abs(x) - 1
        if x > 0:
            return 2 * v          # xi
        else:
            return 2 * v + 1      # ¬xi

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        ia = lit_index(a)
        ib = lit_index(b)
        na = ia ^ 1   # negation vertex
        nb = ib ^ 1
        # ¬a -> b
        g[na].append(ib)
        rg[ib].append(na)
        # ¬b -> a
        g[nb].append(ia)
        rg[ia].append(nb)

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
            u = stack.pop()
            if comp[u] != -1:
                continue
            comp[u] = label
            for to in rg[u]:
                if comp[to] == -1:
                    stack.append(to)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cur)
            cur += 1

    # check satisfiability
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            sys.stdout.write("NO")
            return

    # build assignment
    ans = [0] * n
    for i in range(n):
        ans[i] = 1 if comp[2*i] > comp[2*i+1] else 0

    out = ["YES", " ".join(map(str, ans))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()