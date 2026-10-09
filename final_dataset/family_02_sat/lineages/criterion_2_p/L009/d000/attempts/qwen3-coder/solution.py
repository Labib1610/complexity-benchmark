import sys
sys.setrecursionlimit(1000000)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build implication graph
    # Each variable x_i is represented by node 2*i and node 2*i+1
    # x_i -> node 2*i represents x_i is False
    # x_i -> node 2*i+1 represents x_i is True
    
    adj = [[] for _ in range(2 * (n + 1))]
    rev_adj = [[] for _ in range(2 * (n + 1))]
    
    index = 2
    clauses = []
    for i in range(m):
        l1 = int(data[index])
        l2 = int(data[index + 1])
        index += 2
        clauses.append((l1, l2))
        
        # clause: (x_l1 OR x_l2) 
        # This is equivalent to (~x_l1 -> x_l2) AND (~x_l2 -> x_l1)
        # l1 is positive means x_l1, negative means ~x_|l1|
        # So ~x_l1 corresponds to not(l1>0) XOR (l1>0 ? 2*|l1| : 2*|l1|-1) = 2*|l1| if l1>0 else 2*|l1|+1
        # But easier way: for literal l, the node is: 2*|l| if l<0 else 2*|l|+1
        # And negation of that node is: 2*|l|+1 if l<0 else 2*|l|
        
        if l1 > 0:
            node_not_l1 = 2 * l1      # x_l1 is false
            node_l1 = 2 * l1 + 1      # x_l1 is true
        else:
            node_not_l1 = 2 * (-l1) + 1  # ~x_|l1| is true (so x_|l1| is false)
            node_l1 = 2 * (-l1)          # x_|l1| is true
        
        if l2 > 0:
            node_not_l2 = 2 * l2      # x_l2 is false
            node_l2 = 2 * l2 + 1      # x_l2 is true
        else:
            node_not_l2 = 2 * (-l2) + 1  # ~x_|l2| is true
            node_l2 = 2 * (-l2)          # x_|l2| is true
            
        # Add implications: not_l1 -> l2, not_l2 -> l1
        adj[node_not_l1].append(node_l2)
        adj[node_not_l2].append(node_l1)
        
        # Reverse graph for Kosaraju
        rev_adj[node_l2].append(node_not_l1)
        rev_adj[node_l1].append(node_not_l2)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * (n + 1))
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for u in range(2, 2 * (n + 1)):
        if not visited[u]:
            dfs1(u)
    
    # Second DFS on transpose graph
    visited = [False] * (2 * (n + 1))
    components = [-1] * (2 * (n + 1))
    component_id = 0
    
    def dfs2(u):
        visited[u] = True
        components[u] = component_id
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            component_id += 1
    
    # Check for satisfiability
    for i in range(1, n + 1):
        node_false = 2 * i
        node_true = 2 * i + 1
        if components[node_false] == components[node_true]:
            print("NO")
            return
    
    # Extract solution
    assignment = [0] * (n + 1)
    for i in range(1, n + 1):
        node_false = 2 * i
        node_true = 2 * i + 1
        if components[node_false] > components[node_true]:
            assignment[i] = 0
        else:
            assignment[i] = 1
    
    print("YES")
    print(' '.join(map(str, assignment[1:])))

if __name__ == "__main__":
    main()