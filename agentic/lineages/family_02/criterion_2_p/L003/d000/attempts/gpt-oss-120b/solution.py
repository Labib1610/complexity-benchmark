import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # number of vertices
    g = [[] for _ in range(N)]    # forward graph
    rg = [[] for _ in range(N)]   # reverse graph

    def lit_to_idx(x: int) -> int:
        """positive -> true vertex, negative -> false vertex"""
        if x > 0:
            v = x - 1
            return 2 * v          # true
        else:
            v = -x - 1
            return 2 * v + 1      # false

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        A = lit_to_idx(a)
        B = lit_to_idx(b)
        NA = A ^ 1
        NB = B ^ 1
        # ¬A -> B
        g[NA].append(B)
        rg[B].append(NA)
        # ¬B -> A
        g[NB].append(A)
        rg[A].append(NB)

    sys.setrecursionlimit(1 << 25)

    # first pass: order by finish time
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

    # second pass: assign components
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

    # check for contradictions
    assignment = [0] * n
    for i in range(n):
        t = 2 * i
        f = t ^ 1
        if comp[t] == comp[f]:
            print("NO")
            return
        assignment[i] = 1 if comp[t] > comp[f] else 0

    # output
    out = ["YES", " ".join(map(str, assignment))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()