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

    def lit_to_node(l: int) -> int:
        if l > 0:
            return 2 * (l - 1)       # true
        else:
            return 2 * (-l - 1) + 1  # false

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        u = lit_to_node(a)
        v = lit_to_node(b)
        nu = u ^ 1
        nv = v ^ 1
        # ¬a → b
        g[nu].append(v)
        rg[v].append(nu)
        # ¬b → a
        g[nv].append(u)
        rg[u].append(nv)

    sys.setrecursionlimit(1 << 25)

    visited = [False] * N
    order = []

    # first pass: iterative DFS to get order
    for i in range(N):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                v, idx = stack.pop()
                if idx == 0:
                    if visited[v]:
                        continue
                    visited[v] = True
                    stack.append((v, 1))  # post‑process marker
                    for to in g[v]:
                        if not visited[to]:
                            stack.append((to, 0))
                else:
                    order.append(v)

    comp = [-1] * N
    cid = 0
    # second pass on reversed graph
    for v in reversed(order):
        if comp[v] == -1:
            stack = [v]
            comp[v] = cid
            while stack:
                x = stack.pop()
                for to in rg[x]:
                    if comp[to] == -1:
                        comp[to] = cid
                        stack.append(to)
            cid += 1

    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        # component with larger id comes earlier in topological order
        assignment[i] = 1 if comp[2 * i] > comp[2 * i + 1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()