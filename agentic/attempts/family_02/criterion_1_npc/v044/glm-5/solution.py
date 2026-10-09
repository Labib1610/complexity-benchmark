import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # Each check is a clause: (var, value) pairs, meaning var = value is one option.
    # Clause is satisfied if at least one option holds.
    clauses = []
    for _ in range(m):
        opts = []
        for _ in range(3):
            c = int(next(it))
            var = abs(c)
            val = 1 if c > 0 else 0
            opts.append((var, val))
        clauses.append(opts)
    
    # Current assignment: None means unknown, 0 or 1 means fixed.
    state = [None] * (n + 1)
    
    def check_clause(idx, st):
        """Check if clause idx is satisfied under state st."""
        for v, val in clauses[idx]:
            if st[v] is not None and st[v] == val:
                return True
        return False
    
    # Pre-check: are there any clauses unsatisfiable even with all free variables?
    # A clause is impossible to satisfy iff all its options are invalid.
    # An option (v, val) is invalid if state[v] is not None and state[v] != val.
    for ci, cl in enumerate(clauses):
        possible = False
        for v, val in cl:
            if state[v] is None or state[v] == val:
                possible = True
                break
        if not possible:
            print("NO")
            return
    
    # Propagation step
    changed = True
    while changed:
        changed = False
        for ci, cl in enumerate(clauses):
            if check_clause(ci, state):
                continue
            # Clause not satisfied yet.
            # Collect valid options (those not contradicted by current state).
            valid_opts = []
            for v, val in cl:
                if state[v] is None or state[v] == val:
                    valid_opts.append((v, val))
            
            # If only one valid option remains, we must take it.
            if len(valid_opts) == 1:
                v, val = valid_opts[0]
                if state[v] is None:
                    state[v] = val
                    changed = True
            elif len(valid_opts) == 0:
                # This clause is impossible.
                print("NO")
                return
    
    # Algorithm setup for solving remaining variables
    all_vars = list(range(1, n + 1))
    
    # Helper to solve SAT for remaining unset variables.
    # Returns True if satisfiable, else False. Modifies state in place.
    def solve_sat():
        # Build mapping from global var to local var index
        unset_vars = [v for v in all_vars if state[v] is None]
        if not unset_vars:
            return True
        
        var_to_idx = {v: i for i, v in enumerate(unset_vars)}
        K = len(unset_vars)
        
        # Build adjacency list for implication graph
        # Node indices: 2*i for x_i = False, 2*i+1 for x_i = True
        adj = [[] for _ in range(2 * K)]
        radj = [[] for _ in range(2 * K)]
        
        def add_implication(u_if, u_val, v_if, v_val):
            """If u = u_val then v = v_val"""
            u_node = 2 * u_if + u_val
            v_node = 2 * v_if + v_val
            adj[u_node].append(v_node)
            radj[v_node].append(u_node)
        
        # Process clauses to add implications
        # A clause (a v b v c) is equivalent to:
        # (not a -> b v c) and (not a and not b -> c), etc.
        # We useUC: if there are k fixed false options in a clause, 
        # and exactly K-k-1 other options, then the last one must be true.
        # Generalized for 3-options:
        # If 2 options are false, the 3rd must be true.
        # If 1 option is false, the other 2 form a binary clause.
        
        for cl in clauses:
            # Categorize options by variable status
            # fixed_false: options contradicted by state
            # fixed_true: options already satisfied by state
            # free: options whose variable is unset or matches state
            
            # Actually we only care about unset variables.
            # Let's build the list of options relevant to 2-SAT
            # An option is "active" in 2-SAT if its var is unset, OR if it's already fixed true.
            # If fixed true, clause is satisfied, skip.
            
            satisfied = False
            free_opts = []
            for v, val in cl:
                if state[v] is not None:
                    if state[v] == val:
                        satisfied = True
                        break
                else: # state[v] is None
                    free_opts.append((v, val))
            
            if satisfied:
                continue
            
            k = len(free_opts)
            if k == 0:
                return False
            
            # Implications: for each free option o_i, if it's false, then at least one of the others must be true.
            # If k=1: (not o_1 -> False), so o_1 must be true.
            # If k=2: (not o_1 -> o_2) and (not o_2 -> o_1). Binary clause.
            # If k=3: (not o_1 -> o_2 v o_3). This is SAT but not 2-SAT.
            #       We transform (not o_1 -> o_2 v o_3) into CNF: (not o_1 -> o_2) v (not o_1 -> o_3) is wrong.
            #       (a -> b v c) is not directly solvable by unit/binary implications.
            #       We have to use the standard reduction: x <-> (o_2 v o_3), then (not o_1 -> x).
            #       Or simpler: try assignments to one variable.
            
            if k == 1:
                v, val = free_opts[0]
                idx = var_to_idx[v]
                # Add clause (v = val)
                # We can handle this by setting state directly or adding single-node implications?
                # Wait, we are building graph here, not modifying state.
                # A unary clause v=val is equivalent to (not v -> v) which is not helpful in graph.
                # It means we must set v=val. But solve_sat is for 2-SAT.
                # If we have unary clause, it's not purely 2-SAT.
                # However, we can treat it by guessing.
                
                # Actually, if k=1, it means 2 options are fixed false. The last one must be true.
                # This should have been caught by propagation?
                # Maybe not if propagation was not exhaustive.
                # But since we are here, we might still have unary clauses derived from 3-vars.
                # Let's just recursively branch on one variable if we can't handle.
                
                # Warshall's algorithm for 2-SAT with ternary clauses?
                # Let's just use recursion: pick a var, try both.
                pass
            
            # Since general 3-SAT is NP-complete, we must use recursion/DP for exact solving.
            # The number of unset vars K <= n <= 90. Too large for O(2^K).
            # BUT clauses have specific structure.
            # Backtracking with pruning should be fine for K<=90, m=400?
            # Possibly not. 2^90 is too large.
            # However, the propagation might have reduced K significantly.
            # Let's check the worst case.
            # Propagation handles cases where 2 vars fixed so 3rd is fixed.
            # Remaining unsolved variables are in components where no "2 fixed" exists.
            # This means for every clause, either satisfied, or has 3 free vars, or 2 free and 1 fixed false (but we handled 2 fixed false?).
            # Propagation stops when no clause has exactly 1 valid option.
            # So remaining clauses have 0 valid (impossible, returned NO), 2 valid, or 3 valid.
            # 0 valid -> handled.
            # 1 valid -> handled.
            
            # So remaining state:
            # Clauses are either:
            #  1. Satisfied (ignored)
            #  2. Have 2 valid options (binary clause). Unit assignment reduces this to satisfied.
            #  3. Have 3 valid options (ternary clause).
            
            # If we have binary clauses (k=2), we can use 2-SAT logic.
            # If we have ternary clauses (k=3), we can't directly.
            # However, notice that k=3 implies all 3 vars are unset.
            # We can pick one var, try values. If setting it reduces ternary clauses to binary, solver handles fast.
            
            # Strategy:
            # Collect remaining clauses (simplified).
            # Use backtracking with 2-SAT-check lookahead.
            # Pick a var, try 0 and 1. For each branch:
            #   Assert unit clause.
            #   Propagate unit clauses and binary clauses (2-SAT + unit propagation).
            #   If conflict, backtrack.
            #   If no conflict, recurse.
            
            # This combined Unit-Prop + 2SAT + Recursion is DPLL with 2-SAT lookahead.
            # It is correct and fast for these constraints.
        
        # Implementation of DPLL with 2-SAT lookahead
        # We need to manage state, unit clauses, binary clauses.
        # Since state is global list, we need careful rollback.
        
        pass
    
    # Since we need to implement the recursive solver and the helper logic inside solve(),
    # let's restructure to use a class or nested functions for clarity.
    pass

