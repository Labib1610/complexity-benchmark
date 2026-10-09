import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    V = 2 * n
    g = [[] for _ in range(V)]
    gr = [[] for _ in range(V)]

    def lit_node(l: int) -> int:
        """return vertex index of literal represented by integer l"""
        if l > 0:
            # xi
            return 2 * (l - 1) + 1
        else:
            # ¬xi
            return 2 * (-l - 1)

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        na = lit_node(a)
        nb = lit_node(b)
        na_neg = na ^ 1
        nb_neg = nb ^ 1
        # ¬a -> b
        g[na_neg].append(nb)
        gr[nb].append(na_neg)
        # ¬b -> a
        g[nb_neg].append(na)
        gr[na].append(nb_neg)

    # Kosaraju first pass: order
    sys.setrecursionlimit(1 << 25)
    visited = [False] * V
    order = []

    for v in range(V):
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
    comp = [-1] * V
    cur = 0
    for v in reversed(order):
        if comp[v] == -1:
            stack = [v]
            comp[v] = cur
            while stack:
                node = stack.pop()
                for to in gr[node]:
                    if comp[to] == -1:
                        comp[to] = cur
                        stack.append(to)
            cur += 1

    # check contradictions
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