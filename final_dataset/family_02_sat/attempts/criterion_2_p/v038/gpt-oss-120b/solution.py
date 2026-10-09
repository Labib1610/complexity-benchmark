import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # total vertices
    g = [[] for _ in range(N)]   # forward graph
    rg = [[] for _ in range(N)]  # reversed graph

    def lit_idx(c: int) -> int:
        v = abs(c) - 1            # 0‑based variable index
        if c > 0:
            return 2 * v          # x_i
        else:
            return 2 * v + 1      # ¬x_i

    for _ in range(m):
        c1 = int(next(it))
        c2 = int(next(it))
        a = lit_idx(c1)
        b = lit_idx(c2)
        na = a ^ 1                 # negation
        nb = b ^ 1
        # ¬a -> b
        g[na].append(b)
        rg[b].append(na)
        # ¬b -> a
        g[nb].append(a)
        rg[a].append(nb)

    sys.setrecursionlimit(1 << 25)

    # ---------- first pass: order ----------
    visited = [False] * N
    order = []

    for v in range(N):
        if not visited[v]:
            stack = [(v, 0)]          # (vertex, next_child_index)
            visited[v] = True
            while stack:
                cur, idx = stack[-1]
                if idx < len(g[cur]):
                    nxt = g[cur][idx]
                    stack[-1] = (cur, idx + 1)
                    if not visited[nxt]:
                        visited[nxt] = True
                        stack.append((nxt, 0))
                else:
                    order.append(cur)
                    stack.pop()

    # ---------- second pass: components ----------
    comp = [-1] * N
    cur_comp = 0
    for v in reversed(order):
        if comp[v] == -1:
            stack = [v]
            comp[v] = cur_comp
            while stack:
                cur = stack.pop()
                for nxt in rg[cur]:
                    if comp[nxt] == -1:
                        comp[nxt] = cur_comp
                        stack.append(nxt)
            cur_comp += 1

    # ---------- check satisfiability ----------
    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        # larger component id => true
        assignment[i] = 1 if comp[2 * i] > comp[2 * i + 1] else 0

    # ---------- output ----------
    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()