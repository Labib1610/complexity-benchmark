import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n, m = int(data[idx]), int(data[idx + 1]); idx += 2

    def lit(l):
        return 2 * (l - 1) if l > 0 else 2 * (-l - 1) + 1

    N = 2 * n
    adj  = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]

    for _ in range(m):
        a, b = int(data[idx]), int(data[idx + 1]); idx += 2
        la, lb = lit(a), lit(b)
        na, nb = la ^ 1, lb ^ 1
        adj[na].append(lb);  radj[lb].append(na)
        adj[nb].append(la);  radj[la].append(nb)

    # Kosaraju's SCC — iterative
    visited = [False] * N
    order = []
    for s in range(N):
        if visited[s]:
            continue
        stack = [(s, iter(adj[s]))]
        visited[s] = True
        while stack:
            v, it = stack[-1]
            try:
                w = next(it)
                if not visited[w]:
                    visited[w] = True
                    stack.append((w, iter(adj[w])))
            except StopIteration:
                order.append(v)
                stack.pop()

    comp = [-1] * N
    c = 0
    for s in reversed(order):
        if comp[s] != -1:
            continue
        stk = [s]
        while stk:
            v = stk.pop()
            if comp[v] != -1:
                continue
            comp[v] = c
            for w in radj[v]:
                if comp[w] == -1:
                    stk.append(w)
        c += 1

    # Output smallest variable (1-indexed) whose true/false literals share an SCC
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print(i + 1)
            return

solve()
