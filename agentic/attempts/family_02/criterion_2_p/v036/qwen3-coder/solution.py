import sys
from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # If no constraints, any configuration works
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each variable x, we'll have two nodes: x (for x=1) and -x (for x=0)
    # But we'll use a mapping: for variable i (1-based), 
    # node i represents xi=1, node -i represents xi=0
    
    # We build implication graph and solve 2-SAT
    
    # adjacency list for implication graph
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    # Each variable xi corresponds to index i (1-based)
    # xi=1 is represented by literal i
    # xi=0 is represented by literal -i
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # clause is (l1 OR l2)
        # which is equivalent to (NOT l1 -> l2) AND (NOT l2 -> l1)
        
        # NOT l1 -> l2
        if l1 > 0:
            u = -l1  # NOT(x_l1 = 1) means x_l1 = 0
            v = l2
        else:
            u = -l1  # NOT(x_|l1| = 0) means x_|l1| = 1
            v = l2
        
        adj[u].append(v)
        
        # NOT l2 -> l1
        if l2 > 0:
            u = -l2
            v = l1
        else:
            u = -l2
            v = l1
            
        adj[u].append(v)
    
    # Now we do Kosaraju's algorithm to find strongly connected components
    visited = set()
    order = []
    
    def dfs1(u):
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                dfs1(v)
        order.append(u)
    
    # Collect all literals appearing
    all_nodes = set()
    for u in adj:
        all_nodes.add(u)
        for v in adj[u]:
            all_nodes.add(v)
            
    for u in all_nodes:
        if u not in visited:
            dfs1(u)
    
    # Build reverse graph
    for u in adj:
        for v in adj[u]:
            rev_adj[v].append(u)
    
    visited.clear()
    scc = {}
    scc_id = 0
    
    def dfs2(u):
        visited.add(u)
        scc[u] = scc_id
        for v in rev_adj[u]:
            if v not in visited:
                dfs2(v)
    
    # Process in reverse post-order
    for u in reversed(order):
        if u not in visited:
            dfs2(u)
            scc_id += 1
    
    # Check for contradiction: for each variable xi, xi and -xi must be in different SCCs
    for i in range(1, n+1):
        if scc.get(i, -1) == scc.get(-i, -2):
            print("NO")
            return
    
    # Assign values based on topological order of SCCs
    # Variables in later SCCs (higher id) should be assigned TRUE
    assignment = {}
    
    # Create mapping from scc_id to list of literals
    scc_literals = defaultdict(list)
    for lit, sid in scc.items():
        scc_literals[sid].append(lit)
    
    # Process SCCs in topological order (reverse of finishing times in second DFS)
    sorted_scc_ids = sorted(scc_literals.keys(), key=lambda x: x)
    
    assigned_vars = set()
    
    # Process SCCs in increasing order of id
    # Actually, we want the reverse topological order of the condensation
    # In Kosaraju, the first finished SCC in second DFS is sink
    # So we process in the order we found them in second DFS (which is reverse topological)
    # But since we used normal order in dfs2, let's re-sort properly
    
    # Let's just assign based on the fact that if SCC A -> SCC B, then A comes before B in topo order
    # So higher SCC id means later in topological order, so we set those to True
    
    for sid in sorted(scc_literals.keys()):
        for lit in scc_literals[sid]:
            var = abs(lit)
            if var not in assigned_vars and var <= n:
                if lit > 0:
                    assignment[var] = 1
                else:
                    assignment[var] = 0
                assigned_vars.add(var)
    
    # For unassigned variables, assign default value (e.g., 0)
    for i in range(1, n+1):
        if i not in assignment:
            assignment[i] = 0
    
    result = []
    for i in range(1, n+1):
        result.append(str(assignment[i]))
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()