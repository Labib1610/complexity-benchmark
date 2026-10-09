import sys

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    N = n * 2
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def lit_to_idx(x: int) -> int:
        v = abs(x) - 1
        if x > 0:
            return v * 2 + 1   # true
        else:
            return v * 2       # false

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        ia = lit_to_idx(a)
        ib = lit_to_idx(b)
        na = ia ^ 1  # negation
        nb = ib ^ 1
        # (!a -> b)
        g[na].append(ib)
        rg[ib].append(na)
        # (!b -> a)
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
    cid = 0

    def rdfs(v: int, label: int):
        stack = [v]
        while stack:
            v = stack.pop()
            if comp[v] != -1:
                continue
            comp[v] = label
            for to in rg[v]:
                if comp[to] == -1:
                    stack.append(to)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cid)
            cid += 1

    assignment = [0] * n
    for i in range(n):
        f = i * 2
        t = f + 1
        if comp[f] == comp[t]:
            print("NO")
            return
        assignment[i] = 1 if comp[t] > comp[f] else 0

    out = ["YES", " ".join(map(str, assignment))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()