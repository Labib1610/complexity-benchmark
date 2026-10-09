import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n + 2
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]
    
    def node(lit):
        if lit > 0:
            return 2 * lit
        else:
            return 2 * (-lit) + 1
    
    def neg(lit):
        return lit ^ 1
    
    for _ in range(m):
        a, b = map(int, input().split())
        u = node(a)
        v = node(b)
        # not a -> b
        g[neg(u)].append(v)
        gr[v].append(neg(u))
        # not b -> a
        g[neg(v)].append(u)
        gr[u].append(neg(v))
    
    # Kosaraju
    visited = [False] * N
    order = []
    
    def dfs1(u):
        visited[u] = True
        for w in g[u]:
            if not visited[w]:
                dfs1(w)
        order.append(u)
    
    for i in range(2, N):
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
    
    for j in range(1, n + 1):
        if comp[2 * j] == comp[2 * j + 1]:
            print(j)
            return

if __name__ == "__main__":
    solve()