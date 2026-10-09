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

    def lit_to_node(l):
        v = abs(l) - 1
        if l > 0:
            return 2 * v + 1   # xi
        else:
            return 2 * v       # ¬xi

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        na = lit_to_node(a)
        nb = lit_to_node(b)
        na_neg = na ^ 1
        nb_neg = nb ^ 1
        # ¬a -> b
        g[na_neg].append(nb)
        rg[nb].append(na_neg)
        # ¬b -> a
        g[nb_neg].append(na)
        rg[na].append(nb_neg)

    sys.setrecursionlimit(1 << 25)

    visited = [False] * N
    order = []

    # iterative DFS for first pass
    for v in range(N):
        if not visited[v]:
            stack = [(v, 0)]
            while stack:
                node, idx = stack.pop()
                if idx == 0:
                    if visited[node]:
                        continue
                    visited[node] = True
                    stack.append((node, 1))  # post‑process marker
                    for to in g[node]:
                        if not visited[to]:
                            stack.append((to, 0))
                else:
                    order.append(node)

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