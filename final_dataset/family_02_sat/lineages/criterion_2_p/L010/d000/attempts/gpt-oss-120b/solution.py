import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    N = 2 * n
    G = [[] for _ in range(N)]
    GR = [[] for _ in range(N)]

    def lit_index(l: int) -> int:
        v = abs(l) - 1
        return v if l > 0 else v + n

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        ia = lit_index(a)
        ib = lit_index(b)
        na = ia + n if ia < n else ia - n
        nb = ib + n if ib < n else ib - n
        # ¬a -> b
        G[na].append(ib)
        GR[ib].append(na)
        # ¬b -> a
        G[nb].append(ia)
        GR[ia].append(nb)

    sys.setrecursionlimit(1 << 25)

    visited = [False] * N
    order = []

    # iterative DFS for first pass
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
                    for to in G[node]:
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
                for to in GR[node]:
                    if comp[to] == -1:
                        comp[to] = cid
                        stack.append(to)
            cid += 1

    # check satisfiability
    for i in range(n):
        if comp[i] == comp[i + n]:
            sys.stdout.write("NO")
            return

    # build assignment
    assign = [0] * n
    for i in range(n):
        assign[i] = 1 if comp[i] > comp[i + n] else 0

    out = ["YES", " ".join(map(str, assign))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()