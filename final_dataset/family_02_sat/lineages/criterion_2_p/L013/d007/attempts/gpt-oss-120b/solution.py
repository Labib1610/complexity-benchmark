import sys

sys.setrecursionlimit(1 << 25)

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

    def var_idx(i: int, is_true: bool) -> int:
        # i: 0‑based variable index
        return 2 * i + (0 if is_true else 1)

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))

        i1 = abs(l1) - 1
        d1 = 1 if l1 < 0 else 0          # delta
        # literal A is (y_i == 1) if d1==1 else (y_i == 0)
        # i.e., A is true when y_i == d1
        # So A corresponds to y_i if d1==1 else ¬y_i
        A_true = (d1 == 1)               # whether A is y_i (True) or ¬y_i (False)
        A = var_idx(i1, A_true)

        i2 = abs(l2) - 1
        d2 = 1 if l2 < 0 else 0
        B_true = (d2 == 1)
        B = var_idx(i2, B_true)

        # clause: (¬A) OR (¬B)
        # add implications: A -> ¬B, B -> ¬A
        notA = var_idx(i1, not A_true)
        notB = var_idx(i2, not B_true)

        g[A].append(notB)
        rg[notB].append(A)

        g[B].append(notA)
        rg[notA].append(B)

    # Kosaraju
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
    cur = 0

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
            rdfs(v, cur)
            cur += 1

    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        # variable is true if its SCC comes later (higher topological order)
        assignment[i] = 1 if comp[2 * i] > comp[2 * i + 1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()