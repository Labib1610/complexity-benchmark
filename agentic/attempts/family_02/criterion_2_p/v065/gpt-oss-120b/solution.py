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

    def lit_node(l: int) -> int:
        """return node index for literal l (positive -> true, negative -> false)"""
        if l > 0:
            return 2 * (l - 1) + 1   # true
        else:
            return 2 * (-l - 1)       # false

    def neg(node: int) -> int:
        return node ^ 1

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        na = lit_node(a)
        nb = lit_node(b)
        # (!a -> b)
        g[neg(na)].append(nb)
        rg[nb].append(neg(na))
        # (!b -> a)
        g[neg(nb)].append(na)
        rg[na].append(neg(nb))

    visited = [False] * N
    order = []

    def dfs(v: int):
        stack = [(v, 0)]
        while stack:
            v, idx = stack.pop()
            if idx == 0:
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
            u = stack.pop()
            if comp[u] != -1:
                continue
            comp[u] = label
            for to in rg[u]:
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
        # component with larger id comes earlier in topological order
        assignment[i] = 1 if comp[2*i+1] > comp[2*i] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()