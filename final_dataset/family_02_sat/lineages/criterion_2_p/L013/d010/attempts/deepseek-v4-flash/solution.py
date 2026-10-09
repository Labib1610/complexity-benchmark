import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    # 2-SAT: variable i (0-indexed) -> s_{i+1}
    # We'll use 2*i for false, 2*i+1 for true
    N = 2 * n
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]
    
    def add_imp(u, v):
        g[u].append(v)
        rg[v].append(u)
    
    def add_clause(a, b):
        # a and b are literals: (val, var_index) where val True means s=1
        # Clause: a or b
        # (not a -> b) and (not b -> a)
        # not a:
        na = (a[0] ^ 1, a[1])
        nb = (b[0] ^ 1, b[1])
        # not a -> b
        add_imp(na[0]*n + na[1], b[0]*n + b[1])
        # not b -> a
        add_imp(nb[0]*n + nb[1], a[0]*n + a[1])
    
    for _ in range(m):
        l1, l2 = map(int, input().split())
        # t_l = 1 condition:
        # if l > 0: t=1 iff s=0 -> literal (False, idx)
        # if l < 0: t=1 iff s=1 -> literal (True, idx)
        def t_eq_1(l):
            idx = abs(l) - 1
            if l > 0:
                return (0, idx)  # s=0
            else:
                return (1, idx)  # s=1
        
        # We need not (t1=1 and t2=1) => (t1=0) or (t2=0)
        # t=0 is negation of t=1
        def t_eq_0(l):
            idx = abs(l) - 1
            if l > 0:
                return (1, idx)  # s=1
            else:
                return (0, idx)  # s=0
        
        a = t_eq_0(l1)
        b = t_eq_0(l2)
        add_clause(a, b)
    
    # Kosaraju SCC
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
        for v in rg[u]:
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
    
    # Assign values
    assignment = [False] * n
    for i in range(n):
        # In Kosaraju, comp id order: if comp[2*i] > comp[2*i+1] then true
        assignment[i] = comp[2*i] > comp[2*i+1]
    
    print("YES")
    print(' '.join('1' if assignment[i] else '0' for i in range(n)))

if __name__ == "__main__":
    solve()