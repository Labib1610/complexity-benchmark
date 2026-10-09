import sys
sys.setrecursionlimit(10**6)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # 2-SAT problem
    # Variables: x1, x2, ..., xn where xi = 1 means assign service i to Route 1
    # For each rule (l1, l2):
    # If l1 = +i, it means xi must be true
    # If l1 = -i, it means xi must be false
    # The rule is satisfied if at least one of l1 or l2 is satisfied
    # This translates to the clause (l1 OR l2)
    
    # We'll build implication graph and use SCC to solve 2-SAT
    
    # Number of variables
    num_vars = n
    # Total nodes in implication graph: 2 * num_vars
    # Node 0 to n-1 represent x1 to xn
    # Node n to 2n-1 represent not x1 to not xn
    # So node i represents variable i+1, and node i+n represents not(variable i+1)
    
    adj = [[] for _ in range(2 * n)]
    rev_adj = [[] for _ in range(2 * n)]
    
    index = lambda x: x - 1 if x > 0 else (-x - 1 + n)
    
    # For clause (a OR b), we add edges (not a -> b) and (not b -> a)
    for i in range(m):
        offset = 2 + 2 * i
        l1 = int(data[offset])
        l2 = int(data[offset + 1])
        
        # Convert to 0-based indexing in implication graph
        # l1 corresponds to node index(l1)
        # not l1 corresponds to index(-l1)
        # Similarly for l2
        
        # Clause (l1 OR l2) is equivalent to (not l1 -> l2) and (not l2 -> l1)
        adj[index(-l1)].append(index(l2))
        adj[index(-l2)].append(index(l1))
        rev_adj[index(l2)].append(index(-l1))
        rev_adj[index(l1)].append(index(-l2))
    
    # Kosaraju's algorithm for SCC
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
    
    visited = [False] * (2 * n)
    scc_id = [-1] * (2 * n)
    scc_count = 0
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = scc_count
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            scc_count += 1
    
    # Check if for every variable x, x and not x are in different SCCs
    for i in range(n):
        if scc_id[i] == scc_id[i + n]:
            print("NO")
            return
    
    # Assign values based on topological order of SCCs
    # Variables in later SCCs (higher scc_id) should be assigned False
    assignment = [False] * n
    for i in range(n):
        if scc_id[i] > scc_id[i + n]:
            assignment[i] = True  # x_i = True (Route 1)
        else:
            assignment[i] = False # x_i = False (Route 0)
    
    print("YES")
    print(' '.join(str(int(b)) for b in assignment))

if __name__ == "__main__":
    main()