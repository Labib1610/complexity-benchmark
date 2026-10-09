import sys
sys.setrecursionlimit(1000000)

def solve():
    n, m = map(int, input().split())
    
    # Build implication graph
    # Each variable x has two nodes: x (true) and x+n (false)
    adj = [[] for _ in range(2 * n + 1)]
    rev_adj = [[] for _ in range(2 * n + 1)]
    
    # For each clause (a OR b), we add edges (!a -> b) and (!b -> a)
    for _ in range(m):
        l1, l2 = map(int, input().split())
        
        # Convert to 0-indexed variables
        # Positive means variable is true, negative means false
        if l1 > 0:
            a_var = l1  # x_i is true
            a_node = a_var + n  # !x_i (false node)
        else:
            a_var = -l1
            a_node = a_var  # x_i (true node)
            
        if l2 > 0:
            b_var = l2  # x_j is true
            b_node = b_var + n  # !x_j (false node)
        else:
            b_var = -l2
            b_node = b_var  # x_j (true node)
        
        # Add implications: !a -> b and !b -> a
        adj[a_node].append(b_var if l2 > 0 else b_var + n)
        adj[b_node].append(a_var if l1 > 0 else a_var + n)
        
        rev_adj[b_var if l2 > 0 else b_var + n].append(a_node)
        rev_adj[a_var if l1 > 0 else a_var + n].append(b_node)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * n + 1)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    # First DFS
    for i in range(1, 2 * n + 1):
        if not visited[i]:
            dfs1(i)
    
    # Second DFS on transpose graph
    visited = [False] * (2 * n + 1)
    scc_id = [0] * (2 * n + 1)
    scc_count = 0
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = scc_count
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    # Process in reverse order
    for u in reversed(order):
        if not visited[u]:
            scc_count += 1
            dfs2(u)
    
    # Check if satisfiable
    for i in range(1, n + 1):
        if scc_id[i] == scc_id[i + n]:
            print("NO")
            return
    
    # Build solution
    print("YES")
    result = [0] * (n + 1)
    
    # Assign values based on SCC completion order
    # Variables in later finishing SCCs are assigned first
    scc_order = [(scc_id[i], i) for i in range(1, 2 * n + 1)]
    scc_order.sort(reverse=True)
    
    assigned = [False] * (n + 1)
    
    for _, node in scc_order:
        var = node if node <= n else node - n
        if not assigned[var]:
            if node <= n:  # This is x_i node (true)
                result[var] = 1
            else:  # This is !x_i node (false)
                result[var] = 0
            assigned[var] = True
    
    print(' '.join(map(str, result[1:])))

solve()