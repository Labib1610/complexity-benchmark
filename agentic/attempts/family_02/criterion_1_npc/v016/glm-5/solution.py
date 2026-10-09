import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    interlocks = []
    for _ in range(m):
        c1 = int(next(it)); c2 = int(next(it)); c3 = int(next(it))
        interlocks.append((c1, c2, c3))
    
    # Literal representation: for valve i (1-indexed), literal 2*i is (x_i = True), literal 2*i+1 is (x_i = False)
    # Implication graph edges: if literal u implies literal v (u -> v)
    N_vars = n
    N_lits = 2 * N_vars + 2  # 1-based indexing for literals up to 2*n+1
    adj = [[] for _ in range(N_lits)]
    radj = [[] for _ in range(N_lits)]
    
    # Helper to get literal index for a condition
    # condition c: if c > 0, want x_c = True; if c < 0, want x_|c| = False
    def get_lit(c):
        v = abs(c)
        if c > 0:
            return 2 * v      # Literal representing x_v = True
        else:
            return 2 * v + 1  # Literal representing x_v = False
    
    # The negation of a literal index
    def neg(lit_idx):
        return lit_idx ^ 1
    
    for c1, c2, c3 in interlocks:
        # Clause: (c1 OR c2 OR c3)
        # 2-SAT implications: if condition fails, at least one of the other two must hold
        # (~c1 -> c2) and (~c1 -> c3)
        l1 = get_lit(c1)
        l2 = get_lit(c2)
        l3 = get_lit(c3)
        
        # ~l1 -> l2
        adj[neg(l1)].append(l2)
        radj[l2].append(neg(l1))
        
        # ~l1 -> l3
        adj[neg(l1)].append(l3)
        radj[l3].append(neg(l1))
        
        # ~l2 -> l1
        adj[neg(l2)].append(l1)
        radj[l1].append(neg(l2))
        
        # ~l2 -> l3
        adj[neg(l2)].append(l3)
        radj[l3].append(neg(l2))
        
        # ~l3 -> l1
        adj[neg(l3)].append(l1)
        radj[l1].append(neg(l3))
        
        # ~l3 -> l2
        adj[neg(l3)].append(l2)
        radj[l2].append(neg(l3))
    
    # Kosaraju's algorithm for SCC
    visited = [False] * N_lits
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack.pop()
            if idx == 0:
                if visited[node]:
                    continue
                visited[node] = True
                stack.append((node, 1))
                for v in reversed(adj[node]):
                    if not visited[v]:
                        stack.append((v, 0))
            else:
                order.append(node)
    
    for u in range(2, N_lits):  # Literals are from 2 to 2*n+1
        if not visited[u]:
            dfs1(u)
    
    comp_id = [-1] * N_lits
    cid = 0
    
    def dfs2(u, cid):
        stack = [u]
        visited_scc = set()
        while stack:
            node = stack.pop()
            if node in visited_scc:
                continue
            visited_scc.add(node)
            comp_id[node] = cid
            for v in radj[node]:
                if comp_id[v] == -1:
                    stack.append(v)
    
    for u in reversed(order):
        if comp_id[u] == -1:
            dfs2(u, cid)
            cid += 1
    
    # Check for contradiction: x and ~x in same SCC
    assignment = [False] * (N_vars + 1)
    for v in range(1, N_vars + 1):
        lit_true = 2 * v
        lit_false = 2 * v + 1
        if comp_id[lit_true] == comp_id[lit_false]:
            print("NO")
            return
        assignment[v] = comp_id[lit_true] > comp_id[lit_false]
    
    print("YES")
    print(' '.join('1' if assignment[i] else '0' for i in range(1, N_vars + 1)))

solve()