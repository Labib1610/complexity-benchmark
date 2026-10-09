import sys

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # total vertices
    g = [[] for _ in range(N)]   # forward graph
    rg = [[] for _ in range(N)]  # reverse graph

    def var_node(i: int, is_true: bool) -> int:
        """return vertex number for Li (is_true) or ¬Li (not is_true)"""
        base = 2 * (i - 1)
        return base + (1 if is_true else 0)

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))

        # translate input literal to (var, is_true) where literal = (is_true ? Li : ¬Li)
        if l1 > 0:
            a_var, a_true = l1, False   # ¬Li
        else:
            a_var, a_true = -l1, True   # Li

        if l2 > 0:
            b_var, b_true = l2, False
        else:
            b_var, b_true = -l2, True

        a = var_node(a_var, a_true)
        nota = var_node(a_var, not a_true)
        b = var_node(b_var, b_true)
        notb = var_node(b_var, not b_true)

        # add implications ¬A → B , ¬B → A
        g[nota].append(b)
        rg[b].append(nota)

        g[notb].append(a)
        rg[a].append(notb)

    # Kosaraju
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

    # check satisfiability
    assignment = [0] * n
    for i in range(1, n + 1):
        false_node = var_node(i, False)
        true_node = var_node(i, True)
        if comp[false_node] == comp[true_node]:
            print("NO")
            return
        # component with larger number appears earlier in topological order of reversed graph
        assignment[i - 1] = 1 if comp[true_node] > comp[false_node] else 0

    print("YES")
    print(' '.join(map(str, assignment)))


if __name__ == "__main__":
    solve()