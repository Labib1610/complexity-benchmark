import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    clauses = []
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        clauses.append((l1, l2, l3))
    
    # 2-SAT formulation:
    # For each template (l1, l2, l3), we need at least one condition active.
    # This is equivalent to: (l1 OR l2 OR l3)
    # Convert to CNF: (l1 OR l2 OR l3) = (l1 OR l2) AND (l1 OR l3) AND (l2 OR l3)
    
    # Build implication graph
    # Node i: variable i is True (Phase 1)
    # Node i+N: variable i is False (Phase 0)
    # Total 2N nodes: 0 to N-1 for True, N to 2N-1 for False
    
    N = n
    adj = [[] for _ in range(2 * N)]
    adj_rev = [[] for _ in range(2 * N)]
    
    def get_node(lit):
        # lit > 0: node lit-1 (True state)
        # lit < 0: node |lit|-1 + N (False state)
        if lit > 0:
            return lit - 1
        else:
            return (-lit) - 1 + N
    
    def get_neg(node):
        if node < N:
            return node + N
        else:
            return node - N
    
    def add_implication(u, v):
        adj[u].append(v)
        adj_rev[v].append(u)
    
    # Add 2-SAT clauses
    for l1, l2, l3 in clauses:
        nodes = [get_node(l1), get_node(l2), get_node(l3)]
        # (a OR b OR c) = (a OR b) AND (a OR c) AND (b OR c)
        for i in range(3):
            for j in range(i + 1, 3):
                a, b = nodes[i], nodes[j]
                # (a OR b) = (!a -> b) AND (!b -> a)
                add_implication(get_neg(a), b)
                add_implication(get_neg(b), a)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * N)
    order = []
    
    def dfs1(v):
        stack = [(v, 0)]
        while stack:
            node, idx = stack[-1]
            if not visited[node]:
                visited[node] = True
            if idx < len(adj[node]):
                neighbor = adj[node][idx]
                stack[-1] = (node, idx + 1)
                if not visited[neighbor]:
                    stack.append((neighbor, 0))
            else:
                stack.pop()
                order.append(node)
    
    for v in range(2 * N):
        if not visited[v]:
            dfs1(v)
    
    visited = [False] * (2 * N)
    comp = [-1] * (2 * N)
    comp_id = 0
    
    def dfs2(v, cid):
        stack = [v]
        while stack:
            node = stack[-1]
            if not visited[node]:
                visited[node] = True
                comp[node] = cid
                for neighbor in adj_rev[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
                        break
                else:
                    stack.pop()
            else:
                stack.pop()
    
    for v in reversed(order):
        if not visited[v]:
            dfs2(v, comp_id)
            comp_id += 1
    
    # Check for contradiction
    for i in range(N):
        if comp[i] == comp[i + N]:
            print("NO")
            return
    
    # Assign values
    assignment = [0] * N
    for i in range(N):
        # If True state has higher component id, assign True
        if comp[i] > comp[i + N]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(" ".join(map(str, assignment)))

solve()