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

    def lit_idx(x: int) -> int:
        v = abs(x) - 1
        return 2 * v + (0 if x > 0 else 1)

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        a_idx = lit_idx(a)
        b_idx = lit_idx(b)
        na = a_idx ^ 1  # negation
        nb = b_idx ^ 1
        # ¬a -> b
        g[na].append(b_idx)
        rg[b_idx].append(na)
        # ¬b -> a
        g[nb].append(a_idx)
        rg[a_idx].append(nb)

    visited = [False] * N
    order = []

    # iterative DFS for order
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

    comp = [-1] * N
    cid = 0
    # second pass
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
        assignment[i] = 1 if comp[2 * i] > comp[2 * i + 1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()