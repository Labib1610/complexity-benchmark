import sys

def main():
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
        # encode literals
        def enc(lit):
            var = abs(lit) - 1
            return var * 2 if lit > 0 else var * 2 + 1
        clauses.append([enc(l1), enc(l2), enc(l3)])
    
    # DPLL solver
    # variable count = n
    # literal index: 2*var for true, 2*var+1 for false
    # negation: lit ^ 1
    
    def neg(lit):
        return lit ^ 1
    
    def solve():
        # assignment: None = unassigned, True/False
        assignment = [None] * n
        
        def dpll(clauses, assignment):
            # unit propagation
            changed = True
            while changed:
                changed = False
                # find unit clauses
                for clause in clauses:
                    unassigned = []
                    satisfied = False
                    for lit in clause:
                        var = lit // 2
                        val = lit % 2 == 0  # True if lit is positive
                        if assignment[var] is None:
                            unassigned.append(lit)
                        elif assignment[var] == val:
                            satisfied = True
                            break
                    if satisfied:
                        continue
                    if len(unassigned) == 0:
                        return None  # conflict
                    if len(unassigned) == 1:
                        lit = unassigned[0]
                        var = lit // 2
                        val = lit % 2 == 0
                        assignment[var] = val
                        changed = True
            # pure literal elimination
            # (optional, but can speed up)
            # check for conflict
            for clause in clauses:
                satisfied = False
                for lit in clause:
                    var = lit // 2
                    val = lit % 2 == 0
                    if assignment[var] is not None and assignment[var] == val:
                        satisfied = True
                        break
                if not satisfied:
                    # all assigned and none match
                    all_assigned = all(assignment[lit//2] is not None for lit in clause)
                    if all_assigned:
                        return None
            # choose unassigned variable
            for i in range(n):
                if assignment[i] is None:
                    # try True
                    assign_copy = assignment[:]
                    assign_copy[i] = True
                    res = dpll(clauses, assign_copy)
                    if res is not None:
                        return res
                    # try False
                    assign_copy = assignment[:]
                    assign_copy[i] = False
                    res = dpll(clauses, assign_copy)
                    if res is not None:
                        return res
                    return None
            # all assigned
            return assignment
        
        return dpll(clauses, assignment)
    
    result = solve()
    if result is None:
        print("NO")
    else:
        print("YES")
        print(' '.join('1' if v else '0' for v in result))

if __name__ == "__main__":
    main()