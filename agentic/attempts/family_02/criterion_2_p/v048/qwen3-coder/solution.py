import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # For each variable x (1 to n), we have two nodes: x (positive) and -x (negative)
    # We'll use 2*x for positive literal x, and 2*x + 1 for negative literal -x
    # But actually, let's use a more standard 2-SAT approach:
    # Variables are 0 to 2*n-1
    # For variable i (1-based), node 2*(i-1) is x_i = 0, node 2*(i-1)+1 is x_i = 1
    
    adj = [[] for _ in range(2 * n)]
    adj_rev = [[] for _ in range(2 * n)]
    
    # Helper to convert literal to node index
    def lit_to_node(lit):
        var = abs(lit) - 1  # 0-based variable index
        if lit > 0:
            return 2 * var + 1  # x_i = 1
        else:
            return 2 * var      # x_i = 0
    
    # For each clause (l1 OR l2), we add edges (~l1 -> l2) and (~l2 -> l1)
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # Add implication edges
        # ~l1 -> l2
        adj[lit_to_node(-l1)].append(lit_to_node(l2))
        adj_rev[lit_to_node(l2)].append(lit_to_node(-l1))
        # ~l2 -> l1
        adj[lit_to_node(-l2)].append(lit_to_node(l1))
        adj_rev[lit_to_node(l1)].append(lit_to_node(-l2))
    
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
    
    for i in reversed(order):
        if not visited[i]:
            dfs2(i)
            scc_count += 1
    
    # Check if satisfiable
    assignment = [-1] * n
    for i in range(n):
        # Variable i corresponds to nodes 2*i and 2*i+1
        if scc_id[2*i] == scc_id[2*i + 1]:
            print("NO")
            return
        # In the implication graph, if there's a path from ~x to x,
        # then x must be true. If there's a path from x to ~x, then x must be false.
        # The SCC id gives the topological order of SCCs in the condensation.
        # Higher SCC id means later in topological order.
        if scc_id[2*i] > scc_id[2*i + 1]:
            assignment[i] = 1  # x_i = 1
        else:
            assignment[i] = 0  # x_i = 0
    
    print("YES")
    print(' '.join(map(str, assignment)))

threading.Thread(target=main).start()