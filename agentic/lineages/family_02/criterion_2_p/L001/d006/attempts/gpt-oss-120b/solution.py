import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # number of literals
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def lit(v: int) -> int:
        """return index of literal representing (s_|v| == target(v))"""
        var = abs(v) - 1
        if v > 0:
            return 2 * var          # true literal
        else:
            return 2 * var + 1      # false literal

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        la = lit(a)
        lb = lit(b)
        na = la ^ 1
        nb = lb ^ 1
        # ¬a -> b
        g[na].append(lb)
        rg[lb].append(na)
        # ¬b -> a
        g[nb].append(la)
        rg[la].append(nb)

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
            x = stack.pop()
            if comp[x] != -1:
                continue
            comp[x] = label
            for to in rg[x]:
                if comp[to] == -1:
                    stack.append(to)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cur)
            cur += 1

    assignment = [0] * n
    for i in range(n):
        t = 2 * i
        f = t ^ 1
        if comp[t] == comp[f]:
            print("NO")
            return
        assignment[i] = 1 if comp[t] > comp[f] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()