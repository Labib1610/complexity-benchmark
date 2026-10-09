import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # For each variable x_i, we create two nodes:
    # Node 2*i represents x_i (valve i open)
    # Node 2*i + 1 represents NOT x_i (valve i closed)
    
    # We'll build implication graph for 2-SAT
    # For clause (a OR b), we add edges: NOT a -> b and NOT b -> a
    
    adj = [[] for _ in range(2 * (n + 1))]  # 0 unused, 1..n for vars
    rev_adj = [[] for _ in range(2 * (n + 1))]
    
    def var(i):
        return 2 * i
    
    def not_var(i):
        return 2 * i + 1
    
    def add_implication(a, b):
        adj[a].append(b)
        rev_adj[b].append(a)
    
    def add_clause(a, b):  # a OR b
        # NOT a -> b
        # NOT b -> a
        add_implication(a ^ 1, b)
        add_implication(b ^ 1, a)
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # Convert literals to node indices
        # Positive literal i means "valve i open" => node 2*i
        # Negative literal -i means "valve i closed" => node 2*i + 1 
        node1 = var(abs(l1)) if l1 > 0 else not_var(abs(l1))
        node2 = var(abs(l2)) if l2 > 0 else not_var(abs(l2))
        add_clause(node1, node2)
    
    # Kosaraju's algorithm for finding SCCs
    order = []
    visited = [False] * (2 * (n + 1))
    
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
    for i in range(2, 2 * (n + 1)):
        if not visited[i]:
            dfs1(i)
    
    # Second DFS pass on reversed graph in reverse finish order
    visited = [False] * (2 * (n + 1))
    components = {}
    comp_id = 0
    
    while order:
        u = order.pop()
        if not visited[u]:
            component = []
            dfs2(u, component)
            for node in component:
                components[node] = comp_id
            comp_id += 1
    
    # Check if satisfiable: for each variable, x and NOT x must be in different SCCs
    assignment = [-1] * (n + 1)
    for i in range(1, n + 1):
        x_node = var(i)
        nx_node = not_var(i)
        if components[x_node] == components[nx_node]:
            print("NO")
            return
        
        # In Kosaraju, if NOT x has higher topological order than x,
        # then x should be TRUE
        if components[x_node] > components[nx_node]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    result = []
    for i in range(1, n + 1):
        result.append(str(assignment[i]))
    print(' '.join(result))

threading.Thread(target=main).start()