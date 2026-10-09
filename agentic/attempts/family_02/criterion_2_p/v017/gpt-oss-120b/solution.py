import sys

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
        """return node index for literal x (positive => true, negative => false)"""
        v = abs(x) - 1
        return 2 * v + (1 if x > 0 else 0)

    def neg(node: int) -> int:
        return node ^ 1

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        A = lit(a)
        B = lit(b)
        # (!A -> B)
        g[neg(A)].append(B)
        rg[B].append(neg(A))
        # (!B -> A)
        g[neg(B)].append(A)
        rg[A].append(neg(B))

    sys.setrecursionlimit(1 << 25)

    # Kosaraju first pass
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

    # second pass
    comp = [-1] * N
    cid = 0
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

    # check satisfiability
    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        assignment[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()