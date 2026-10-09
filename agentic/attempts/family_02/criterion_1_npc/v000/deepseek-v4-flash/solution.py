import sys
sys.setrecursionlimit(500000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n, m = int(input_data[0]), int(input_data[1])
    
    # variables: 1..n for positive, n+1..2n for negative (n + i means NOT i)
    idx = 0
    clauses = []
    for _ in range(m):
        l1 = int(input_data[idx+2])
        l2 = int(input_data[idx+3])
        l3 = int(input_data[idx+4])
        idx += 3
        
        def lit(x):
            if x > 0:
                return (x, True)
            else:
                return (-x, False)
        
        a, av = lit(l1)
        b, bv = lit(l2)
        c, cv = lit(l3)
        
        # Add (a or b), (b or c), (a or c)
        clauses.append((a, av, b, bv))
        clauses.append((b, bv, c, cv))
        clauses.append((a, av, c, cv))
    
    N = 2 * n
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]
    
    def var_id(x, val):
        # x: task number, val: True if positive
        if val:
            return x - 1
        else:
            return n + x - 1
    
    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)
    
    # Add implication edges for (p or q)
    for a, av, b, bv in clauses:
        na = var_id(a, not av)
        nb = var_id(b, not bv)
        pa = var_id(a, av)
        pb = var_id(b, bv)
        # ¬p -> q
        add_imp(na, pb)
        # ¬q -> p
        add_imp(nb, pa)
    
    # Kosaraju SCC
    visited = [False]*N
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
    
    comp = [-1]*N
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
    
    for i in range(n):
        if comp[i] == comp[n+i]:
            print("NO")
            return
    
    assignment = [0]*n
    for i in range(n):
        # If comp[¬i] < comp[i] then set True
        if comp[n+i] < comp[i]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    solve()