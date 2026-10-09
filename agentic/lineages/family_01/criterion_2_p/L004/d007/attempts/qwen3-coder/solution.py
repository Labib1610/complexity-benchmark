import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    edge_indices = defaultdict(list)
    
    idx = 2
    for i in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
        edge_indices[(u, v)].append(i)
        edge_indices[(v, u)].append(i)
    
    # Precompute cross products
    V = {1: (1, 2, 2), 2: (2, 1, 2)}
    
    def cross(a, b):
        return (a[1]*b[2] - a[2]*b[1], 
                a[2]*b[0] - a[0]*b[2], 
                a[0]*b[1] - a[1]*b[0])
    
    def norm_sq(vec):
        return vec[0]**2 + vec[1]**2 + vec[2]**2
    
    # Compute required norm squared for each edge
    required_norm = {}
    for u, v in edges:
        required_norm[(u, v)] = 17
        required_norm[(v, u)] = 17
    
    # For each edge, determine what combinations of s_u and s_v give norm 17
    valid_pairs = {}
    for s_u in [1, 2]:
        for s_v in [1, 2]:
            vec = cross(V[s_u], V[s_v])
            norm_val = norm_sq(vec)
            if norm_val == 17:
                valid_pairs[(s_u, s_v)] = True
            else:
                valid_pairs[(s_u, s_v)] = False
                
    # Build constraints graph
    # For each edge (u,v), we have a constraint that (s_u, s_v) must be in {(1,2), (2,1)}
    # This is a 2-SAT problem
    
    # Variables: for each node i, we have two boolean variables:
    # x_i (s_i = 1) and not x_i (s_i = 2)
    # We'll use node_id*2 for x_i (s_i=1) and node_id*2+1 for not x_i (s_i=2)
    # But actually, let's think of it as:
    # var[i] = 2*i for s_i=1, var[i]+1 = 2*i+1 for s_i=2
    # But to avoid confusion, let's map:
    # For node i:
    # variable 2*i represents s_i = 1 (True)
    # variable 2*i+1 represents s_i = 2 (False)
    # Wait, that's confusing. Let me re-think.
    # Let's say:
    # variable 2*(i-1) represents s_i = 1
    # variable 2*(i-1)+1 represents s_i = 2
    # But even simpler: for node i (1-based):
    # literal 2*i means s_i = 1
    # literal 2*i + 1 means s_i = 2
    # No, that's also bad because then 2*i and 2*i+1 are both for node i.
    # Standard approach:
    # For node i (1-based):
    # variable (i-1)*2     represents s_i = 1
    # variable (i-1)*2 + 1 represents s_i = 2
    # But we need to encode implications.
    
    # Actually, let's think of literals:
    # For node i:
    # literal 2*i-2 represents s_i = 1
    # literal 2*i-1 represents s_i = 2
    # But to make indexing easier with 1-based nodes:
    # literal 2*(i-1) represents s_i = 1 (variable index 2*(i-1))
    # literal 2*(i-1)+1 represents s_i = 2 (variable index 2*(i-1)+1)
    
    # For implication a => b, we add (~a OR b)
    # For constraint that (s_u,s_v) must be (1,2) or (2,1):
    # This means:
    # NOT ((s_u=1) AND (s_v=1)) 
    # AND NOT ((s_u=2) AND (s_v=2))
    # Which is equivalent to:
    # (s_u!=1 OR s_v!=1) AND (s_u!=2 OR s_v!=2)
    # Which is:
    # (s_u=2 OR s_v=2) AND (s_u=1 OR s_v=1)
    # In terms of literals (with 0-based indexing for variables):
    # For node u: var_u_1 = 2*(u-1), var_u_2 = 2*(u-1)+1
    # For node v: var_v_1 = 2*(v-1), var_v_2 = 2*(v-1)+1
    # Clauses:
    # (var_u_2 OR var_v_2)  i.e. (NOT var_u_1 OR NOT var_v_1)
    # (var_u_1 OR var_v_1)  i.e. (NOT var_u_2 OR NOT var_v_2)
    # Wait, no. Let me be more careful.
    #
    # s_u=1 corresponds to setting variable for "s_u=1" to True
    # s_u=2 corresponds to setting variable for "s_u=1" to False
    #
    # So if we have variables:
    # For each node u, we have boolean variable x_u meaning "s_u = 1"
    # Then s_u = 1 iff x_u is True, s_u = 2 iff x_u is False.
    #
    # The valid pairs are (1,2) and (2,1).
    # This means:
    # (s_u=1 AND s_v=2) OR (s_u=2 AND s_v=1)
    # Which is:
    # (x_u AND NOT x_v) OR (NOT x_u AND x_v)
    # This is XOR: x_u XOR x_v
    # Which can be encoded as:
    # (x_u OR x_v) AND (NOT x_u OR NOT x_v)
    #
    # So clauses are:
    # (x_u OR x_v)
    # (NOT x_u OR NOT x_v)
    #
    # In DIMACS format with variable indices:
    # For node u: variable index is u
    # For node v: variable index is v
    # But we want to distinguish between s_u=1 and s_u=2 variables.
    # So let's use:
    # For node i, variable index for "s_i=1" is 2*i - 1
    # For node i, variable index for "s_i=2" is 2*i
    # No, that duplicates. Let's do:
    # Variable index for node i is i (for s_i=1)
    # But then how to represent s_i=2? 
    # Ah, in 2-SAT, we don't have separate variables for s_i=2.
    # We just interpret the value of the single boolean variable for node i.
    # If x_i is true, then s_i=1. If x_i is false, then s_i=2.
    #
    # So for node u and v, the constraint is:
    # (x_u OR x_v) AND (NOT x_u OR NOT x_v)
    # In clause form:
    # (u OR v)
    # (-u OR -v)
    # Where -u means NOT x_u.
    
    # Number of variables
    num_vars = n
    # Clauses will be list of pairs (a, b) representing (a OR b)
    # where a and b are literals (positive or negative integers)
    clauses = []
    
    for u, v in edges:
        # Add clauses for XOR constraint
        clauses.append((u, v))      # x_u OR x_v
        clauses.append((-u, -v))    # NOT x_u OR NOT x_v
    
    # Now solve 2-SAT
    # We'll use strongly connected components (SCC) approach
    
    # Build implication graph
    # Nodes: 1..n for x_i, -(1..n) for NOT x_i
    # But in implementation, we'll map to 0-based indices
    # Node indices: 0 .. 2*n-1
    # For variable i (1-based): 
    #   node 2*(i-1) represents x_i (s_i=1)
    #   node 2*(i-1)+1 represents NOT x_i (s_i=2)
    # But actually, let's think of it differently:
    # For literal L:
    #   if L > 0: node index = 2*(L-1)
    #   if L < 0: node index = 2*(-L-1)+1
    # And reverse mapping:
    #   node index j:
    #     if j is even: represents variable j//2 + 1 set to True
    #     if j is odd:  represents variable (j-1)//2 + 1 set to False
    
    adj_impl = [[] for _ in range(2 * n)]
    rev_adj = [[] for _ in range(2 * n)]
    
    # Mapping function
    def lit_to_node(lit):
        if lit > 0:
            return 2 * (lit - 1)
        else:
            return 2 * (-lit - 1) + 1
            
    def node_to_lit(node):
        if node % 2 == 0:
            return (node // 2) + 1
        else:
            return -((node - 1) // 2 + 1)
    
    # For clause (a OR b), we add edges (~a -> b) and (~b -> a)
    for a, b in clauses:
        # ~a -> b
        adj_impl[lit_to_node(-a)].append(lit_to_node(b))
        rev_adj[lit_to_node(b)].append(lit_to_node(-a))
        # ~b -> a
        adj_impl[lit_to_node(-b)].append(lit_to_node(a))
        rev_adj[lit_to_node(a)].append(lit_to_node(-b))
        
    # Kosaraju's algorithm for SCC
    order = []
    visited = [False] * (2 * n)
    
    def dfs1(u):
        visited[u] = True
        for v in adj_impl[u]:
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
        var_node_true = 2 * i       # x_{i+1}
        var_node_false = 2 * i + 1  # NOT x_{i+1}
        if scc_id[var_node_true] == scc_id[var_node_false]:
            print("NO")
            return
            
    # Assign values: process SCCs in reverse topological order
    # The SCC ids are already in reverse topological order since we used Kosaraju
    assignment = [None] * n
    
    # Process nodes in order of decreasing SCC id
    scc_nodes = [[] for _ in range(scc_count)]
    for node in range(2 * n):
        scc_nodes[scc_id[node]].append(node)
        
    for comp_id in reversed(range(scc_count)):
        for node in scc_nodes[comp_id]:
            lit = node_to_lit(node)
            var_index = abs(lit) - 1  # 0-based
            if assignment[var_index] is None:
                # Assign based on literal
                if lit > 0:
                    assignment[var_index] = True   # s_{var_index+1} = 1
                else:
                    assignment[var_index] = False  # s_{var_index+1} = 2
                    
    # Convert to result: 1 for True (s_i=1), 2 for False (s_i=2)
    result = []
    for val in assignment:
        if val:
            result.append(1)
        else:
            result.append(2)
            
    # To get lexicographically smallest, we should try assigning 1 first
    # Our current assignment might not be lex smallest
    # We need to ensure that when we have a choice, we pick the smaller value
    # In 2-SAT solution, if a variable and its negation are in different SCCs,
    # we can choose the value based on the topological order
    # To get lex smallest, when processing SCC, if we have a choice, prefer False (which means s_i=2)
    # No, wait. Let's re-examine:
    # x_i = True means s_i = 1
    # x_i = False means s_i = 2
    # For lex smallest, we want s_i = 1 if possible.
    # So when we have a choice in SCC, we should set x_i = True (s_i=1) if possible.
    # But we're constrained by the SCC structure.
    # Actually, our assignment above should already respect the constraints.
    # To get lex smallest, we should process variables in order 1 to n,
    # and for each unset variable, try setting it to 1 (True) first.
    # But in 2-SAT, the truth assignment is determined globally by SCCs.
    # However, if a variable's truth value is not forced by SCC (i.e., the variable node and its negation node are in different SCCs),
    # and the SCC containing the variable node comes AFTER the SCC containing its negation in the topological sort,
    # then we can set the variable to False. Otherwise, it's forced.
    # To get lex smallest, when we have a free choice, we should choose True (s_i=1).
    
    # Actually, let's re-implement the assignment part to ensure lex smallest.
    # When we process an SCC, if a variable and its negation are in different SCCs,
    # and this SCC hasn't been assigned yet, we can choose.
    # For lex smallest, we prefer the variable to be True (s_i=1).
    # But we have to be consistent within the SCC.
    
    # Let's think of it this way:
    # Each SCC represents a set of literals that must have the same truth value.
    # When processing SCCs in reverse topological order, if we haven't assigned a variable yet,
    # we can choose its value. For lex smallest, we prefer s_i=1, which means x_i=True.
    
    final_assignment = [None] * n
    for comp_id in reversed(range(scc_count)):
        nodes_in_scc = scc_nodes[comp_id]
        # Determine if we should set variables in this SCC to True or False
        # For lex smallest, prefer True unless it would conflict
        # But in a single SCC, all literals must be consistent
        # We just need to pick a consistent assignment
        
        # Check if any variable in this SCC has already been assigned due to another literal in same SCC
        # But actually, in an SCC, if it contains both a variable and its negation, it's unsatisfiable
        # We already checked that.
        
        # Pick assignment that leads to lex smallest result
        # Since all variables in an SCC must have consistent values,
        # we look at the "canonical" literal in the SCC and decide based on that
        # For lex smallest, prefer x_i = True (s_i=1) over x_i = False (s_i=2)
        # So we prefer the positive literal
        
        # Find a representative literal from this SCC
        # To get lex smallest, among literals in the SCC, we prefer positive ones
        # But we have to be consistent. 
        # A simple heuristic: if there's a positive literal in the SCC, set it to True
        # If there's only negative literals, set them to False (which makes original variables True)
        # No, that's not right logic.
        
        # Correct approach:
        # An SCC represents a set of equivalences.
        # When processing SCCs in reverse topological order, 
        # if a variable appears as a positive literal in the SCC, we can set it to True
        # if it appears as a negative literal, we set it to False
        # But we have to be consistent.
        
        # Simpler: for each variable in SCC, check if it or its negation determines the value
        # But to get lex smallest, when we have a choice, prefer s_i=1 (x_i=True)
        
        # Let's take the first literal from the SCC and base our decision on it
        # But to ensure lex smallest, we should iterate through variables in order
        # and for each unassigned one, if it appears in this SCC, assign it to make s_i=1 if possible
        
        # Even simpler approach:
        # Process variables in order 1 to n
        # For each unassigned variable, check which literals involving it are in this SCC
        # If x_i is in SCC: set x_i = True (s_i=1)  
        # If NOT x_i is in SCC: set x_i = False (s_i=2)
        # But we must be consistent within the SCC
        
        # Best approach: 
        # For each variable in this SCC, determine what the SCC forces
        # If both x_i and NOT x_i are in same SCC, it's unsat (we already checked)
        # So for each variable, exactly one of x_i or NOT x_i is in the SCC
        # We set the variable accordingly
        
        # To get lex smallest, when we have a choice (i.e., when processing the SCC that contains x_i),
        # we prefer x_i = True. This happens automatically if x_i is in the SCC.
        # If NOT x_i is in the SCC, we must set x_i = False.
        
        for node in nodes_in_scc:
            lit = node_to_lit(node)
            var_index = abs(lit) - 1
            if final_assignment[var_index] is None:
                if lit > 0:
                    final_assignment[var_index] = True   # s_{var_index+1} = 1
                else:
                    final_assignment[var_index] = False  # s_{var_index+1} = 2
                    
    # Convert to output format
    output_result = []
    for val in final_assignment:
        if val:
            output_result.append(1)
        else:
            output_result.append(2)
            
    print("YES")
    print(" ".join(map(str, output_result)))

if __name__ == "__main__":
    main()