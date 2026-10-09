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

    def idx(lit: int) -> int:
        if lit > 0:
            return 2 * (lit - 1)          # xi
        else:
            return 2 * (-lit - 1) + 1     # ¬xi

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        A = idx(a)
        B = idx(b)
        NA = A ^ 1
        NB = B ^ 1
        # ¬a -> b
        g[NA].append(B)
        rg[B].append(NA)
        # ¬b -> a
        g[NB].append(A)
        rg[A].append(NB)

    # ---------- first pass ----------
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

    # ---------- second pass ----------
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

    # ---------- check satisfiability ----------
    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        # true component has larger number (appears earlier in second pass)
        assignment[i] = 1 if comp[2 * i] > comp[2 * i + 1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()