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

    def lit_index(l: int) -> int:
        """return vertex index for literal l (positive -> xi, negative -> ¬xi)"""
        if l > 0:
            v = l - 1
            return 2 * v + 1          # xi
        else:
            v = -l - 1
            return 2 * v              # ¬xi

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        A = lit_index(a)
        B = lit_index(b)
        NA = A ^ 1          # opposite literal (toggle last bit)
        NB = B ^ 1
        # ¬a -> b
        g[NA].append(B)
        rg[B].append(NA)
        # ¬b -> a
        g[NB].append(A)
        rg[A].append(NB)

    sys.setrecursionlimit(1 << 25)

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

    # ---------- check satisfiability ----------
    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        assignment[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    # ---------- output ----------
    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()