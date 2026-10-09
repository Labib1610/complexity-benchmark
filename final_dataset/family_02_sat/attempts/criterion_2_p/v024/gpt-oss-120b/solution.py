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

    def lit_to_node(l: int) -> int:
        v = abs(l) - 1
        if l > 0:
            return 2 * v + 1          # true
        else:
            return 2 * v              # false

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        u = lit_to_node(a)
        v = lit_to_node(b)
        nu = u ^ 1
        nv = v ^ 1
        # ¬a -> b
        g[nu].append(v)
        rg[v].append(nu)
        # ¬b -> a
        g[nv].append(u)
        rg[u].append(nv)

    visited = [False] * N
    order = []

    sys.setrecursionlimit(1 << 25)

    def dfs(v: int):
        stack = [(v, 0)]
        while stack:
            node, idx = stack.pop()
            if idx == 0:
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

    # check satisfiability
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return

    # build assignment
    ans = [0] * n
    for i in range(n):
        ans[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()