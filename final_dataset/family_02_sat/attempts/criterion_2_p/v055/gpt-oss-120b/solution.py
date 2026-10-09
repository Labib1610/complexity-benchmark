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

    def lit_node(x: int) -> int:
        """return node index for literal x (positive means var true, negative means var false)"""
        if x > 0:
            return 2 * (x - 1)          # var true
        else:
            return 2 * (abs(x) - 1) + 1  # var false

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        na = lit_node(a)
        nb = lit_node(b)
        na_neg = na ^ 1
        nb_neg = nb ^ 1
        # clause: ¬a ∨ ¬b  => a -> ¬b , b -> ¬a
        g[na].append(nb_neg)
        g[nb].append(na_neg)
        rg[nb_neg].append(na)
        rg[na_neg].append(nb)

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

    assignment = [0] * n
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
        # component with larger number comes earlier in topological order
        assignment[i] = 1 if comp[2*i] > comp[2*i+1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()