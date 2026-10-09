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

    def lit_to_node(x: int) -> int:
        v = abs(x) - 1
        if x > 0:
            return 2 * v + 1   # true
        else:
            return 2 * v       # false

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        u = lit_to_node(a)
        v = lit_to_node(b)
        nu = u ^ 1
        nv = v ^ 1
        G[nu].append(v)
        GR[v].append(nu)
        G[nv].append(u)
        GR[u].append(nv)

    # first pass: order by finish time
    visited = [False] * N
    order = []

    for start in range(N):
        if visited[start]:
            continue
        stack = [(start, 0)]  # (vertex, next child index)
        while stack:
            v, idx = stack[-1]
            if not visited[v]:
                visited[v] = True
            # explore next neighbour
            if idx < len(G[v]):
                nxt = G[v][idx]
                stack[-1] = (v, idx + 1)
                if not visited[nxt]:
                    stack.append((nxt, 0))
            else:
                order.append(v)
                stack.pop()

    # second pass: assign components on reversed graph
    comp = [-1] * N
    cid = 0
    for v in reversed(order):
        if comp[v] != -1:
            continue
        stack = [v]
        comp[v] = cid
        while stack:
            cur = stack.pop()
            for nb in GR[cur]:
                if comp[nb] == -1:
                    comp[nb] = cid
                    stack.append(nb)
        cid += 1

    # check satisfiability
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            sys.stdout.write("NO")
            return

    # build assignment
    assign = [0] * n
    for i in range(n):
        assign[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    out = ["YES", " ".join(map(str, assign))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()