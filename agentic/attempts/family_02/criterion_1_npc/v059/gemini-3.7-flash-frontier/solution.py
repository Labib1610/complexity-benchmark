import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve_sat():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    clauses = []
    idx = 2
    for _ in range(m):
        c = [int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])]
        idx += 3
        # Simplify clause: remove duplicates
        c_set = set(c)
        # Check if tautology
        tautology = False
        for lit in c_set:
            if -lit in c_set:
                tautology = True
                break
        if not tautology:
            clauses.append(list(c_set))
            
    # DPLL Implementation
    assignment = [None] * (n + 1)
    
    def get_clause_status(clause):
        # Returns:
        # True if satisfied
        # False if unsatisfied (all false)
        # list of unassigned literals otherwise
        unassigned = []
        for lit in clause:
            var = abs(lit)
            val = assignment[var]
            if val is not None:
                if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                    return True, []
            else:
                unassigned.append(lit)
        if not unassigned:
            return False, []
        return None, unassigned

    def unit_propagate():
        trail = []
        while True:
            unit_found = False
            for clause in clauses:
                status, unassigned = get_clause_status(clause)
                if status is True:
                    continue
                if status is False:
                    # Conflict
                    return False, trail
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    val = 1 if lit > 0 else 0
                    assignment[var] = val
                    trail.append(var)
                    unit_found = True
                    break
            if not unit_found:
                break
        return True, trail

    def dpll():
        success, trail = unit_propagate()
        if not success:
            for var in trail:
                assignment[var] = None
            return False

        # Check if all satisfied and compute Jeroslow-Wang weights
        weights = {}
        all_satisfied = True
        
        for clause in clauses:
            status, unassigned = get_clause_status(clause)
            if status is True:
                continue
            if status is False:
                for var in trail:
                    assignment[var] = None
                return False
            all_satisfied = False
            k = len(unassigned)
            w = 2 ** (-k)
            for lit in unassigned:
                weights[lit] = weights.get(lit, 0.0) + w

        if all_satisfied:
            return True

        # Choose best variable using Jeroslow-Wang heuristic
        best_var = None
        best_score = -1.0
        for var in range(1, n + 1):
            if assignment[var] is None:
                pos_w = weights.get(var, 0.0)
                neg_w = weights.get(-var, 0.0)
                score = pos_w + neg_w
                if score > best_score:
                    best_score = score
                    best_var = var

        if best_var is None:
            return True

        pos_w = weights.get(best_var, 0.0)
        neg_w = weights.get(-best_var, 0.0)
        first_val = 1 if pos_w >= neg_w else 0

        # Try first branch
        assignment[best_var] = first_val
        if dpll():
            return True

        # Try second branch
        assignment[best_var] = 1 - first_val
        if dpll():
            return True

        # Backtrack
        assignment[best_var] = None
        for var in trail:
            assignment[var] = None
        return False

    if dpll():
        print("YES")
        res = [assignment[i] if assignment[i] is not None else 0 for i in range(1, n + 1)]
        print(*(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve_sat()