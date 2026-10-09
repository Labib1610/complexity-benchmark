import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))

    # Each clause is a disjunction of 3 literals.
    # We want to find an assignment satisfying all clauses.
    # This is a 3-SAT problem which can be reduced to 2-SAT.
    # For a clause (l1 v l2 v l3), it is equivalent to:
    # (!l1 -> l2) & (!l1 -> l3) & (!l2 -> l1) & (!l2 -> l3) & (!l3 -> l1) & (!l3 -> l2)
    
    adj = [[] for _ in range(2 * n)]
    
    def get_node(lit):
        # lit is a non-zero integer, |lit| <= n
        # positive lit -> 2*(lit-1), negative lit -> 2*(-lit-1) + 1
        if lit > 0:
            return 2 * (lit - 1)
        else:
            return 2 * (-lit - 1) + 1
            
    def add_imp(u, v):
        adj[u].append(v)
        
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        
        u1 = get_node(l1)
        u2 = get_node(l2)
        u3 = get_node(l3)
        
        # Negations
        nu1 = u1 ^ 1
        nu2 = u2 ^ 1
        nu3 = u3 ^ 1
        
        add_imp(nu1, u2)
        add_imp(nu1, u3)
        add_imp(nu2, u1)
        add_imp(nu2, u3)
        add_imp(nu3, u1)
        add_imp(nu3, u2)

    # Kosaraju's algorithm to find Strongly Connected Components
    sys.setrecursionlimit(10000)
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
            
    radj = [[] for _ in range(2 * n)]
    for u in range(2 * n):
        for v in adj[u]:
            radj[v].append(u)
            
    comp_id = [-1] * (2 * n)
    cid = 0
    
    def dfs2(u, cid):
        comp_id[u] = cid
        for v in radj[u]:
            if comp_id[v] == -1:
                dfs2(v, cid)

    for u in reversed(order):
        if comp_id[u] == -1:
            dfs2(u, cid)
            cid += 1

    # Check for unsatisfiability and assign values
    ans = [0] * n
    for i in range(n):
        pos = 2 * i
        neg = 2 * i + 1
        if comp_id[pos] == comp_id[neg]:
            print("NO")
            return
        if comp_id[pos] > comp_id[neg]:
            ans[i] = 1
        else:
            ans[i] = 0

    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    solve()