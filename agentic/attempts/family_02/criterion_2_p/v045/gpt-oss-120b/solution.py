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

    def lit_node(k: int):
        var = abs(k) - 1
        val = 1 if k > 0 else 0
        return 2 * var + val

    for _ in range(m):
        a = int(next(it)); b = int(next(it))
        na = lit_node(-a)   # ¬a
        nb = lit_node(-b)   # ¬b
        a_node = lit_node(a)
        b_node = lit_node(b)
        # ¬a -> b
        g[na].append(b_node)
        rg[b_node].append(na)
        # ¬b -> a
        g[nb].append(a_node)
        rg[a_node].append(nb)

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
    cid = 0
    # second pass on reversed graph
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
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
        # component with larger id appears earlier in topological order
        assignment[i] = 1 if comp[2*i] < comp[2*i+1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()