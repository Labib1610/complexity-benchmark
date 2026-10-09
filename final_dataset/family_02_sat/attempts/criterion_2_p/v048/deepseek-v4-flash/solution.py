import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def node(var):
        # var > 0: literal x, var < 0: literal ¬x
        if var > 0:
            return (var - 1) * 2      # even index for positive
        else:
            return (-var - 1) * 2 + 1 # odd index for negative

    def neg_node(idx):
        return idx ^ 1

    for _ in range(m):
        a, b = map(int, input().split())
        u = node(a)
        v = node(b)
        # ¬u -> v
        g[neg_node(u)].append(v)
        gr[v].append(neg_node(u))
        # ¬v -> u
        g[neg_node(v)].append(u)
        gr[u].append(neg_node(v))

    # Kosaraju
    visited = [False] * N
    order = []
    def dfs1(u):
        visited[u] = True
        for w in g[u]:
            if not visited[w]:
                dfs1(w)
        order.append(u)

    for i in range(N):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * N
    def dfs2(u, cid):
        comp[u] = cid
        for w in gr[u]:
            if comp[w] == -1:
                dfs2(w, cid)

    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1

    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return

    print("YES")
    # Assign values: if comp[2*i] > comp[2*i+1], set 1 else 0
    res = []
    for i in range(n):
        if comp[2*i] > comp[2*i+1]:
            res.append('1')
        else:
            res.append('0')
    print(' '.join(res))

if __name__ == "__main__":
    solve()