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
    
    # 2-SAT formulation:
    # For each rule (a,b,c), at least one must hold.
    # If a>0, literal is x_a; if a<0, literal is ~x_{-a}.
    # We add clauses: (a or b), (a or c), (b or c).
    # This is equivalent to (a or b or c) for 3 literals.
    
    # Build implication graph
    # Variables 1..n, literal 2*x for x=True, 2*x+1 for x=False
    # literal id: for positive a -> 2*a (meaning x_a true)
    #             for negative a -> 2*(-a)+1 (meaning x_{-a} false)
    
    def lit(val):
        if val > 0:
            return 2 * val
        else:
            return 2 * (-val) + 1
    
    def neg(l):
        return l ^ 1
    
    adj = [[] for _ in range(2*n + 2)]
    radj = [[] for _ in range(2*n + 2)]
    
    def add_impl(u, v):
        adj[u].append(v)
        radj[v].append(u)
    
    def add_or(u, v):
        add_impl(neg(u), v)
        add_impl(neg(v), u)
    
    for a, b, c in clauses:
        la, lb, lc = lit(a), lit(b), lit(c)
        add_or(la, lb)
        add_or(la, lc)
        add_or(lb, lc)
    
    # SCC via Kosaraju
    visited = [False] * (2*n + 2)
    order = []
    for i in range(2, 2*n + 2):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                node, ptr = stack[-1]
                if ptr == 0:
                    visited[node] = True
                if ptr < len(adj[node]):
                    child = adj[node][ptr]
                    stack[-1] = (node, ptr + 1)
                    if not visited[child]:
                        stack.append((child, 0))
                else:
                    stack.pop()
                    order.append(node)
    
    comp = [-1] * (2*n + 2)
    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            stack = [u]
            comp[u] = cid
            while stack:
                node = stack.pop()
                for child in radj[node]:
                    if comp[child] == -1:
                        comp[child] = cid
                        stack.append(child)
            cid += 1
    
    assignment = [0] * (n + 1)
    for i in range(1, n + 1):
        if comp[2*i] == comp[2*i + 1]:
            print("NO")
            return
        assignment[i] = 1 if comp[2*i] < comp[2*i + 1] else 0
    
    print("YES")
    print(' '.join(str(assignment[i]) for i in range(1, n + 1)))

solve()