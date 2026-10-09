import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # For each variable x_i, we create two nodes: 2*i (for x_i = True) and 2*i+1 (for x_i = False)
    # But in this problem, x_i corresponds to service i being upgraded (1) or legacy (0)
    # So x_i = True means upgraded, x_i = False means legacy
    # For literals:
    #  positive literal k means x_k = True (upgraded)
    #  negative literal -k means x_k = False (legacy)
    
    # We will build a graph for 2-SAT
    # Each variable x_i has two nodes: 2*i (True) and 2*i+1 (False)
    adj = [[] for _ in range(2 * (n + 1))]
    adj_rev = [[] for _ in range(2 * (n + 1))]
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        # Convert to 0-based indexing for internal use
        # a and b are literals
        # We need (x_a or x_b) to be true
        # This is equivalent to (not x_a => x_b) and (not x_b => x_a)
        
        # Convert literals to node indices
        # For literal k: node is 2*|k| if k>0 (meaning x_{|k|} = True), else 2*|k|+1 (meaning x_{|k|} = False)
        # not x_k = True is x_k = False, so not (2*k) is 2*k+1
        # not x_k = False is x_k = True, so not (2*k+1) is 2*k
        
        def lit_to_node(lit):
            if lit > 0:
                return 2 * lit  # x_k = True
            else:
                return 2 * (-lit) + 1  # x_{-lit} = False
        
        node_a = lit_to_node(a)
        node_b = lit_to_node(b)
        
        # not a => b
        adj[node_a ^ 1].append(node_b)
        adj_rev[node_b].append(node_a ^ 1)
        
        # not b => a
        adj[node_b ^ 1].append(node_a)
        adj_rev[node_a].append(node_b ^ 1)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * (n + 1))
    order = []
    
    def dfs1(v):
        visited[v] = True
        for u in adj[v]:
            if not visited[u]:
                dfs1(u)
        order.append(v)
    
    for i in range(2, 2 * (n + 1)):
        if not visited[i]:
            dfs1(i)
    
    # Second DFS on transpose graph
    visited = [False] * (2 * (n + 1))
    components = [-1] * (2 * (n + 1))
    comp_id = 0
    
    def dfs2(v):
        visited[v] = True
        components[v] = comp_id
        for u in adj_rev[v]:
            if not visited[u]:
                dfs2(u)
    
    while order:
        v = order.pop()
        if not visited[v]:
            dfs2(v)
            comp_id += 1
    
    # Check for contradiction: for each variable, True and False nodes must be in different components
    for i in range(1, n + 1):
        if components[2 * i] == components[2 * i + 1]:
            print("NO")
            return
    
    # Assign values: if component of True node > component of False node, set to True
    assignment = [0] * (n + 1)
    for i in range(1, n + 1):
        if components[2 * i] > components[2 * i + 1]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(' '.join(map(str, assignment[1:])))

threading.Thread(target=main).start()