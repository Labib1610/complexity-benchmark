import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # number of vertices
    g = [[] for _ in range(N)]    # forward graph
    rg = [[] for _ in range(N)]   # reverse graph

    def lit_index(x: int) -> int:
        """return vertex index for literal x (positive -> true, negative -> false)"""
        v = abs(x) - 1
        if x > 0:
            return 2 * v          # true
        else:
            return 2 * v + 1      # false

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        ia = lit_index(a)
        ib = lit_index(b)
        na = ia ^ 1                # negation
        nb = ib ^ 1
        # ¬a -> b
        g[na].append(ib)
        rg[ib].append(na)
        # ¬b -> a
        g[nb].append(ia)
        rg[ia].append(nb)

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

    def rdfs(v: int, label: int):
        stack = [v]
        while stack:
            node = stack.pop()
            if comp[node] != -1:
                continue
            comp[node] = label
            for to in rg[node]:
                if comp[to] == -1:
                    stack.append(to)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cur)
            cur += 1

    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        # true component appears later (higher number) -> assign true
        assignment[i] = 1 if comp[2 * i] > comp[2 * i + 1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()