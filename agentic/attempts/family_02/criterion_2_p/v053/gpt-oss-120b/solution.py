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

    def lit(x: int) -> int:
        if x > 0:
            v = x - 1
            return v * 2          # true (upgraded)
        else:
            v = -x - 1
            return v * 2 + 1      # false (legacy)

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
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
        assignment[i] = 1 if comp[2*i] > comp[2*i+1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()