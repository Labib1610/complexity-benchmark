import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # Each clause is a list of 3 literals.
    # Literal encoding: positive for True (focusing), negative for False (defocusing).
    # 1-indexed variables.
    clauses = []
    for _ in range(m):
        clause = []
        for _ in range(3):
            val = int(next(it))
            clause.append(val)
        clauses.append(clause)
    
    # 2-SAT setup
    # Variables are 1..n.
    # Implication graph has 2*n nodes: 1..n for True, n+1..2n for False.
    # Node u corresponds to literal u (True), node n+u corresponds to literal -u (False).
    # Actually, let's map:
    # Index(u) = u if u > 0
    # Index(-u) = n + u
    # Total nodes = 2*n
    
    num_nodes = 2 * n
    adj = [[] for _ in range(num_nodes + 1)]
    
    def get_node(lit):
        if lit > 0:
            return lit
        else:
            return n + (-lit)
    
    # Build implication graph
    # Clause (a v b v c) is equivalent to:
    # (!a -> b) and (!a -> c)
    # (!b -> a) and (!b -> c)
    # (!c -> a) and (!c -> b)
    
    for c in clauses:
        a, b, c_val = c[0], c[1], c[2]
        
        u1, u2, u3 = get_node(a), get_node(b), get_node(c_val)
        # Negations:
        # !a is get_node(-a)
        nu1, nu2, nu3 = get_node(-a), get_node(-b), get_node(-c_val)
        
        adj[nu1].append(u2)
        adj[nu1].append(u3)
        
        adj[nu2].append(u1)
        adj[nu2].append(u3)
        
        adj[nu3].append(u1)
        adj[nu3].append(u2)
    
    # Kosaraju's algorithm to find SCCs
    visited = [False] * (num_nodes + 1)
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
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
    
    for i in range(1, num_nodes + 1):
        if not visited[i]:
            dfs1(i)
    
    visited = [False] * (num_nodes + 1)
    comp_id = [0] * (num_nodes + 1)
    current_comp = 0
    
    # Build reverse graph
    rev_adj = [[] for _ in range(num_nodes + 1)]
    for u in range(1, num_nodes + 1):
        for v in adj[u]:
            rev_adj[v].append(u)
    
    def dfs2(u, cid):
        stack = [u]
        visited[u] = True
        while stack:
            node = stack.pop()
            comp_id[node] = cid
            for neighbor in rev_adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
    
    for u in reversed(order):
        if not visited[u]:
            current_comp += 1
            dfs2(u, current_comp)
    
    # Check validity and assign values
    assignment = [-1] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        node_true = i
        node_false = n + i
        
        if comp_id[node_true] == comp_id[node_false]:
            possible = False
            break
        
        # Assign True if comp_id[True] > comp_id[False] (topological order)
        # Since we process in reverse order of finishing times, higher comp_id means earlier in topological sort
        # We want to assign the value that appears later in topological order (i.e., has smaller comp_id if we process in reverse)
        # Actually, in Kosaraju, the first SCC found (comp_id 1) is a sink in the condensation graph.
        # We want to set variable to False if comp_id[True] > comp_id[False]?
        # Let's trace: if comp_id[True] > comp_id[False], it means True was processed later in the first pass (or earlier in the second pass?).
        # In the second pass, we process nodes in reverse order of finishing times from first pass.
        # The first SCC we find (comp_id 1) is a sink.
        # If comp_id[True] > comp_id[False], then True is in a component that is "closer to source" than False.
        # We should pick the one closer to sink (smaller comp_id) to be True?
        # Standard approach: if comp_id[True] < comp_id[False], set to True.
        # Wait, let's stick to the standard: if comp_id[True] > comp_id[False], set to True.
        # Because in the second pass, we assign components in reverse topological order.
        # The first component found (id 1) is a sink.
        # If comp_id[True] > comp_id[False], True is in a component that is "more source-like".
        # We want to set the variable to the value that is consistent with the topological order.
        # If True implies False (contradiction), we would have detected it.
        # Otherwise, if comp_id[True] > comp_id[False], it means True is processed before False in the second pass? No.
        # Let's use the standard rule: if comp_id[True] > comp_id[False], assignment[i] = True.
        
        if comp_id[node_true] > comp_id[node_false]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    if not possible:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, assignment[1:])))

solve()