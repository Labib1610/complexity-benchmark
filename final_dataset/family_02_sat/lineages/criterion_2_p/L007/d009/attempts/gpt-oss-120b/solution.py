import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # number of nodes in implication graph
    G = [[] for _ in range(N)]
    GR = [[] for _ in range(N)]

    def node(idx: int, val: int) -> int:
        """return node number for literal (x_idx == val)"""
        return 2 * idx + val      # val = 0 -> false node, 1 -> true node

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        i = abs(l1) - 1
        j = abs(l2) - 1
        t1 = 1 if l1 > 0 else 0
        t2 = 1 if l2 > 0 else 0

        a = node(i, t1)
        b = node(j, t2)

        na = a ^ 1          # negation of a
        nb = b ^ 1          # negation of b

        # ¬a → b
        G[na].append(b)
        GR[b].append(na)
        # ¬b → a
        G[nb].append(a)
        GR[a].append(nb)

    # ---------- Kosaraju ----------
    visited = [False] * N
    order = []

    sys.setrecursionlimit(1 << 25)

    def dfs(v: int):
        visited[v] = True
        for to in G[v]:
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
        for to in GR[v]:
            if comp[to] == -1:
                rdfs(to, label)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cur)
            cur += 1

    # ---------- check satisfiability ----------
    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        # later component (larger number) means true
        assignment[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()