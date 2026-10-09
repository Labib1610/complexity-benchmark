import sys
sys.setrecursionlimit(1000000)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # For each variable x_i, we create two nodes:
    # Node 2*i represents x_i (positive literal)
    # Node 2*i + 1 represents ~x_i (negative literal)
    # We'll build implication graph and check for SCCs
    
    adj = [[] for _ in range(2 * (n + 1))]
    adj_rev = [[] for _ in range(2 * (n + 1))]
    
    index = 2
    for i in range(m):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2
        
        # Convert to 0-based indexing for variables
        # Also handle signs: positive means x_i, negative means ~x_i
        if a > 0:
            node_a = 2 * a + 1  # ~x_a -> ...
            var_a = a
            sign_a = 0  # x_a true
        else:
            node_a = 2 * (-a)  # x_a -> ...
            var_a = -a
            sign_a = 1  # x_a false
            
        if b > 0:
            node_b = 2 * b + 1  # ~x_b -> ...
            var_b = b
            sign_b = 0
        else:
            node_b = 2 * (-b)  # x_b -> ...
            var_b = -b
            sign_b = 1
            
        # The clause (a OR b) is equivalent to (~a -> b) AND (~b -> a)
        # In our notation:
        # node_a (which is ~var_a) implies node_b_bar (which is var_b)
        # node_b (which is ~var_b) implies node_a_bar (which is var_a)
        
        node_a_bar = node_a ^ 1  # flip last bit to get complement
        node_b_bar = node_b ^ 1
        
        adj[node_a].append(node_b_bar)
        adj[node_b].append(node_a_bar)
        adj_rev[node_b_bar].append(node_a)
        adj_rev[node_a_bar].append(node_b)
        
    # Now do Kosaraju's algorithm to find strongly connected components
    visited = [False] * (2 * (n + 1))
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
        
    for i in range(2, 2 * (n + 1)):
        if not visited[i]:
            dfs1(i)
            
    # Second DFS on transpose graph
    visited = [False] * (2 * (n + 1))
    component = [-1] * (2 * (n + 1))
    comp_num = 0
    
    def dfs2(u):
        visited[u] = True
        component[u] = comp_num
        for v in adj_rev[u]:
            if not visited[v]:
                dfs2(v)
                
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            comp_num += 1
            
    # Check for contradictions: variable and its negation in same SCC
    for i in range(1, n + 1):
        pos_node = 2 * i
        neg_node = 2 * i + 1
        if component[pos_node] == component[neg_node]:
            print("NO")
            return
            
    # If no contradiction, construct a solution
    # Assign values based on topological order of SCCs
    # Nodes in later SCCs should be assigned TRUE
    assignment = [0] * (n + 1)
    
    # Create component graph and sort by reverse topological order
    comp_order = list(range(comp_num))
    # Actually, since we want to assign values, we can just use the fact that 
    # if comp of x_i is < comp of ~x_i, then x_i should be FALSE
    # if comp of x_i is > comp of ~x_i, then x_i should be TRUE
    
    for i in range(1, n + 1):
        pos_node = 2 * i
        neg_node = 2 * i + 1
        if component[pos_node] > component[neg_node]:
            assignment[i] = 1
        else:
            assignment[i] = 0
            
    print("YES")
    print(' '.join(map(str, assignment[1:])))

if __name__ == "__main__":
    main()