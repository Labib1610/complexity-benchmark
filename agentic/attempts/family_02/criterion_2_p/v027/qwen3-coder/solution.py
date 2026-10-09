import sys
sys.setrecursionlimit(1000000)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # For each variable x_i, we create two nodes: 2*i (for x_i = 0) and 2*i+1 (for x_i = 1)
    # Clauses are of the form (a OR b), where a and b are literals (possibly negated variables)
    
    # We'll use 2-SAT approach
    # Variables: x_1, ..., x_n corresponding to filters 1,...,n being active (=1) or bypassed (=0)
    # Literal +i means x_i = 1 (node 2*i + 1)
    # Literal -i means x_i = 0 (node 2*i)
    
    adj = [[] for _ in range(2 * (n + 1))]
    adj_rev = [[] for _ in range(2 * (n + 1))]
    
    index = 2
    clauses = []
    for _ in range(m):
        l1 = int(data[index])
        l2 = int(data[index+1])
        index += 2
        clauses.append((l1, l2))
        
        # clause (l1 OR l2) is equivalent to (NOT l1 -> l2) AND (NOT l2 -> l1)
        # NOT l1 is represented as -l1
        # If l1 is +i, NOT l1 is node 2*i 
        # If l1 is -i, NOT l1 is node 2*i + 1
        # Similarly for l2
        
        # Convert literals to nodes
        if l1 > 0:
            node_not_l1 = 2 * l1      # x_{l1} = 0
            node_l2 = 2 * abs(l2) + (1 if l2 > 0 else 0)
        else:
            node_not_l1 = 2 * (-l1) + 1  # x_{-l1} = 1, so NOT(x_{-l1}=1) is x_{-l1}=0
            node_l2 = 2 * abs(l2) + (1 if l2 > 0 else 0)
            
        if l2 > 0:
            node_not_l2 = 2 * l2
            node_l1 = 2 * abs(l1) + (1 if l1 > 0 else 0)
        else:
            node_not_l2 = 2 * (-l2) + 1
            node_l1 = 2 * abs(l1) + (1 if l1 > 0 else 0)
            
        adj[node_not_l1].append(node_l2)
        adj[node_not_l2].append(node_l1)
        adj_rev[node_l2].append(node_not_l1)
        adj_rev[node_l1].append(node_not_l2)
    
    # Now run Kosaraju's algorithm to find strongly connected components
    visited = [False] * (2 * (n + 1))
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
        
    for i in range(2, 2*(n+1)):
        if not visited[i]:
            dfs1(i)
            
    # Second DFS on transpose graph
    visited = [False] * (2 * (n + 1))
    scc_id = [-1] * (2 * (n + 1))
    scc_count = 0
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = scc_count
        for v in adj_rev[u]:
            if not visited[v]:
                dfs2(v)
                
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            scc_count += 1
            
    # Check for contradictions: for each variable x_i, nodes 2*i and 2*i+1 should not be in same SCC
    for i in range(1, n+1):
        if scc_id[2*i] == scc_id[2*i + 1]:
            print("NO")
            return
            
    # Assign values based on topological order of SCCs
    # Variables in later SCCs (higher id) are assigned True first
    assignment = [-1] * (n + 1)
    
    # Create mapping from SCC id to list of nodes
    scc_nodes = [[] for _ in range(scc_count)]
    for i in range(2, 2*(n+1)):
        scc_nodes[scc_id[i]].append(i)
        
    # Process SCCs in reverse topological order (from last finished in first DFS)
    for comp in reversed(range(scc_count)):
        for node in scc_nodes[comp]:
            var_index = (node // 2)
            if var_index == 0:
                continue
            if assignment[var_index] == -1:
                # If node = 2*i, then x_i = 0
                # If node = 2*i+1, then x_i = 1
                assignment[var_index] = node % 2
                
    print("YES")
    result = []
    for i in range(1, n+1):
        result.append(str(assignment[i]))
    print(' '.join(result))

if __name__ == "__main__":
    main()