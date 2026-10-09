import sys

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

    def lit_idx(x: int) -> int:
        """return vertex index for literal x (positive -> true, negative -> false)"""
        if x > 0:
            v = x - 1
            return 2 * v + 1          # true
        else:
            v = -x - 1
            return 2 * v              # false

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        ia = lit_idx(a)
        ib = lit_idx(b)
        na = ia ^ 1          # negation
        nb = ib ^ 1
        # ¬a -> b
        g[na].append(ib)
        rg[ib].append(na)
        # ¬b -> a
        g[nb].append(ia)
        rg[ia].append(nb)

    sys.setrecursionlimit(1 << 25)

    # first pass: order
    visited = [False] * N
    order = []

    for v in range(N):
        if not visited[v]:
            stack = [(v, 0)]  # (node, next_child_index), 0 means entry
            while stack:
                node, state = stack.pop()
                if state == 0:
                    if visited[node]:
                        continue
                    visited[node] = True
                    stack.append((node, 1))  # exit later
                    for to in g[node]:
                        if not visited[to]:
                            stack.append((to, 0))
                else:
                    order.append(node)

    # second pass: assign components
    comp = [-1] * N
    cur = 0
    for v in reversed(order):
        if comp[v] == -1:
            stack = [v]
            comp[v] = cur
            while stack:
                node = stack.pop()
                for to in rg[node]:
                    if comp[to] == -1:
                        comp[to] = cur
                        stack.append(to)
            cur += 1

    # check satisfiability
    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        # true if component of true literal > component of false literal
        assignment[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()