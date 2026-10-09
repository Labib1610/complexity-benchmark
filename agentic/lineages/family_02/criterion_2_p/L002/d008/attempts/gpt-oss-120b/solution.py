import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # node id: i*2 + value (0 or 1)
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        rg[v].append(u)

    for _ in range(m):
        c1 = int(next(it))
        c2 = int(next(it))
        i1 = abs(c1) - 1
        i2 = abs(c2) - 1
        v1 = 0 if c1 > 0 else 1   # rigid when xi == v1
        v2 = 0 if c2 > 0 else 1

        # clause: (xi != v1) OR (xj != v2)
        # literals a = (xi = 1-v1), b = (xj = 1-v2)
        a = i1 * 2 + (1 - v1)
        nota = i1 * 2 + v1
        b = i2 * 2 + (1 - v2)
        notb = i2 * 2 + v2

        add_imp(nota, b)   # (xi = v1) -> (xj = 1-v2)
        add_imp(notb, a)   # (xj = v2) -> (xi = 1-v1)

    sys.setrecursionlimit(1 << 25)

    # Kosaraju first pass: order
    visited = [False] * N
    order = []

    for v in range(N):
        if not visited[v]:
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
        if comp[i*2] == comp[i*2+1]:
            print("NO")
            return
        # higher component number means earlier in topological order
        assignment[i] = 1 if comp[i*2+1] > comp[i*2] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()