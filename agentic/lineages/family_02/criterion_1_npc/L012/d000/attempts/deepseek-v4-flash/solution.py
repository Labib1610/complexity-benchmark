import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    clauses = []
    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx]); l2 = int(input_data[idx+1]); l3 = int(input_data[idx+2])
        idx += 3
        clauses.append((l1, l2, l3))
    
    # Convert literals to variable indices: positive x -> 2*x, negative x -> 2*x+1
    # We'll use 0-based variable indices internally.
    def lit_to_var(lit):
        var = abs(lit) - 1
        return var, lit > 0
    
    # Build clause list in internal form: each clause is list of (var, is_true)
    clause_list = []
    for c in clauses:
        clause = []
        for lit in c:
            var, val = lit_to_var(lit)
            clause.append((var, val))
        clause_list.append(clause)
    
    assignment = [None] * n  # None = unassigned, True/False = value
    
    # Watch lists: for each variable, list of clause indices where it appears
    watch = [[] for _ in range(n)]
    for ci, clause in enumerate(clause_list):
        for var, _ in clause:
            watch[var].append(ci)
    
    # For unit propagation and pure literal, we need to track clause status
    # We'll implement a simple recursive backtracking with propagation.
    
    def propagate():
        changed = True
        while changed:
            changed = False
            # Unit propagation
            for ci, clause in enumerate(clause_list):
                unassigned = []
                satisfied = False
                for var, val in clause:
                    if assignment[var] is None:
                        unassigned.append((var, val))
                    elif assignment[var] == val:
                        satisfied = True
                        break
                if satisfied:
                    continue
                if len(unassigned) == 0:
                    return False  # conflict
                if len(unassigned) == 1:
                    var, val = unassigned[0]
                    if assignment[var] is None:
                        assignment[var] = val
                        changed = True
                    elif assignment[var] != val:
                        return False
            # Pure literal elimination
            # For each unassigned variable, check if it appears only with one polarity
            for var in range(n):
                if assignment[var] is not None:
                    continue
                pos_seen = False
                neg_seen = False
                for ci in watch[var]:
                    clause = clause_list[ci]
                    # Check if clause is already satisfied
                    sat = False
                    for v, val in clause:
                        if assignment[v] is not None and assignment[v] == val:
                            sat = True
                            break
                    if sat:
                        continue
                    # If not satisfied, check polarity in this clause
                    for v, val in clause:
                        if v == var:
                            if val:
                                pos_seen = True
                            else:
                                neg_seen = True
                            break
                if pos_seen and not neg_seen:
                    assignment[var] = True
                    changed = True
                elif neg_seen and not pos_seen:
                    assignment[var] = False
                    changed = True
        return True
    
    def backtrack():
        # Propagate first
        if not propagate():
            return False
        # Find unassigned variable
        var = -1
        for i in range(n):
            if assignment[i] is None:
                var = i
                break
        if var == -1:
            return True  # all assigned
        
        # Try both values
        for val in [True, False]:
            assignment[var] = val
            saved = assignment[:]
            if backtrack():
                return True
            assignment[:] = saved
        assignment[var] = None
        return False
    
    if backtrack():
        print("YES")
        print(" ".join('1' if assignment[i] else '0' for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()