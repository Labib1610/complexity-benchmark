import sys
sys.setrecursionlimit(1000000)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # For each variable x_i, we create two nodes:
    # Node 2*i represents x_i (Heavy-Lift)
    # Node 2*i + 1 represents NOT x_i (Long-Range)
    # But we'll use 2*i for x_i = 1, 2*i+1 for x_i = 0
    
    # In 2-SAT, each clause (a OR b) is converted to (~a -> b) and (~b -> a)
    # We'll build implication graph
    
    adj = [[] for _ in range(2 * n)]
    adj_rev = [[] for _ in range(2 * n)]
    
    index = 2
    for i in range(m):
        l1 = int(data[index])
        l2 = int(data[index+1])
        index += 2
        
        # Convert to 0-based indexing and determine which node represents the literal
        # For variable i (1-based), node 2*(i-1) is x_i=1, node 2*(i-1)+1 is x_i=0
        
        # l1 can be positive (x_i=1) or negative (-i means x_i=0)
        if l1 > 0:
            node1 = 2 * (l1 - 1)      # x_{l1} = 1
            not_node1 = 2 * (l1 - 1) + 1  # x_{l1} = 0
        else:
            node1 = 2 * (-l1 - 1) + 1   # x_{-l1} = 0
            not_node1 = 2 * (-l1 - 1)   # x_{-l1} = 1
            
        if l2 > 0:
            node2 = 2 * (l2 - 1)      # x_{l2} = 1
            not_node2 = 2 * (l2 - 1) + 1  # x_{l2} = 0
        else:
            node2 = 2 * (-l2 - 1) + 1   # x_{-l2} = 0
            not_node2 = 2 * (-l2 - 1)   # x_{-l2} = 1
            
        # Clause (node1 OR node2) is equivalent to (~node1 -> node2) AND (~node2 -> node1)
        adj[not_node1].append(node2)
        adj[not_node2].append(node1)
        
        adj_rev[node2].append(not_node1)
        adj_rev[node1].append(not_node2)
    
    # Kosaraju's algorithm for finding SCCs
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
    
    # Reverse the graph and find SCCs
    visited = [False] * (2 * n)
    scc_id = [-1] * (2 * n)
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
            
    # Check if for each variable, x_i and ~x_i are in different SCCs
    for i in range(n):
        if scc_id[2*i] == scc_id[2*i + 1]:
            print("NO")
            return
    
    # Assign values based on topological order of SCCs
    # Variables in later SCCs (higher id) should be assigned False first
    result = [-1] * n
    for i in range(n):
        if scc_id[2*i] > scc_id[2*i + 1]:
            result[i] = 1  # Heavy-Lift
        else:
            result[i] = 0  # Long-Range
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()