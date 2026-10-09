import sys
sys.setrecursionlimit(1000000)

def solve():
    n, m = map(int, input().split())
    
    # Build implication graph
    # Each variable x has two nodes: x (positive) and x+n (negative)
    # We'll use 1-based indexing, so variables are 1..n and n+1..2n
    adj = [[] for _ in range(2 * n + 1)]
    rev_adj = [[] for _ in range(2 * n + 1)]
    
    # For each rule (a or b), we add implications (!a => b) and (!b => a)
    for _ in range(m):
        l1, l2 = map(int, input().split())
        
        # Convert to node indices
        # If l1 > 0, it's variable l1 positive, node l1
        # If l1 < 0, it's variable |l1| negative, node |l1|+n
        if l1 > 0:
            node_a = l1
            not_a = l1 + n
        else:
            node_a = -l1 + n
            not_a = -l1
        
        if l2 > 0:
            node_b = l2
            not_b = l2 + n
        else:
            node_b = -l2 + n
            not_b = -l2
            
        # Add implications: !a => b and !b => a
        adj[not_a].append(node_b)
        adj[not_b].append(node_a)
        rev_adj[node_b].append(not_a)
        rev_adj[node_a].append(not_b)
    
    # Kosaraju's algorithm for finding SCCs
    visited = [False] * (2 * n + 1)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    # First DFS on original graph
    for i in range(1, 2 * n + 1):
        if not visited[i]:
            dfs1(i)
    
    # Second DFS on transpose graph
    visited = [False] * (2 * n + 1)
    scc_id = [0] * (2 * n + 1)
    scc_count = 0
    
    def dfs2(u, cid):
        visited[u] = True
        scc_id[u] = cid
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v, cid)
    
    # Process in reverse order
    while order:
        u = order.pop()
        if not visited[u]:
            scc_count += 1
            dfs2(u, scc_count)
    
    # Check if satisfiable
    for i in range(1, n + 1):
        if scc_id[i] == scc_id[i + n]:
            print("NO")
            return
    
    # Assign values based on topological order of SCCs
    assignment = [0] * (n + 1)
    # Create a mapping from SCC id to whether it's been assigned
    scc_value = {}
    
    # Process SCCs in reverse topological order
    # In Kosaraju, the order we found SCCs in dfs2 is reverse topological
    # But we stored them in order, so we process them in reverse
    
    # Actually, let's recompute the topological order properly
    scc_nodes = [[] for _ in range(scc_count + 1)]
    for i in range(1, 2 * n + 1):
        scc_nodes[scc_id[i]].append(i)
    
    # For each variable, if positive literal SCC comes later than negative,
    # then variable should be true
    for i in range(1, n + 1):
        pos_scc = scc_id[i]
        neg_scc = scc_id[i + n]
        if pos_scc != neg_scc:
            # Variable i is true if its positive node is in a "later" SCC
            # We can determine this by checking which comes first in order list
            # But we need to reconstruct the topological order
            pass
    
    # Simpler approach: process SCCs in topological order and assign values
    # A node gets value True if we haven't assigned its variable yet
    assigned = [False] * (n + 1)
    
    # Reconstruct topological order of SCCs
    scc_order = []
    scc_visited = [False] * (scc_count + 1)
    
    def get_scc_order(u_scc):
        scc_visited[u_scc] = True
        for i in range(1, 2 * n + 1):
            if scc_id[i] == u_scc:
                for v in adj[i]:
                    v_scc = scc_id[v]
                    if not scc_visited[v_scc]:
                        get_scc_order(v_scc)
        scc_order.append(u_scc)
    
    # Find source SCCs to start
    for cid in range(1, scc_count + 1):
        if not scc_visited[cid]:
            get_scc_order(cid)
    
    # Process in topological order (reverse of how we added)
    while scc_order:
        cid = scc_order.pop()
        for node in range(1, 2 * n + 1):
            if scc_id[node] == cid and not assigned[min(node, node if node <= n else node - n)]:
                if node <= n:  # Positive literal
                    assignment[node] = 1
                    assigned[node] = True
                else:  # Negative literal (node = var + n)
                    var = node - n
                    assignment[var] = 0
                    assigned[var] = True
    
    print("YES")
    print(' '.join(map(str, assignment[1:])))

solve()