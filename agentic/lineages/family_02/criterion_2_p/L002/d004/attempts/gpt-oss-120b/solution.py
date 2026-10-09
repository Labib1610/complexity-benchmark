import sys
sys.setrecursionlimit(1 << 25)

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

    def lit(c: int) -> int:
        """return vertex index of the literal that is high for feed c"""
        if c > 0:
            return 2 * (c - 1)          # xi = False
        else:
            return 2 * (-c - 1) + 1    # xi = True

    for _ in range(m):
        c1 = int(next(it)); c2 = int(next(it))
        a = lit(c1)
        b = lit(c2)
        na = a ^ 1
        nb = b ^ 1
        # a -> not b
        g[a].append(nb)
        rg[nb].append(a)
        # b -> not a
        g[b].append(na)
        rg[na].append(b)

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
    label = 0
    for v in reversed(order):
        if comp[v] == -1:
            stack = [v]
            comp[v] = label
            while stack:
                cur = stack.pop()
                for to in rg[cur]:
                    if comp[to] == -1:
                        comp[to] = label
                        stack.append(to)
            label += 1

    assignment = [0] * n
    for i in range(n):
        f = 2 * i
        t = f + 1
        if comp[f] == comp[t]:
            print("NO")
            return
        # higher component number = earlier in topological order
        assignment[i] = 1 if comp[t] > comp[f] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()