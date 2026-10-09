import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # 2-SAT problem
    # Variable x_i: sensor i is Active (1)
    # x_i = True means Active, x_i = False means Standby
    # For each routine (a, b, c), at least one condition must hold
    # If a > 0: need x_a = True; if a < 0: need x_{-a} = False
    # Clause: (cond_a OR cond_b OR cond_c)
    # Convert to 2-SAT by splitting: (cond_a OR cond_b) AND (cond_a OR cond_c) AND (cond_b OR cond_c)
    
    # Node indexing:
    # For variable i (1-indexed):
    #   2*(i-1) = False node (Standby)
    #   2*(i-1)+1 = True node (Active)
    # Total nodes: 2*n
    
    N = 2 * n
    adj = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]
    
    def get_node(sensor_idx, is_active):
        # sensor_idx is 1-indexed
        # is_active: True for Active (1), False for Standby (0)
        # returns node index
        idx = sensor_idx - 1
        return 2 * idx + (1 if is_active else 0)
    
    def add_implication(u, v):
        adj[u].append(v)
        radj[v].append(u)
    
    def add_clause(sensor_a, val_a, sensor_b, val_b):
        # (sensor_a == val_a) OR (sensor_b == val_b)
        u = get_node(sensor_a, val_a)
        v = get_node(sensor_b, val_b)
        # u OR v is equivalent to (not u -> v) AND (not v -> u)
        add_implication(u ^ 1, v)
        add_implication(v ^ 1, u)
    
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        
        # Parse conditions
        def parse(x):
            if x > 0:
                return (x, True)
            else:
                return (-x, False)
        
        sa, va = parse(a)
        sb, vb = parse(b)
        sc, vc = parse(c)
        
        # Add 2-SAT clauses
        add_clause(sa, va, sb, vb)
        add_clause(sa, va, sc, vc)
        add_clause(sb, vb, sc, vc)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * N
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack[-1]
            if not visited[node]:
                visited[node] = True
            if idx < len(adj[node]):
                v = adj[node][idx]
                stack[-1] = (node, idx + 1)
                if not visited[v]:
                    stack.append((v, 0))
            else:
                stack.pop()
                order.append(node)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    visited = [False] * N
    comp = [-1] * N
    cid = 0
    
    def dfs2(u, c):
        stack = [u]
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                comp[node] = c
                for v in radj[node]:
                    if not visited[v]:
                        stack.append(v)
    
    for u in reversed(order):
        if not visited[u]:
            dfs2(u, cid)
            cid += 1
    
    # Check for contradiction
    for i in range(n):
        if comp[2*i] == comp[2*i + 1]:
            print("NO")
            return
    
    # Assign values
    assignment = [0] * n
    for i in range(n):
        # If True node has higher topo order (lower comp id), set to True
        if comp[2*i + 1] < comp[2*i]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()