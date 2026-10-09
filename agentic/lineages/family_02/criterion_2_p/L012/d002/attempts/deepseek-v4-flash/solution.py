import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    g = [[] for _ in range(2 * n)]
    gr = [[] for _ in range(2 * n)]

    def node(x):
        # positive x -> (x-1)*2, negative x -> (-x-1)*2+1
        if x > 0:
            return (x - 1) * 2
        else:
            return (-x - 1) * 2 + 1

    def neg_node(u):
        return u ^ 1

    for _ in range(m):
        a, b = map(int, input().split())
        u = node(a)
        v = node(b)
        # (not u) -> v
        g[neg_node(u)].append(v)
        gr[v].append(neg_node(u))
        # (not v) -> u
        g[neg_node(v)].append(u)
        gr[u].append(neg_node(v))

    # Kosaraju SCC
    visited = [False] * (2 * n)
    order = []

    def dfs1(u):
        visited[u] = True
        for w in g[u]:
            if not visited[w]:
                dfs1(w)
        order.append(u)

    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * (2 * n)
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
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return

    print("YES")
    assignment = [0] * n
    for i in range(n):
        # In Kosaraju, comp id order gives topological order of SCCs in reverse
        assignment[i] = 1 if comp[2 * i] > comp[2 * i + 1] else 0
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()