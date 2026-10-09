import sys
sys.setrecursionlimit(1000000)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # For each rule: (a, b) means at least one of a or b must be true
    # a and b are literals: positive for True variable, negative for False variable
    rules = []
    index = 2
    for _ in range(m):
        l1 = int(data[index])
        l2 = int(data[index+1])
        rules.append((l1, l2))
        index += 2
    
    # We'll solve this using 2-SAT
    # Variables are 1-indexed from 1 to n
    # For each variable x_i:
    # Node 2*i represents x_i (True)
    # Node 2*i + 1 represents not x_i (False)
    
    # But in graph algorithms it's easier to work with 0-based indexing
    # So:
    # Node 2*(i-1) represents x_i (True) 
    # Node 2*(i-1)+1 represents not x_i (False)
    
    def var_to_node(v):
        # v is a literal like 3 or -3
        # returns the node index in implication graph
        var_index = abs(v)  # 1-based
        node_base = 2 * (var_index - 1)  # 0-based base node for this variable
        if v > 0:
            return node_base      # True node
        else:
            return node_base + 1  # False node
            
    def node_to_var(node):
        # Given a node, return the literal it represents
        var_index = (node // 2) + 1  # back to 1-based
        if node % 2 == 0:
            return var_index    # True literal
        else:
            return -var_index   # False literal
            
    # Build implication graph
    # For clause (a OR b), we add edges (not a -> b) and (not b -> a)
    # Total nodes: 2*n
    adj = [[] for _ in range(2 * n)]
    rev_adj = [[] for _ in range(2 * n)]
    
    for l1, l2 in rules:
        # Add implications: not l1 -> l2  and  not l2 -> l1
        node_not_l1 = var_to_node(-l1)
        node_l2 = var_to_node(l2)
        adj[node_not_l1].append(node_l2)
        rev_adj[node_l2].append(node_not_l1)
        
        node_not_l2 = var_to_node(-l2)
        node_l1 = var_to_node(l1)
        adj[node_not_l2].append(node_l1)
        rev_adj[node_l1].append(node_not_l2)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
        
    def dfs2(u, component):
        visited[u] = True
        component.append(u)
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v, component)
                
    # First DFS pass
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
            
    # Second DFS pass on reverse graph
    visited = [False] * (2 * n)
    components = []
    while order:
        u = order.pop()
        if not visited[u]:
            component = []
            dfs2(u, component)
            components.append(component)
            
    # Assign component numbers
    comp_id = [-1] * (2 * n)
    for idx, comp in enumerate(components):
        for node in comp:
            comp_id[node] = idx
            
    # Check for contradictions
    for i in range(n):
        true_node = 2 * i
        false_node = 2 * i + 1
        if comp_id[true_node] == comp_id[false_node]:
            print("NO")
            return
            
    # If no contradiction, build solution
    print("YES")
    
    # Topologically sort components
    # Component graph is a DAG, and components are in reverse topological order already
    # (because of how Kosaraju works)
    assignment = [-1] * n
    
    # Process components in reverse order (topological order of condensation)
    for comp in reversed(components):
        for node in comp:
            var_index_0based = node // 2  # 0-based
            if assignment[var_index_0based] == -1:
                # This variable hasn't been assigned yet
                # If it's a true node, set variable to 1
                # If it's a false node, set variable to 0
                if node % 2 == 0:
                    assignment[var_index_0based] = 1
                else:
                    assignment[var_index_0based] = 0
                    
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    main()