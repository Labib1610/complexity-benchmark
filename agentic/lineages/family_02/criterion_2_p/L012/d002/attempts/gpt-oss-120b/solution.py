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

    def lit_to_node(l: int) -> int:
        if l > 0:
            return 2 * (l - 1)          # true
        else:
            return 2 * (-l - 1) + 1     # false

    for _ in range(m):
        a = int(next(it)); b = int(next(it))
        u = lit_to_node(a)
        v = lit_to_node(b)
        nu = u ^ 1
        nv = v ^ 1
        # ¬a -> b
        g[nu].append(v)
        rg[v].append(nu)
        # ¬b -> a
        g[nv].append(u)
        rg[u].append(nv)

    sys.setrecursionlimit(1 << 25)

    # first pass: order by finish time
    visited = [False] * N
    order = []

    for start in range(N):
        if visited[start]:
            continue
        stack = [(start, 0)]          # (vertex, next_child_index)
        while stack:
            v, idx = stack[-1]
            if not visited[v]:
                visited[v] = True
            # explore neighbours
            if idx < len(g[v]):
                nxt = g[v][idx]
                stack[-1] = (v, idx + 1)
                if not visited[nxt]:
                    stack.append((nxt, 0))
            else:
                order.append(v)
                stack.pop()

    # second pass: assign components on reversed graph
    comp = [-1] * N
    cur_comp = 0
    for v in reversed(order):
        if comp[v] != -1:
            continue
        stack = [v]
        comp[v] = cur_comp
        while stack:
            x = stack.pop()
            for y in rg[x]:
                if comp[y] == -1:
                    comp[y] = cur_comp
                    stack.append(y)
        cur_comp += 1

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
    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()