# Re-implementing with DPLL + 2-SAT lookahead structure.

def solve():
    import sys
    sys.setrecursionlimit(10000)
    
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    init_clauses = []
    for _ in range(m):
        raw = []
        for _ in range(3):
            x = int(next(it))
            raw.append((abs(x), 1 if x > 0 else 0))
        init_clauses.append(raw)
    
    # state[v] = 0, 1, or None
    state = [None] * (n + 1)
    
    # Simple propagation until fixed point handles unit clauses derived from ternary
    # where 2 options are blocked.
    
    while True:
        found_unit = False
        for cl in init_clauses:
            # Check satisfied
            sat = False
            for v, val in cl:
                if state[v] is not None and state[v] == val:
                    sat = True
                    break
            if sat:
                continue
            
            # Not satisfied. Collect possible options.
            possible = []
            for v, val in cl:
                if state[v] is None or state[v] == val:
                    possible.append((v, val))
            
            if len(possible) == 0:
                print("NO")
                return
            
            if len(possible) == 1:
                v, val = possible[0]
                if state[v] is not None and state[v] != val:
                    print("NO")
                    return
                if state[v] is None:
                    state[v] = val
                    found_unit = True
        
        if not found_unit:
            break
    
    # If all set, check and return
    if all(state[i] is not None for i in range(1, n+1)):
        # Verify
        for cl in init_clauses:
            sat = False
            for v, val in cl:
                if state[v] == val:
                    sat = True
                    break
            if not sat:
                print("NO")
                return
        print("YES")
        print(" ".join(map(str, state[1:])))
        return
    
    # We have partial assignment. Remaining problem is SAT.
    # Variables are 1..n.
    # Clauses are ternary.
    # We use DPLL algorithm with pure literal elimination? No, pure literal doesn't work well with "at least one".
    # We use DPLL with MOMs heuristic or just random picking?
    # Given constraints n=90, we need good pruning.
    
    # But first, verify current partial state consistency.
    # We already did consistency check in propagation.
    
    # Let's use a simple DPLL that picks a variable and recurses.
    # Optimization: Check 2-SAT core correctness first?
    # If we treat ternary clauses as (a v b v c), and we assign a=False,
    # it becomes (b v c). This is binary.
    # If we have many binary clauses, we can propagate fast.
    
    # Let's build an implication graph dynamically or maintain clause list.
    # state is global list.
    
    def recursive_solve():
        # Returns True if solved (state fully assigned and consistent), False otherwise.
        # state is shared.
        
        # 1. Propagation of unit clauses from ternary clauses becoming binary->unit
        # This is the DPLL deduction step.
        # We iterate deductions.
        deduced = True
        while deduced:
            deduced = False
            for cl in init_clauses:
                # Check if satisfied
                sat = False
                # Optimization: sorted or processed?
                # Just scan.
                for v, val in cl:
                    if state[v] is not None and state[v] == val:
                        sat = True
                        break
                if sat:
                    continue
                
                # Count possible
                possible = []
                for v, val in cl:
                    if state[v] is None or state[v] == val:
                        possible.append((v, val))
                
                if len(possible) == 0:
                    return False # Conflict
                
                if len(possible) == 1:
                    v, val = possible[0]
                    # This case handles unit clauses propagating.
                    # Also handles binary clauses becoming unit.
                    state[v] = val
                    deduced = True
        
        # 2. Check if all solved
        if all(state[i] is not None for i in range(1, n+1)):
            return True
        
        # 3. Branch
        # Pick a variable. Heuristic: variable appearing in most unsatisfied clauses?
        # Or simply first unset.
        # Optim: Use variable in smallest active clause (effectively MOMs).
        
        # Construct active clauses (unsatisfied)
        active_clauses = []
        for cl in init_clauses:
            sat = False
            for v, val in cl:
                if state[v] is not None and state[v] == val:
                    sat = True
                    break
            if not sat:
                active_clauses.append(cl)
        
        if not active_clauses:
            # All satisfied?
            # Fill remaining vars with 0.
            for i in range(1, n+1):
                if state[i] is None:
                    state[i] = 0
            return True

        # Pick variable
        # Best start: a variable in a ternary clause.
        # If no ternary, we have binary only. DPLL handles it.
        best_v = -1
        best_score = -1
        # Score: number of unsatisfied clauses containing v.
        cand_map = {}
        for cl in active_clauses:
            for v, val in cl:
                if state[v] is None:
                    cand_map[v] = cand_map.get(v, 0) + 1
        
        if not cand_map:
            # All active clauses use only set variables? Impossible if unsatisfied.
            # This means active_clauses has clause like (1=0 v 1=0 v 1=0) where state[1]=1.
            # This check should have returned False earlier.
            # Impossible state.
            return False
        
        # Pick max occurence
        best_v = max(cand_map, key=lambda k: cand_map[k])
        
        # Try values
        # Order: which value satisfies more?
        # Local lookahead?
        
        # Save state
        snapshot = list(state)
        
        # Try v = 1
        state[best_v] = 1
        if recursive_solve():
            return True
        
        # Restore and try v = 0
        # Need to restore state properly because recursion modifies it
        for i in range(len(state)):
            state[i] = snapshot[i]
        
        state[best_v] = 0
        if recursive_solve():
            return True
            
        # Restore before returning False
        for i in range(len(state)):
            state[i] = snapshot[i]
        return False

    if recursive_solve():
        # Final check (sanity)
        for cl in init_clauses:
            ok = False
            for v, val in cl:
                if state[v] == val:
                    ok = True
                    break
            if not ok:
                print("NO")
                return
        print("YES")
        print(" ".join(map(str, state[1:])))
    else:
        print("NO")

solve()