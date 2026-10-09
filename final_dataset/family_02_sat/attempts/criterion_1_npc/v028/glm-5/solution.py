import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    idx = 2
    clauses = []
    for _ in range(m):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        clauses.append((a, b, c))
    
    # 2-SAT: variable i (1-indexed) true means truck i is on upper corridor (1)
    # literal x: positive -> x is true; negative -> x is false
    # We need to find assignment satisfying all clauses (each clause is OR of 3 literals)
    
    # Build implication graph
    # For literal L, its negation is -L
    # For clause (a OR b OR c):
    #   not a -> b, not a -> c
    #   not b -> a, not b -> c
    #   not c -> a, not c -> b
    
    # Node numbering: literal L -> if L>0: 2*(L-1); if L<0: 2*(-L-1)+1
    # Negation flips last bit
    
    size = 2 * n
    adj = [[] for _ in range(size)]
    radj = [[] for _ in range(size)]
    
    def node(lit):
        if lit > 0:
            return 2 * (lit - 1)
        else:
            return 2 * (-lit - 1) + 1
    
    def add_impl(u, v):
        adj[u].append(v)
        radj[v].append(u)
    
    for a, b, c in clauses:
        na, nb, nc = node(a), node(b), node(c)
        nna, nnb, nnc = na ^ 1, nb ^ 1, nc ^ 1
        # not a -> b, not a -> c
        add_impl(nna, nb)
        add_impl(nna, nc)
        # not b -> a, not b -> c
        add_impl(nnb, na)
        add_impl(nnb, nc)
        # not c -> a, not c -> b
        add_impl(nnc, na)
        add_impl(nnc, nb)
    
    # Kosaraju SCC
    visited = [False] * size
    order = []
    for i in range(size):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                v, ei = stack[-1]
                if ei == 0:
                    visited[v] = True
                if ei < len(adj[v]):
                    to = adj[v][ei]
                    stack[-1] = (v, ei + 1)
                    if not visited[to]:
                        stack.append((to, 0))
                else:
                    stack.pop()
                    order.append(v)
    
    comp = [-1] * size
    cid = 0
    for i in reversed(order):
        if comp[i] == -1:
            stack = [i]
            comp[i] = cid
            while stack:
                v = stack.pop()
                for to in radj[v]:
                    if comp[to] == -1:
                        comp[to] = cid
                        stack.append(to)
            cid += 1
    
    # Check satisfiability
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
    
    # Assign: if comp[2*i] < comp[2*i+1] then variable i is true (upper)
    # Actually standard: if comp of literal < comp of negation, literal is true
    # But we need to be careful: in Kosaraju with this order, 
    # if comp[x] < comp[not x] then x is true
    result = []
    for i in range(n):
        if comp[2*i] < comp[2*i+1]:
            result.append(1)
        else:
            result.append(0)
    
    print("YES")
    print(" ".join(map(str, result)))

solve()