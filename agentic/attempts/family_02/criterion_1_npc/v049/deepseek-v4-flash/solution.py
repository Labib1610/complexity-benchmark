import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        clauses.append((l1, l2, l3))
    
    # We'll use a simple DPLL-like backtracking
    assignment = [None] * (n + 1)  # None = unassigned, True = warm, False = cool
    
    # Precompute clause literals as (var, is_positive)
    clause_lits = []
    for c in clauses:
        lits = []
        for lit in c:
            var = abs(lit)
            is_pos = lit > 0
            lits.append((var, is_pos))
        clause_lits.append(lits)
    
    def evaluate_clause(clause):
        # Returns True if satisfied, False if violated, None if undetermined
        satisfied = False
        undetermined = False
        for var, is_pos in clause:
            val = assignment[var]
            if val is None:
                undetermined = True
            else:
                if val == is_pos:
                    satisfied = True
                    break
        if satisfied:
            return True
        if undetermined:
            return None
        return False
    
    def unit_propagate():
        changed = True
        while changed:
            changed = False
            for clause in clause_lits:
                status = evaluate_clause(clause)
                if status is False:
                    return False
                if status is None:
                    # Check if only one unassigned literal
                    unassigned = []
                    for var, is_pos in clause:
                        if assignment[var] is None:
                            unassigned.append((var, is_pos))
                    if len(unassigned) == 1:
                        var, is_pos = unassigned[0]
                        assignment[var] = is_pos
                        changed = True
        return True
    
    def pure_literal_eliminate():
        # Find pure literals: variables that appear only with one polarity in unresolved clauses
        pos_count = {}
        neg_count = {}
        for clause in clause_lits:
            status = evaluate_clause(clause)
            if status is not None:
                continue
            for var, is_pos in clause:
                if assignment[var] is not None:
                    continue
                if is_pos:
                    pos_count[var] = pos_count.get(var, 0) + 1
                else:
                    neg_count[var] = neg_count.get(var, 0) + 1
        for var in range(1, n + 1):
            if assignment[var] is not None:
                continue
            p = pos_count.get(var, 0)
            q = neg_count.get(var, 0)
            if p > 0 and q == 0:
                assignment[var] = True
            elif q > 0 and p == 0:
                assignment[var] = False
    
    def backtrack():
        if not unit_propagate():
            return False
        pure_literal_eliminate()
        # Find first unassigned variable
        var = None
        for i in range(1, n + 1):
            if assignment[i] is None:
                var = i
                break
        if var is None:
            # All assigned, check all clauses
            for clause in clause_lits:
                if evaluate_clause(clause) is not True:
                    return False
            return True
        # Try True then False
        for val in (True, False):
            assignment[var] = val
            if backtrack():
                return True
            assignment[var] = None
        return False
    
    if backtrack():
        print("YES")
        print(" ".join('1' if assignment[i] else '0' for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()