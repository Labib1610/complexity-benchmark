import sys
from collections import defaultdict

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
    
    clauses = []
    index = 2
    for _ in range(m):
        c1 = int(data[index])
        c2 = int(data[index+1])
        index += 2
        # Convert to variable indices and polarities
        # Variables are 1-indexed. We'll use 1..n for s_i=0 and n+1..2n for s_i=1
        # But actually, let's think in terms of s_i being 0 or 1.
        # p_i = 1 - 2*s_i, so p_i = 1 if s_i=0, p_i = -1 if s_i=1.
        # For channel c:
        #   if c > 0: v = p_{|c|} = 1-2*s_{|c|}
        #   if c < 0: v = -p_{|c|} = -(1-2*s_{|c|}) = -1+2*s_{|c|}
        # So for a monitor with channels c1, c2:
        # v1 = (1-2*s_{|c1|}) * sign1, where sign1 = 1 if c1>0 else -1
        # v2 = (1-2*s_{|c2|}) * sign2, where sign2 = 1 if c2>0 else -1
        # R = v1 + v2 + v1*v2 > 0  =>  NOT satisfied
        # We want R <= 0 for all monitors.
        # Let's compute what R > 0 means in terms of s variables.
        
        # Let's denote:
        # a = |c1|, sa = 1 if c1>0 else -1
        # b = |c2|, sb = 1 if c2>0 else -1
        # v1 = (1-2*s_a) * sa = sa - 2*sa*s_a
        # v2 = (1-2*s_b) * sb = sb - 2*sb*s_b
        # R = v1 + v2 + v1*v2
        #   = (sa - 2*sa*s_a) + (sb - 2*sb*s_b) + (sa - 2*sa*s_a)(sb - 2*sb*s_b)
        #   = sa + sb - 2*sa*s_a - 2*sb*s_b + sa*sb - 2*sa*sb*s_a - 2*sa*sb*s_b + 4*sa*sb*s_a*s_b
        #   = sa + sb + sa*sb - 2*s_a*(sa + sa*sb) - 2*s_b*(sb + sa*sb) + 4*sa*sb*s_a*s_b
        #   = sa + sb + sa*sb - 2*sa*(1 + sb)*s_a - 2*sb*(1 + sa)*s_b + 4*sa*sb*s_a*s_b
        # R > 0 is forbidden.
        
        # Let's simplify by cases:
        # Case 1: c1>0, c2>0 => sa=1, sb=1
        #   v1 = 1-2*s_a, v2 = 1-2*s_b
        #   R = (1-2*s_a) + (1-2*s_b) + (1-2*s_a)(1-2*s_b)
        #     = 2 - 2*s_a - 2*s_b + (1 - 2*s_a - 2*s_b + 4*s_a*s_b)
        #     = 3 - 4*s_a - 4*s_b + 4*s_a*s_b
        #   R > 0  <=>  3 - 4*s_a - 4*s_b + 4*s_a*s_b > 0
        #             4*s_a*s_b - 4*s_a - 4*s_b + 3 > 0
        #   Check all (s_a,s_b) in {0,1}^2:
        #     (0,0): 3 > 0  => forbidden
        #     (0,1): -1 > 0 => OK
        #     (1,0): -1 > 0 => OK
        #     (1,1): -1 > 0 => OK
        #   So clause is: NOT (s_a=0 AND s_b=0)  =>  (s_a=1 OR s_b=1)
        
        # Case 2: c1>0, c2<0 => sa=1, sb=-1
        #   v1 = 1-2*s_a, v2 = -1+2*s_b
        #   R = (1-2*s_a) + (-1+2*s_b) + (1-2*s_a)(-1+2*s_b)
        #     = 0 - 2*s_a + 2*s_b + (-1 + 2*s_b + 2*s_a - 4*s_a*s_b)
        #     = -1 - 2*s_a + 2*s_b + 2*s_b + 2*s_a - 4*s_a*s_b
        #     = -1 + 4*s_b - 4*s_a*s_b
        #     = -1 + 4*s_b*(1 - s_a)
        #   R > 0  <=>  4*s_b*(1 - s_a) > 1
        #             s_b*(1 - s_a) > 1/4
        #   Since s_a,s_b in {0,1}, s_b*(1-s_a) in {0,1}
        #   R > 0  <=>  s_b*(1-s_a) = 1  <=>  s_b=1 AND s_a=0
        #   So forbidden is: (s_a=0 AND s_b=1)
        #   Clause is: NOT (s_a=0 AND s_b=1)  =>  (s_a=1 OR s_b=0)
        
        # Case 3: c1<0, c2>0 => sa=-1, sb=1
        #   Symmetric to case 2.
        #   Forbidden: (s_a=1 AND s_b=0)
        #   Clause: (s_a=0 OR s_b=1)
        
        # Case 4: c1<0, c2<0 => sa=-1, sb=-1
        #   v1 = -1+2*s_a, v2 = -1+2*s_b
        #   R = (-1+2*s_a) + (-1+2*s_b) + (-1+2*s_a)(-1+2*s_b)
        #     = -2 + 2*s_a + 2*s_b + (1 - 2*s_b - 2*s_a + 4*s_a*s_b)
        #     = -1 + 4*s_a*s_b
        #   R > 0  <=>  4*s_a*s_b > 1  <=>  s_a*s_b = 1  <=>  s_a=1 AND s_b=1
        #   So forbidden is: (s_a=1 AND s_b=1)
        #   Clause is: NOT (s_a=1 AND s_b=1)  =>  (s_a=0 OR s_b=0)
        
        a = abs(c1)
        b = abs(c2)
        sa = 1 if c1 > 0 else -1
        sb = 1 if c2 > 0 else -1
        
        # Build 2-SAT clauses
        if sa == 1 and sb == 1:
            # Clause: s_a=1 OR s_b=1
            # In 2-SAT: (a_true OR b_true)
            clauses.append((a, True, b, True))
        elif sa == 1 and sb == -1:
            # Clause: s_a=1 OR s_b=0
            # In 2-SAT: (a_true OR b_false)
            clauses.append((a, True, b, False))
        elif sa == -1 and sb == 1:
            # Clause: s_a=0 OR s_b=1
            # In 2-SAT: (a_false OR b_true)
            clauses.append((a, False, b, True))
        else: # sa == -1 and sb == -1
            # Clause: s_a=0 OR s_b=0
            # In 2-SAT: (a_false OR b_false)
            clauses.append((a, False, b, False))
    
    # Now we have a 2-SAT problem. Let's solve it.
    # Variables are 1-indexed from 1 to n.
    # We'll use Kosaraju's algorithm to solve 2-SAT.
    
    # Number of variables
    num_vars = n
    
    # Build implication graph
    # Nodes: 1..n for x_i, n+1..2n for NOT x_i
    # But we think of x_i as s_i = 1, so:
    # Node i (1 <= i <= n) represents s_i = 1
    # Node i+n represents s_i = 0
    
    def var_node(var, val):
        # var is 1-indexed variable number
        # val is True (s_i=1) or False (s_i=0)
        if val:
            return var
        else:
            return var + num_vars
    
    def neg_node(node):
        if node <= num_vars:
            return node + num_vars
        else:
            return node - num_vars
    
    # Adjacency list for implication graph
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    # For each clause (a, val_a, b, val_b) meaning (a==val_a OR b==val_b)
    # This is equivalent to (NOT (a==val_a) => b==val_b) AND (NOT (b==val_b) => a==val_a)
    # Which is (a==(not val_a) => b==val_b) AND (b==(not val_b) => a==val_a)
    for a, val_a, b, val_b in clauses:
        # First implication: a is False (s_a != val_a) => b is True (s_b == val_b)
        # Node for (a, not val_a) => Node for (b, val_b)
        u = var_node(a, not val_a)
        v = var_node(b, val_b)
        adj[u].append(v)
        rev_adj[v].append(u)
        
        # Second implication: b is False (s_b != val_b) => a is True (s_a == val_a)
        u = var_node(b, not val_b)
        v = var_node(a, val_a)
        adj[u].append(v)
        rev_adj[v].append(u)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * num_vars + 1)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(1, 2 * num_vars + 1):
        if not visited[i]:
            dfs1(i)
    
    # Second DFS on transpose graph
    visited = [False] * (2 * num_vars + 1)
    scc_id = [0] * (2 * num_vars + 1)
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
            scc_count += 1
            dfs2(u)
    
    # Check if satisfiable
    for i in range(1, num_vars + 1):
        if scc_id[i] == scc_id[i + num_vars]:
            print("NO")
            return
    
    # Assign values
    assignment = [None] * (num_vars + 1)
    # Process SCCs in reverse topological order
    # We can do this by processing nodes in order of decreasing scc_id
    # But since we used Kosaraju, the last SCC processed is the first in topological order of condensation
    # Actually, in Kosaraju, the order we get SCCs in dfs2 is reverse topological.
    # So we process them in order, and for each, assign values to unassigned variables.
    
    # Create list of (scc_id, node) and sort by scc_id
    scc_nodes = [(scc_id[node], node) for node in range(1, 2 * num_vars + 1)]
    scc_nodes.sort()
    
    # Process in order of SCCs (increasing scc_id, which is reverse topological)
    # But we want to assign False first (s_i=0), which is nodes i+n
    # Actually, let's just go by scc_id order.
    for _, node in scc_nodes:
        var = node if node <= num_vars else node - num_vars
        if assignment[var] is None:
            # Assign the value that corresponds to this node being true in the SCC
            # If node <= num_vars, then s_var = 1
            # If node > num_vars, then s_var = 0
            if node <= num_vars:
                assignment[var] = 1
            else:
                assignment[var] = 0
    
    print("YES")
    print(" ".join(str(assignment[i]) for i in range(1, num_vars + 1)))

if __name__ == "__main__":
    main()