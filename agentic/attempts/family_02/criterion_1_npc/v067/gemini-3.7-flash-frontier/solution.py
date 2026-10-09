import sys

def solve():
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
        # Remove duplicates in a clause
        c = list(set(c))
        # Check if clause contains both x and -x (tautology)
        tautology = False
        for lit in c:
            if -lit in c:
                tautology = True
                break
        if not tautology:
            clauses.append(c)
            
    assignment = {}

    def get_clause_status(clause):
        # returns (status, unassigned_lits)
        # status: True if satisfied, False if conflict (all false), None if unresolved
        unassigned = []
        for lit in clause:
            var = abs(lit)
            val = assignment.get(var)
            if val is not None:
                if (val and lit > 0) or (not val and lit < 0):
                    return True, []
            else:
                unassigned.append(lit)
        if not unassigned:
            return False, []
        return None, unassigned

    def unit_propagate():
        while True:
            unit_found = False
            for clause in clauses:
                sat, unassigned = get_clause_status(clause)
                if sat is True:
                    continue
                if sat is False:
                    return False
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    val = lit > 0
                    assignment[var] = val
                    unit_found = True
                    break
            if not unit_found:
                break
        return True

    def dpll():
        # Unit propagate
        saved_assignment = assignment.copy()
        if not unit_propagate():
            assignment.clear()
            assignment.update(saved_assignment)
            return False

        # Check if all clauses are satisfied
        all_sat = True
        unsat_clauses = []
        for clause in clauses:
            sat, unassigned = get_clause_status(clause)
            if sat is False:
                assignment.clear()
                assignment.update(saved_assignment)
                return False
            if sat is not True:
                all_sat = False
                unsat_clauses.append(unassigned)

        if all_sat:
            return True

        # Jeroslow-Wang heuristic for branching
        score = {}
        for unassigned in unsat_clauses:
            weight = 2.0 ** (-len(unassigned))
            for lit in unassigned:
                score[lit] = score.get(lit, 0.0) + weight

        best_lit = max(score.keys(), key=lambda l: score[l])
        best_var = abs(best_lit)
        best_val = best_lit > 0

        # Try best_val first
        assignment[best_var] = best_val
        if dpll():
            return True

        # Backtrack and try opposite
        assignment.clear()
        assignment.update(saved_assignment)
        assignment[best_var] = not best_val
        if dpll():
            return True

        assignment.clear()
        assignment.update(saved_assignment)
        return False

    if dpll():
        print("YES")
        res = []
        for i in range(1, n + 1):
            val = assignment.get(i, False)
            res.append(1 if val else 0)
        print(*(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()