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

    def lit_to_node(x: int) -> int:
        v = abs(x) - 1
        base = v * 2
        return base if x > 0 else base ^ 1

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

    # ---------- first pass ----------
    visited = [False] * N
    order = []

    for v in range(N):
        if not visited[v]:
            stack = [(v, 0)]  # (node, next child index)
            while stack:
                node, idx = stack[-1]
                if not visited[node]:
                    visited[node] = True
                # iterate neighbours
                if idx < len(g[node]):
                    nxt = g[node][idx]
                    stack[-1] = (node, idx + 1)
                    if not visited[nxt]:
                        stack.append((nxt, 0))
                else:
                    order.append(node)
                    stack.pop()

    # ---------- second pass ----------
    comp = [-1] * N
    cur_comp = 0
    for v in reversed(order):
        if comp[v] == -1:
            stack = [v]
            comp[v] = cur_comp
            while stack:
                node = stack.pop()
                for nxt in rg[node]:
                    if comp[nxt] == -1:
                        comp[nxt] = cur_comp
                        stack.append(nxt)
            cur_comp += 1

    # ---------- check ----------
    assignment = [0] * n
    for i in range(n):
        t = 2 * i
        f = t ^ 1
        if comp[t] == comp[f]:
            print("NO")
            return
        assignment[i] = 1 if comp[t] > comp[f] else 0

    # ---------- output ----------
    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()