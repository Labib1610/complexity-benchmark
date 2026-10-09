import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # For each dependency, we have two literals
    # A literal is satisfied if:
    #   positive x: x is 1
    #   negative x: |x| is 0
    
    # This is a 2-SAT problem
    # We'll use implication graph and SCC
    
    # Variables: 0 to n-1 (qubits)
    # For variable x:
    #   x*2 represents x=0 (NOT x)
    #   x*2+1 represents x=1 (x)
    
    def var_to_node(x):
        # x is a literal (positive or negative)
        # returns (node, is_true)
        if x > 0:
            return (x - 1) * 2 + 1, True  # x=1
        else:
            return (-x - 1) * 2, True     # x=0
    
    # Build implication graph
    # For clause (a OR b), we add edges (!a -> b) and (!b -> a)
    
    adj = [[] for _ in range(2 * n)]
    rev_adj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # Clause: l1 OR l2
        # This means: (!l1 -> l2) AND (!l2 -> l1)
        
        # Convert literals to nodes
        node1, is_true1 = var_to_node(l1)
        node2, is_true2 = var_to_node(l2)
        
        # !node1 -> node2
        not_node1 = node1 ^ 1
        adj[not_node1].append(node2)
        rev_adj[node2].append(not_node1)
        
        # !node2 -> node1
        not_node2 = node2 ^ 1
        adj[not_node2].append(node1)
        rev_adj[node1].append(not_node2)
    
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
    
    # Second DFS on reverse graph
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
    
    # Check if satisfiable
    for i in range(n):
        node_false = i * 2      # x=0
        node_true = i * 2 + 1   # x=1
        if scc_id[node_false] == scc_id[node_true]:
            print("NO")
            return
    
    # Construct solution
    # In the implication graph, if SCC of !x appears later in topological order than SCC of x,
    # then x should be true.
    
    result = [0] * n
    for i in range(n):
        node_false = i * 2
        node_true = i * 2 + 1
        if scc_id[node_false] > scc_id[node_true]:
            result[i] = 1
        else:
            result[i] = 0
    
    print("YES")
    print(" ".join(map(str, result)))

threading.Thread(target=main).start()