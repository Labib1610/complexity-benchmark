import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # Each relay is a clause: (w1 OR w2 OR w3)
    # w_i > 0 means valve w_i = 1
    # w_i < 0 means valve |w_i| = 0
    # We need to find an assignment that satisfies all clauses.
    
    # We use a backtracking search with unit propagation (DPLL simplification).
    # Since n <= 90, we can use bitmasks to represent clauses.
    
    # Precompute masks for positive and negative literals
    # pos_mask[i] has bit i set if valve i+1 must be 1
    # neg_mask[i] has bit i set if valve i+1 must be 0
    
    clauses_pos = []
    clauses_neg = []
    
    for _ in range(m):
        w1 = int(next(it))
        w2 = int(next(it))
        w3 = int(next(it))
        
        p_mask = 0
        n_mask = 0
        
        for w in [w1, w2, w3]:
            v = abs(w) - 1
            if w > 0:
                p_mask |= (1 << v)
            else:
                n_mask |= (1 << v)
        
        clauses_pos.append(p_mask)
        clauses_neg.append(n_mask)
    
    # Current assignment: 1 = True, 0 = False, -1 = Unassigned
    assignment = [-1] * n
    
    def solve_recursive(idx):
        # Simplify clauses based on current assignment
        # We track if we find a unit clause that forces an assignment
        
        # Simplification pass
        while True:
            unit_found = False
            for i in range(m):
                # Check if clause is already satisfied
                # Clause is satisfied if any literal is True
                # Literal (valve v = 1) is True if assignment[v] == 1
                # Literal (valve v = 0) is True if assignment[v] == 0
                
                # Check if satisfied
                satisfied = False
                unassigned_count = 0
                last_unassigned_v = -1
                last_unassigned_val = -1
                
                # Check positive literals in clause
                # Iterate bits in p_mask
                p_m = clauses_pos[i]
                n_m = clauses_neg[i]
                
                # Optimization: iterate only set bits
                # But for simplicity, we iterate all vars or use bit tricks
                
                # Let's just iterate 0..n-1 for now, or better, check bits
                # To speed up, we can check if (p_m & assigned_true_mask) != 0
                # But we need to know which are assigned.
                
                # Let's iterate variables in the clause
                # Combine p_m and n_m to get involved variables
                involved = p_m | n_m
                
                # If involved is 0 (empty clause?), but problem says 3 observations
                # so involved is not empty.
                
                clause_satisfied = False
                clause_unassigned_v = -1
                clause_unassigned_val = -1
                clause_empty = True
                
                v = 0
                while involved:
                    if involved & 1:
                        # Variable v is in this clause
                        val = assignment[v]
                        if val != -1:
                            # Assigned
                            # Check if it satisfies the clause
                            # Positive literal: v must be 1
                            # Negative literal: v must be 0
                            # If (p_m has v and val == 1) -> satisfied
                            # If (n_m has v and val == 0) -> satisfied
                            if ((p_m >> v) & 1) and val == 1:
                                clause_satisfied = True
                                break
                            if ((n_m >> v) & 1) and val == 0:
                                clause_satisfied = True
                                break
                        else:
                            # Unassigned
                            # This could be the one we need to assign
                            # We need to know what value it would take to satisfy
                            # If p_m has v, needs 1
                            # If n_m has v, needs 0
                            # (It can't have both, as per problem structure, one obs per wire)
                            
                            clause_empty = False
                            if clause_unassigned_v == -1:
                                # First unassigned
                                if (p_m >> v) & 1:
                                    clause_unassigned_val = 1
                                else:
                                    clause_unassigned_val = 0
                                clause_unassigned_v = v
                            else:
                                # Second unassigned, so not a unit clause
                                clause_unassigned_v = -2 # marker for >1 unassigned
                    
                    involved >>= 1
                    v += 1
                
                if clause_satisfied:
                    continue
                
                if clause_empty:
                    # All literals false -> Conflict
                    return False
                
                if clause_unassigned_v >= 0:
                    # Unit clause: must assign clause_unassigned_v = clause_unassigned_val
                    v_to_assign = clause_unassigned_v
                    val_to_assign = clause_unassigned_val
                    
                    # Check consistency
                    if assignment[v_to_assign] == -1:
                        assignment[v_to_assign] = val_to_assign
                        unit_found = True
                    elif assignment[v_to_assign] != val_to_assign:
                        return False
            
            if not unit_found:
                break
        
        # Check if all assigned
        if all(x != -1 for x in assignment):
            return True
        
        # Find first unassigned
        for i in range(n):
            if assignment[i] == -1:
                next_var = i
                break
        
        # Try assigning 1
        saved_assignment = assignment[:]
        assignment[next_var] = 1
        if solve_recursive(next_var + 1):
            return True
        
        assignment = saved_assignment
        # Try assigning 0
        assignment[next_var] = 0
        if solve_recursive(next_var + 1):
            return True
        
        assignment[next_var] = -1
        return False

    if solve_recursive(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

solve()