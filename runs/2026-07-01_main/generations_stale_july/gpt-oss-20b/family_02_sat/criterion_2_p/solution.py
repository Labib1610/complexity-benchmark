import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    N = 2 * n
    adj = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]

    def lit(x):
        if x > 0:
            return 2 * (x - 1)
        else:
            return 2 * (-x - 1) + 1

    for _ in range(m):
        l1 = next(it)
        l2 = next(it)
        a = lit(l1)
        b = lit(l2)
        na = a ^ 1
        nb = b ^ 1
        adj[na].append(b)
        radj[b].append(na)
        adj[nb].append(a)
        radj[a].append(nb)

    sys.setrecursionlimit(1 << 25)
    visited = [False] * N
    order = []

    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for u in range(N):
        if not visited[u]:
            dfs1(u)

    comp = [-1] * N
    cid = 0

    def dfs2(u, cid):
        comp[u] = cid
        for v in radj[u]:
            if comp[v] == -1:
                dfs2(v, cid)

    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1

    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            sys.stdout.write("NO\n")
            return

    assignment = [0] * n
    for i in range(n):
        assignment[i] = 1 if comp[2 * i] > comp[2 * i + 1] else 0

    out_lines = ["YES", " ".join(map(str, assignment))]
    sys.stdout.write("\n".join(out_lines) + "\n")

if __name__ == "__main__":
    main()