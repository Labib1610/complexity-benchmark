import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # number of vertices
    g = [[] for _ in range(N)]   # forward graph
    rg = [[] for _ in range(N)]  # reversed graph

    def lit_to_node(l: int) -> int:
        v = abs(l) - 1
        if l > 0:
            return 2 * v          # xi
        else:
            return 2 * v ^ 1      # ¬xi

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        A = lit_to_node(a)
        B = lit_to_node(b)
        NA = A ^ 1
        NB = B ^ 1
        # ¬a -> b
        g[NA].append(B)
        rg[B].append(NA)
        # ¬b -> a
        g[NB].append(A)
        rg[A].append(NB)

    sys.setrecursionlimit(1 << 25)

    # ---------- first pass: order ----------
    visited = [False] * N
    order = []

    for v in range(N):
        if not visited[v]:
            stack = [(v, 0)]  # (node, next_child_index)
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

    # ---------- second pass: components ----------
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

    # ---------- check satisfiability ----------
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