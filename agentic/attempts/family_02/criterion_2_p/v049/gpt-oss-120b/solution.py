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

    def var_idx(v: int) -> int:
        """return node index for literal v (positive = true, negative = false)"""
        v_abs = abs(v) - 1
        if v > 0:
            return v_abs * 2      # true
        else:
            return v_abs * 2 + 1  # false

    def neg(x: int) -> int:
        return x ^ 1

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        a_idx = var_idx(a)
        b_idx = var_idx(b)
        na = neg(a_idx)
        nb = neg(b_idx)
        # (!a -> b)
        g[na].append(b_idx)
        rg[b_idx].append(na)
        # (!b -> a)
        g[nb].append(a_idx)
        rg[a_idx].append(nb)

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
    cid = 0

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
            rdfs(v, cid)
            cid += 1

    assignment = [0] * n
    for i in range(n):
        if comp[2*i] == comp[2*i + 1]:
            print("NO")
            return
        assignment[i] = 1 if comp[2*i] > comp[2*i + 1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()