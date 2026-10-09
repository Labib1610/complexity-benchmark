import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    N = 2 * n                     # total vertices
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def lit_to_idx(l: int) -> int:
        if l > 0:
            return (l - 1) * 2 + 1   # true
        else:
            return (-l - 1) * 2       # false

    for _ in range(m):
        a = int(next(it)); b = int(next(it))
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

    # first pass: order
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

    # check satisfiability and build answer
    ans = [0] * n
    for i in range(n):
        f = 2 * i
        t = f ^ 1
        if comp[f] == comp[t]:
            print("NO")
            return
        ans[i] = 1 if comp[t] > comp[f] else 0

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()