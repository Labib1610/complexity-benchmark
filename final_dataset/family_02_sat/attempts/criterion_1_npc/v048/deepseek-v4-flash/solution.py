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
        c1 = int(next(it))
        c2 = int(next(it))
        c3 = int(next(it))
        clauses.append((c1, c2, c3))
    
    # Convert to 0-indexed variables: positive x -> var, negative x -> ~var
    # We'll use integers: var index 0..n-1, literal = 2*var + (0 for neg, 1 for pos)
    def lit_to_int(lit):
        var = abs(lit) - 1
        if lit > 0:
            return 2 * var + 1
        else:
            return 2 * var
    
    clause_list = []
    for c1, c2, c3 in clauses:
        clause_list.append([lit_to_int(c1), lit_to_int(c2), lit_to_int(c3)])
    
    assignment = [None] * n  # None = unassigned, True/False = value
    
    # DPLL with unit propagation and pure literal elimination
    def dpll(clauses, assignment):
        # Unit propagation
        changed = True
        while changed:
            changed = False
            # Check for empty clause
            for clause in clauses:
                if all(assignment[lit // 2] is not None and
                       (assignment[lit // 2] == (lit % 2 == 1)) == False for lit in clause):
                    # all literals false
                    return None
            # Find unit clauses
            for clause in clauses:
                unassigned = []
                satisfied = False
                for lit in clause:
                    var = lit // 2
                    val = assignment[var]
                    if val is not None:
                        if (lit % 2 == 1) == val:
                            satisfied = True
                            break
                    else:
                        unassigned.append(lit)
                if satisfied:
                    continue
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = lit // 2
                    val = (lit % 2 == 1)
                    if assignment[var] is None:
                        assignment[var] = val
                        changed = True
                    elif assignment[var] != val:
                        return None
        # Pure literal elimination
        pure = {}
        for clause in clauses:
            for lit in clause:
                var = lit // 2
                if assignment[var] is not None:
                    continue
                sign = lit % 2
                if var not in pure:
                    pure[var] = sign
                elif pure[var] != sign:
                    pure[var] = -1  # not pure
        for var, sign in pure.items():
            if sign != -1 and assignment[var] is None:
                assignment[var] = (sign == 1)
        
        # Check if all clauses satisfied
        all_sat = True
        for clause in clauses:
            sat = False
            for lit in clause:
                var = lit // 2
                val = assignment[var]
                if val is not None and (lit % 2 == 1) == val:
                    sat = True
                    break
            if not sat:
                all_sat = False
                break
        if all_sat:
            return assignment
        
        # Choose unassigned variable
        for var in range(n):
            if assignment[var] is None:
                # Try True
                assignment[var] = True
                res = dpll(clauses, assignment)
                if res is not None:
                    return res
                # Try False
                assignment[var] = False
                res = dpll(clauses, assignment)
                if res is not None:
                    return res
                assignment[var] = None
                return None
        return None
    
    result = dpll(clause_list, assignment)
    if result is None:
        print("NO")
    else:
        print("YES")
        print(" ".join("1" if result[i] else "0" for i in range(n)))

if __name__ == "__main__":
    solve()