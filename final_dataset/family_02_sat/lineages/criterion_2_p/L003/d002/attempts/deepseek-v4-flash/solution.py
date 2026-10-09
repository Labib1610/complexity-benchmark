import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(2 * n + 1)]
    
    def node(var, val):
        # var: 1..n, val: 0 or 1
        return var * 2 + val
    
    for _ in range(m):
        a, b = map(int, input().split())
        va = abs(a)
        vb = abs(b)
        xa = 1 if a > 0 else 0
        xb = 1 if b > 0 else 0
        # Clause: (xa == va) OR (xb == vb)
        # Equivalent to (not (xa == va)) -> (xb == vb)
        # and (not (xb == vb)) -> (xa == va)
        # not (xa == va) means xa != va, i.e. xa = 1-va
        na = 1 - xa
        nb = 1 - xb
        adj[node(va, na)].append(node(vb, xb))
        adj[node(vb, nb)].append(node(va, xa))
    
    N = 2 * n + 1
    visited = [False] * N
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(2, N):
        if not visited[i]:
            dfs1(i)
    
    comp = [-1] * N
    radj = [[] for _ in range(N)]
    for u in range(2, N):
        for v in adj[u]:
            radj[v].append(u)
    
    def dfs2(u, cid):
        comp[u] = cid
        for v in radj[u]:
            if comp[v] == -1:
                dfs2(v, cid)
    
    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1
    
    assignment = [0] * (n + 1)
    for i in range(1, n + 1):
        if comp[node(i, 0)] == comp[node(i, 1)]:
            print("NO")
            return
        assignment[i] = 0 if comp[node(i, 0)] > comp[node(i, 1)] else 1
    
    print("YES")
    print(" ".join(str(assignment[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()