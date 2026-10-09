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

    def var_id(x: int) -> int:
        """return vertex id for literal x (positive -> true, negative -> false)"""
        v = abs(x) - 1
        if x > 0:
            return 2 * v          # xi
        else:
            return 2 * v + 1      # ¬xi

    def add_imp(u: int, v: int) -> None:
        g[u].append(v)
        rg[v].append(u)

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        A = var_id(a)
        B = var_id(b)
        NA = A ^ 1
        NB = B ^ 1
        # ¬A -> B
        add_imp(NA, B)
        # ¬B -> A
        add_imp(NB, A)

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
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
        assignment[i] = 1 if comp[2*i] > comp[2*i+1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()