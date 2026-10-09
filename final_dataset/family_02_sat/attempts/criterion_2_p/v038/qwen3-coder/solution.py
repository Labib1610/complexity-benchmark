import sys
sys.setrecursionlimit(1000000)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # Read clauses
    clauses = []
    index = 2
    for _ in range(m):
        c1 = int(data[index])
        c2 = int(data[index+1])
        clauses.append((c1, c2))
        index += 2
    
    # Create implication graph for 2-SAT
    # Variables: 1 to n (positive) and -1 to -n (negative)
    # We'll map variable x (1-based) to node 2*x and ~x to node 2*x+1
    # But it's easier to use: for variable x (1-based):
    # node for x: 2*(x-1)     (0, 2, 4, ...)
    # node for ~x: 2*(x-1)+1   (1, 3, 5, ...)
    
    adj = [[] for _ in range(2 * n)]
    adj_rev = [[] for _ in range(2 * n)]
    
    # For clause (a OR b), we add edges (~a -> b) and (~b -> a)
    for c1, c2 in clauses:
        # Convert to 0-based indexing for variables
        var1 = abs(c1) - 1
        var2 = abs(c2) - 1
        
        # Determine the nodes
        # For variable x:
        # if c > 0: node is 2*x (meaning x is true)
        # if c < 0: node is 2*x+1 (meaning x is false)
        if c1 > 0:
            node_not_var1 = 2 * var1 + 1  # ~x is false, so x should be true
            node_var1 = 2 * var1          # x is true
        else:
            node_not_var1 = 2 * var1      # ~x is true (x is false), so x should be false
            node_var1 = 2 * var1 + 1      # x is false
            
        if c2 > 0:
            node_not_var2 = 2 * var2 + 1  # ~y is false, so y should be true
            node_var2 = 2 * var2          # y is true
        else:
            node_not_var2 = 2 * var2      # ~y is true (y is false), so y should be false
            node_var2 = 2 * var2 + 1      # y is false
            
        # Add implications: (~var1 -> var2) and (~var2 -> var1)
        adj[node_not_var1].append(node_var2)
        adj[node_not_var2].append(node_var1)
        
        # Reverse graph
        adj_rev[node_var2].append(node_not_var1)
        adj_rev[node_var1].append(node_not_var2)
    
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
    
    # Second DFS on transpose graph
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
    
    # Check if satisfiable
    for i in range(n):
        node_x = 2 * i       # x is true
        node_not_x = 2 * i + 1  # x is false
        if scc_id[node_x] == scc_id[node_not_x]:
            print("NO")
            return
    
    # Build solution
    # In the implication graph, if SCC id of x is greater than SCC id of ~x,
    # then x should be true. Otherwise false.
    assignment = [0] * n
    for i in range(n):
        node_x = 2 * i
        node_not_x = 2 * i + 1
        if scc_id[node_x] > scc_id[node_not_x]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    main()