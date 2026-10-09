import sys

sys.setrecursionlimit(1 << 25)

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

    def node(var: int, val: int) -> int:
        return 2 * var + val  # val 0 = false, 1 = true

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))

        v1 = abs(l1) - 1
        val1 = 1 if l1 > 0 else 0
        v2 = abs(l2) - 1
        val2 = 1 if l2 > 0 else 0

        a = node(v1, val1)
        na = node(v1, 1 - val1)
        b = node(v2, val2)
        nb = node(v2, 1 - val2)

        # ¬a -> b
        G[na].append(b)
        GR[b].append(na)
        # ¬b -> a
        G[nb].append(a)
        GR[a].append(nb)

    visited = [False] * N
    order = []

    # iterative DFS for first pass
    for start in range(N):
        if visited[start]:
            continue
        stack = [(start, 0)]
        while stack:
            v, idx = stack[-1]
            if not visited[v]:
                visited[v] = True
            # explore neighbours
            if idx < len(G[v]):
                nxt = G[v][idx]
                stack[-1] = (v, idx + 1)
                if not visited[nxt]:
                    stack.append((nxt, 0))
            else:
                order.append(v)
                stack.pop()

    comp = [-1] * N
    cid = 0
    # second pass on reversed graph
    for v in reversed(order):
        if comp[v] != -1:
            continue
        stack = [v]
        comp[v] = cid
        while stack:
            cur = stack.pop()
            for nxt in GR[cur]:
                if comp[nxt] == -1:
                    comp[nxt] = cid
                    stack.append(nxt)
        cid += 1

    # check satisfiability
    for i in range(n):
        if comp[node(i, 0)] == comp[node(i, 1)]:
            print("NO")
            return

    # build assignment
    ans = []
    for i in range(n):
        val = 1 if comp[node(i, 1)] > comp[node(i, 0)] else 0
        ans.append(str(val))

    print("YES")
    print(" ".join(ans))


if __name__ == "__main__":
    solve()