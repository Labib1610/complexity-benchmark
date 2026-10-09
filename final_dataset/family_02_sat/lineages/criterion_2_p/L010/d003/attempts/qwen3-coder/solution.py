import sys
from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # For each variable x_i, we'll have two nodes: 2*i (x_i = False) and 2*i+1 (x_i = True)
    # For literals:
    #  l > 0 means x_l = True
    #  l < 0 means x_{-l} = False
    
    # We build implication graph for 2-SAT
    # Each constraint (a OR b) translates to (~a -> b) and (~b -> a)
    # In our case, each constraint says NOT(l1_target AND l2_target), which is (~l1_target OR ~l2_target)
    
    adj = defaultdict(list)
    radj = defaultdict(list)
    
    def lit_to_node(lit):
        var = abs(lit)
        # node for x_var = False is 2*var
        # node for x_var = True is 2*var + 1
        if lit > 0:
            return 2 * var + 1  # want x_var = True
        else:
            return 2 * var      # want x_{-lit} = False, so x_var = False
            
    def neg_lit_node(node):
        # given node for x_i = True (2*i+1) returns node for x_i = False (2*i)
        # given node for x_i = False (2*i) returns node for x_i = True (2*i+1)
        if node % 2 == 1:
            return node - 1
        else:
            return node + 1
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # Constraint: not both l1 and l2 can be in their target states
        # That is: not(l1_target AND l2_target)
        # Which is equivalent to: (not l1_target OR not l2_target)
        
        # So we add implications:
        # l1_target -> not l2_target
        # l2_target -> not l1_target
        
        node1 = lit_to_node(l1)
        node2 = lit_to_node(l2)
        
        # Add implication: l1_target -> not l2_target
        adj[neg_lit_node(node1)].append(neg_lit_node(node2))
        radj[neg_lit_node(node2)].append(neg_lit_node(node1))
        
        # Add implication: l2_target -> not l1_target
        adj[neg_lit_node(node2)].append(neg_lit_node(node1))
        radj[neg_lit_node(node1)].append(neg_lit_node(node2))
    
    # Now run Kosaraju's algorithm to check if satisfiable
    order = []
    visited = [False] * (2 * (n + 1))
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    # First DFS on original graph
    for i in range(1, n+1):
        u_false = 2 * i
        u_true = 2 * i + 1
        if not visited[u_false]:
            dfs1(u_false)
        if not visited[u_true]:
            dfs1(u_true)
    
    # Transpose DFS
    comp = [-1] * (2 * (n + 1))
    def dfs2(u, c):
        comp[u] = c
        for v in radj[u]:
            if comp[v] == -1:
                dfs2(v, c)
                
    # Second DFS on transpose graph in reverse finish time order
    c = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, c)
            c += 1
            
    # Check if satisfiable
    for i in range(1, n+1):
        u_false = 2 * i
        u_true = 2 * i + 1
        if comp[u_false] == comp[u_true]:
            print("NO")
            return
            
    # Satisfiable, reconstruct solution
    assignment = [0] * (n+1)
    for i in range(1, n+1):
        u_false = 2 * i
        u_true = 2 * i + 1
        if comp[u_false] > comp[u_true]:
            assignment[i] = 0  # x_i = False
        else:
            assignment[i] = 1  # x_i = True
            
    print("YES")
    print(' '.join(str(x) for x in assignment[1:]))

if __name__ == "__main__":
    main()