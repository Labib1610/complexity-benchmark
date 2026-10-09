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

    def lit(k: int) -> int:
        idx = abs(k) - 1
        return 2 * idx + (1 if k > 0 else 0)

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        la = lit(a)
        lb = lit(b)
        na = la ^ 1
        nb = lb ^ 1
        G[na].append(lb)
        GR[lb].append(na)
        G[nb].append(la)
        GR[la].append(nb)

    # first pass: order
    visited = [False] * N
    order = []

    for v in range(N):
        if not visited[v]:
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
        if comp[v] == -1:
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
    ans = [0] * n
    for i in range(n):
        ans[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()