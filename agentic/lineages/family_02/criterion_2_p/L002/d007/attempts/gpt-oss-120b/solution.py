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

    def lit(var: int, val: int) -> int:
        """return node index for x_var = val (val 0 or 1)"""
        return 2 * var + val

    for _ in range(m):
        c1 = int(next(it))
        c2 = int(next(it))
        u = abs(c1) - 1
        v = abs(c2) - 1
        # L1 is true when torque negative for c1
        # torque negative when (c>0 and s=0) or (c<0 and s=1)
        val1 = 0 if c1 > 0 else 1
        val2 = 0 if c2 > 0 else 1
        L1 = lit(u, val1)
        L2 = lit(v, val2)
        notL1 = lit(u, 1 - val1)
        notL2 = lit(v, 1 - val2)
        # (L1) -> (not L2)
        g[L1].append(notL2)
        rg[notL2].append(L1)
        # (L2) -> (not L1)
        g[L2].append(notL1)
        rg[notL1].append(L2)

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
        # component with higher order (larger label) is earlier in topological order
        assignment[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()