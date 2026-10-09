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

    def lit(x: int) -> int:
        if x > 0:
            return 2 * (x - 1)          # true
        else:
            return 2 * (-x - 1) + 1     # false

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        la = lit(a)
        lb = lit(b)
        na = la ^ 1
        nb = lb ^ 1
        g[na].append(lb)
        g[nb].append(la)
        rg[lb].append(na)
        rg[la].append(nb)

    visited = [False] * N
    order = []

    # first pass: order by finish time
    stack = []
    for v in range(N):
        if not visited[v]:
            stack.append((v, 0))
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

    comp = [-1] * N
    cid = 0
    # second pass: assign components on reversed graph
    for v in reversed(order):
        if comp[v] == -1:
            stack = [v]
            comp[v] = cid
            while stack:
                node = stack.pop()
                for to in rg[node]:
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