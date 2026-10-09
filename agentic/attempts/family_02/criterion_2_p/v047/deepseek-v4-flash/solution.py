import sys
sys.setrecursionlimit(1_000_000)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def node(var):
        # var > 0: marker var activated -> index var-1
        # var < 0: marker -var suppressed -> index n + (-var) - 1
        if var > 0:
            return var - 1
        else:
            return n + (-var) - 1

    def neg_node(idx):
        # negation of node idx
        if idx < n:
            return idx + n
        else:
            return idx - n

    for _ in range(m):
        a, b = map(int, input().split())
        u = node(a)
        v = node(b)
        # not u -> v
        g[neg_node(u)].append(v)
        gr[v].append(neg_node(u))
        # not v -> u
        g[neg_node(v)].append(u)
        gr[u].append(neg_node(v))

    # Kosaraju
    visited = [False] * N
    order = []

    def dfs1(v):
        visited[v] = True
        for to in g[v]:
            if not visited[to]:
                dfs1(to)
        order.append(v)

    for i in range(N):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * N
    def dfs2(v, cid):
        comp[v] = cid
        for to in gr[v]:
            if comp[to] == -1:
                dfs2(to, cid)

    cid = 0
    for v in reversed(order):
        if comp[v] == -1:
            dfs2(v, cid)
            cid += 1

    for i in range(n):
        if comp[i] == comp[i + n]:
            print("NO")
            return

    # Assign values: if comp[i] > comp[i+n] then True else False
    res = [0] * n
    for i in range(n):
        if comp[i] > comp[i + n]:
            res[i] = 1
        else:
            res[i] = 0

    print("YES")
    print(" ".join(map(str, res)))

if __name__ == "__main__":
    main()