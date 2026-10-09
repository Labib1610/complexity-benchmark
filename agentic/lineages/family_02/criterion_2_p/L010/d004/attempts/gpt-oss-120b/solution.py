import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    N = 2 * n                     # total vertices
    g = [[] for _ in range(N)]    # forward graph
    rg = [[] for _ in range(N)]   # reversed graph

    def lit_index(var, is_true):
        """return vertex index for literal (x_var) if is_true else (¬x_var)"""
        return 2 * var + (1 if is_true else 0)

    for _ in range(m):
        l1 = next(it)
        l2 = next(it)
        a = abs(l1) - 1
        b = abs(l2) - 1
        # literal A
        if l1 > 0:
            A = lit_index(a, True)      # x_a
        else:
            A = lit_index(a, False)     # ¬x_a
        # literal B
        if l2 > 0:
            B = lit_index(b, True)
        else:
            B = lit_index(b, False)

        notA = A ^ 1
        notB = B ^ 1
        # ¬A → B
        g[notA].append(B)
        rg[B].append(notA)
        # ¬B → A
        g[notB].append(A)
        rg[A].append(notB)

    sys.setrecursionlimit(1 << 25)

    visited = [False] * N
    order = []

    # first pass: fill order by finish time
    def dfs(v):
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

    # second pass: assign components on reversed graph
    def rdfs(v, label):
        stack = [v]
        comp[v] = label
        while stack:
            node = stack.pop()
            for to in rg[node]:
                if comp[to] == -1:
                    comp[to] = label
                    stack.append(to)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cur)
            cur += 1

    # check for contradictions
    for i in range(n):
        if comp[2*i] == comp[2*i + 1]:
            print("NO")
            return

    # build assignment
    assignment = [0] * n
    for i in range(n):
        # true component must be "earlier" (higher number) in topological order
        assignment[i] = 1 if comp[2*i + 1] > comp[2*i] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()