import sys
from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # For each switch, we'll have two variables: x_i (switch i is ON) and not x_i (switch i is OFF)
    # We'll use 2*i for x_i (ON) and 2*i+1 for not x_i (OFF)
    # But since variables can be positive or negative, we'll map:
    # variable i (1-based) -> node 2*i (ON), node 2*i+1 (OFF)
    # So switch i ON is node 2*i, switch i OFF is node 2*i+1
    
    # To handle the literals:
    # A positive literal l means switch |l| should be ON -> node 2*|l|
    # A negative literal l means switch |l| should be OFF -> node 2*|l|+1
    
    def var_index(lit):
        """Convert a literal to its node index"""
        if lit > 0:
            return 2 * lit
        else:
            return 2 * (-lit) + 1
            
    def neg_var_index(lit):
        """Get the negation of a literal's node index"""
        if lit > 0:
            return 2 * lit + 1
        else:
            return 2 * (-lit)
            
    # Build implication graph for 2-SAT
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # The constraint is: if not l1 then l2, and if not l2 then l1
        # Which translates to: (l1 OR l2)
        # In implication graph: (not l1 -> l2) and (not l2 -> l1)
        
        # not l1 -> l2
        adj[neg_var_index(l1)].append(var_index(l2))
        rev_adj[var_index(l2)].append(neg_var_index(l1))
        
        # not l2 -> l1
        adj[neg_var_index(l2)].append(var_index(l1))
        rev_adj[var_index(l1)].append(neg_var_index(l2))
        
    # Kosaraju's algorithm for finding SCCs
    visited = [False] * (2 * (n + 1))
    order = []
    
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
    for i in range(2, 2*n + 2):  # nodes from 2 to 2*n+1
        if not visited[i]:
            dfs1(i)
            
    # Second DFS pass on reversed graph
    visited = [False] * (2 * (n + 1))
    components = []
    assignment = [-1] * (n + 1)
    
    while order:
        u = order.pop()
        if not visited[u]:
            component = []
            dfs2(u, component)
            components.append(component)
            
            # Check if component contains both a variable and its negation
            var_in_component = set()
            for node in component:
                if node % 2 == 0:  # even node, represents x_i (ON)
                    var_id = node // 2
                    if (var_id * 2 + 1) in var_in_component:  # its negation was seen
                        print("NO")
                        return
                    var_in_component.add(node)
                else:  # odd node, represents not x_i (OFF)
                    var_id = (node - 1) // 2
                    if (var_id * 2) in var_in_component:  # its negation was seen
                        print("NO")
                        return
                    var_in_component.add(node)
                    
            # Assign values to variables in this component
            for node in component:
                if node % 2 == 0:  # x_i (ON)
                    var_id = node // 2
                    if assignment[var_id] == -1:
                        assignment[var_id] = 1  # ON
                else:  # not x_i (OFF)
                    var_id = (node - 1) // 2
                    if assignment[var_id] == -1:
                        assignment[var_id] = 0  # OFF
                        
    # Check if all variables were assigned
    for i in range(1, n + 1):
        if assignment[i] == -1:
            assignment[i] = 0  # Default to OFF if unconstrained
            
    print("YES")
    print(' '.join(str(assignment[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()