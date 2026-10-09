import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build implication graph
    # Variables: 1..n (positive), -(1..n) negative
    # We'll use 0-based indexing for graph: var -> 2*(|var|-1) + (0 if positive else 1)
    # And reverse mapping: node -> (index+1) * (-1)**(node%2)
    
    adj = [[] for _ in range(2 * n)]
    rev_adj = [[] for _ in range(2 * n)]
    
    def var_to_node(v):
        if v > 0:
            return 2 * (v - 1)
        else:
            return 2 * (-v - 1) + 1
    
    def node_to_var(node):
        idx = node // 2
        sign = node % 2
        return (idx + 1) if sign == 0 else -(idx + 1)
    
    # For each clause (a or b), we add edges (!a -> b) and (!b -> a)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        # Add edge !a -> b
        not_a = var_to_node(-a if a > 0 else -a)
        b_node = var_to_node(b)
        adj[not_a].append(b_node)
        rev_adj[b_node].append(not_a)
        
        # Add edge !b -> a
        not_b = var_to_node(-b if b > 0 else -b)
        a_node = var_to_node(a)
        adj[not_b].append(a_node)
        rev_adj[a_node].append(not_b)
    
    # Kosaraju's algorithm to find SCCs
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
    components = [-1] * (2 * n)
    component_count = 0
    
    def dfs2(u, comp_id):
        visited[u] = True
        components[u] = comp_id
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v, comp_id)
    
    for u in reversed(order):
        if not visited[u]:
            dfs2(u, component_count)
            component_count += 1
    
    # Check if satisfiable: no variable and its negation should be in the same SCC
    for i in range(n):
        pos = var_to_node(i + 1)
        neg = var_to_node(-(i + 1))
        if components[pos] == components[neg]:
            print("NO")
            return
    
    # Assign values based on topological order of SCCs
    assignment = [-1] * n
    # Create component graph topological order
    comp_order = sorted(range(2 * n), key=lambda x: components[x])
    
    for u in comp_order:
        var_idx = u // 2
        if assignment[var_idx] == -1:  # Not assigned yet
            if u % 2 == 0:  # Positive literal
                assignment[var_idx] = 1
            else:  # Negative literal
                assignment[var_idx] = 0
    
    print("YES")
    print(' '.join(str(x) for x in assignment))

threading.Thread(target=main).start()