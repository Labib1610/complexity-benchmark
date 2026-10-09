import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    N = 2 * n
    G = [[] for _ in range(N)]
    GR = [[] for _ in range(N)]

    def lit_to_idx(l: int) -> int:
        v = abs(l) - 1
        if l > 0:
            return 2 * v          # xi = true
        else:
            return 2 * v + 1      # xi = false (¬xi)

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        ia = lit_to_idx(a)
        ib = lit_to_idx(b)
        na = ia ^ 1
        nb = ib ^ 1
        # ¬a -> b
        G[na].append(ib)
        GR[ib].append(na)
        # ¬b -> a
        G[nb].append(ia)
        GR[ia].append(nb)

    # first pass: order by finish time (iterative)
    visited = [False] * N
    order = []

    for v in range(N):
        if visited[v]:
            continue
        stack = [(v, 0)]  # (node, next_child_index)
        while stack:
            node, idx = stack[-1]
            if not visited[node]:
                visited[node] = True
            # explore next neighbor
            if idx < len(G[node]):
                nxt = G[node][idx]
                stack[-1] = (node, idx + 1)
                if not visited[nxt]:
                    stack.append((nxt, 0))
            else:
                order.append(node)
                stack.pop()

    # second pass: assign components
    comp = [-1] * N
    cid = 0
    for v in reversed(order):
        if comp[v] != -1:
            continue
        stack = [v]
        comp[v] = cid
        while stack:
            node = stack.pop()
            for nxt in GR[node]:
                if comp[nxt] == -1:
                    comp[nxt] = cid
                    stack.append(nxt)
        cid += 1

    # check contradictions
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return

    # build assignment
    ans = []
    for i in range(n):
        if comp[2 * i] > comp[2 * i + 1]:
            ans.append('1')
        else:
            ans.append('0')
    print("YES")
    print(' '.join(ans))

if __name__ == "__main__":
    solve()