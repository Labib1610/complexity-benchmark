import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # literal count
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def lit(var: int, val: bool) -> int:
        """return literal id for (x_var == val) where val is True/False"""
        return 2 * var + (0 if val else 1)

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        a = abs(l1) - 1
        b = abs(l2) - 1
        neg1 = l1 < 0          # neg(v) as defined
        neg2 = l2 < 0

        # clause: (x_a != neg1) OR (x_b != neg2)
        # which is (x_a == not neg1) OR (x_b == not neg2)
        valA = not neg1
        valB = not neg2
        A = lit(a, valA)
        B = lit(b, valB)

        # add implications ¬A → B , ¬B → A
        NA = A ^ 1
        NB = B ^ 1
        g[NA].append(B)
        g[NB].append(A)
        rg[B].append(NA)
        rg[A].append(NB)

    # Kosaraju
    visited = [False] * N
    order = []

    def dfs(v: int):
        stack = [v]
        while stack:
            node = stack[-1]
            if visited[node]:
                stack.pop()
                continue
            visited[node] = True
            for to in g[node]:
                if not visited[to]:
                    stack.append(to)
            # after exploring children, will be added to order later
            # we simulate recursion by second pass
            # use separate marker
            if stack and stack[-1] == node:
                stack.pop()
                order.append(node)

    for v in range(N):
        if not visited[v]:
            dfs(v)

    comp = [-1] * N
    cur = 0
    for v in reversed(order):
        if comp[v] != -1:
            continue
        stack = [v]
        while stack:
            node = stack.pop()
            if comp[node] != -1:
                continue
            comp[node] = cur
            for to in rg[node]:
                if comp[to] == -1:
                    stack.append(to)
        cur += 1

    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        # component number larger => earlier in topological order
        assignment[i] = 1 if comp[2 * i] > comp[2 * i + 1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()