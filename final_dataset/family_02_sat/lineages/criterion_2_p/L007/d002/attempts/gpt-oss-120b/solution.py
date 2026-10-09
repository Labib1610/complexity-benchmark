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

    def var_true(i):   # node for xi = True
        return 2 * i

    def var_false(i):  # node for xi = False
        return 2 * i + 1

    def lit_node(v):
        """return node representing the strain literal for integer v"""
        idx = abs(v) - 1
        if v > 0:
            # strain is ¬x_i
            return var_false(idx)
        else:
            # strain is x_i
            return var_true(idx)

    def neg(node):
        return node ^ 1  # toggle true/false

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        lit1 = lit_node(l1)
        lit2 = lit_node(l2)
        # clause (¬lit1 ∨ ¬lit2)
        # implications: lit1 -> ¬lit2, lit2 -> ¬lit1
        a = lit1
        b = lit2
        na = neg(a)
        nb = neg(b)
        # a -> nb
        g[a].append(nb)
        rg[nb].append(a)
        # b -> na
        g[b].append(na)
        rg[na].append(b)

    visited = [False] * N
    order = []

    def dfs(v):
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
    def rdfs(v, cid):
        stack = [v]
        while stack:
            x = stack.pop()
            if comp[x] != -1:
                continue
            comp[x] = cid
            for to in rg[x]:
                if comp[to] == -1:
                    stack.append(to)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cid)
            cid += 1

    assignment = [0] * n
    for i in range(n):
        if comp[var_true(i)] == comp[var_false(i)]:
            print("NO")
            return
        assignment[i] = 1 if comp[var_true(i)] > comp[var_false(i)] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()