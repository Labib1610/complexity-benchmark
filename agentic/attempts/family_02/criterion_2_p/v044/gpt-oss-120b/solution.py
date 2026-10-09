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

    def lit_id(x: int) -> int:
        v = abs(x) - 1
        if x > 0:
            return v * 2          # true
        else:
            return v * 2 ^ 1      # false (negated parity)

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        ida = lit_id(a)
        idb = lit_id(b)
        na = ida ^ 1
        nb = idb ^ 1
        # ¬a -> b
        g[na].append(idb)
        rg[idb].append(na)
        # ¬b -> a
        g[nb].append(ida)
        rg[ida].append(nb)

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
                    for to in g[node]:
                        if not visited[to]:
                            stack.append((to, 0))
                else:
                    order.append(node)

    comp = [-1] * N
    cur = 0
    # second pass on reversed graph
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

    # check satisfiability
    for i in range(n):
        if comp[2 * i] == comp[2 * i ^ 1]:
            print("NO")
            return

    # build answer
    ans = []
    for i in range(n):
        val = 1 if comp[2 * i] > comp[2 * i ^ 1] else 0
        ans.append(str(val))

    print("YES")
    print(' '.join(ans))

if __name__ == "__main__":
    solve()