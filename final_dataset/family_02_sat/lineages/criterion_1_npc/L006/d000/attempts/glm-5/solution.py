import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        
        # Get negated literals for implications
        def get_node(lit):
            if lit > 0:
                return (lit - 1) * 2 + 1  # Node for x_true
            else:
                return (-lit - 1) * 2      # Node for x_false
        
        def get_neg_node(lit):
            if lit > 0:
                return (lit - 1) * 2      # Node for x_false (negation of x_true)
            else:
                return (-lit - 1) * 2 + 1  # Node for x_true (negation of x_false)
        
        u1, u2, u3 = get_neg_node(l1), get_neg_node(l2), get_neg_node(l3)
        v1, v2, v3 = get_node(l2), get_node(l3), get_node(l1)
        
        # Clause (l1 or l2 or l3) splits to:
        # (!l1 -> l2 or l3), (!l2 -> l1 or l3), (!l3 -> l1 or l2)
        # Encoding OR in 2-SAT: a -> (b or c) translates to (a -> b) and (a -> c) ? No.
        # It's handled by one variable being the "pivot":
        # (!l1 -> !l2 -> l3) and (!l1 -> !l3 -> l2)
        
        # Path 1: neg(l1) -> neg(l2) -> l3
        adj[u1].append(u2)
        adj[u2].append(v3)
        
        # Path 2: neg(l1) -> neg(l3) -> l2
        adj[u1].append(u3)
        adj[u3].append(v2)
        
        # Path 3: neg(l2) -> neg(l1) -> l3
        adj[u2].append(u1)
        adj[u1].append(v3)
        
        # Path 4: neg(l2) -> neg(l3) -> l1
        adj[u2].append(u3)
        adj[u3].append(v1)
        
        # Path 5: neg(l3) -> neg(l1) -> l2
        adj[u3].append(u1)
        adj[u1].append(v2)
        
        # Path 6: neg(l3) -> neg(l2) -> l1
        adj[u3].append(u2)
        adj[u2].append(v1)
    
    # Kosaraju's algorithm to find SCCs
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(u):
        stack = [(u, False)]
        while stack:
            node, processed = stack.pop()
            if processed:
                order.append(node)
                continue
            if visited[node]:
                continue
            visited[node] = True
            stack.append((node, True))
            for v in adj[node]:
                if not visited[v]:
                    stack.append((v, False))
    
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    
    visited = [False] * (2 * n)
    comp_id = [-1] * (2 * n)
    current_comp = 0
    
    # Build reverse graph
    radj = [[] for _ in range(2 * n)]
    for u in range(2 * n):
        for v in adj[u]:
            radj[v].append(u)
    
    def dfs2(u, cid):
        stack = [u]
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            comp_id[node] = cid
            for v in radj[node]:
                if not visited[v]:
                    stack.append(v)
    
    for u in reversed(order):
        if not visited[u]:
            dfs2(u, current_comp)
            current_comp += 1
    
    # Check for unsatisfiability and construct assignment
    assignment = [0] * n
    for i in range(n):
        node_true = 2 * i
        node_false = 2 * i + 1
        if comp_id[node_true] == comp_id[node_false]:
            # Use sys.stdout.write for consistency, though print is also fine
            # We must write exactly as specified.
            # Since we are inside solve, we can accumulate output or write directly.
            # Let's write directly for simplicity, adhering to "write only the required answer".
            sys.stdout.write("NO\n")
            return
        if comp_id[node_true] > comp_id[node_false]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, assignment)) + "\n")

if __name__ == '__main__':
    solve()