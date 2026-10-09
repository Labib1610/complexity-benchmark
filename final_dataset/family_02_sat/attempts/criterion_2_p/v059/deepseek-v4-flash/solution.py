import sys
sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    # 2-SAT: variable i (1..n) -> node 2*i for True, 2*i+1 for False
    # We'll use 0-based indexing: node 2*i for True, 2*i+1 for False
    N = 2 * n
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]
    
    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)
    
    def node(var):
        # var > 0: True for var, var < 0: False for |var|
        if var > 0:
            return 2 * (var - 1)      # True node
        else:
            return 2 * (-var - 1) + 1 # False node
    
    for _ in range(m):
        a, b = map(int, input().split())
        na = node(-a)  # negation of a
        nb = node(-b)  # negation of b
        # clause (a or b) => (!a -> b) and (!b -> a)
        add_imp(na, node(b))
        add_imp(nb, node(a))
    
    # Kosaraju's SCC
    visited = [False] * N
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in g[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    comp = [-1] * N
    def dfs2(u, cid):
        comp[u] = cid
        for v in gr[u]:
            if comp[v] == -1:
                dfs2(v, cid)
    
    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1
    
    # Check satisfiability
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
    
    # Build assignment
    assignment = [0] * n
    for i in range(n):
        # In Kosaraju, comp id order gives topological order of SCCs in reverse
        # If True node has larger comp id, assign True
        assignment[i] = 1 if comp[2*i] > comp[2*i+1] else 0
    
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    solve()