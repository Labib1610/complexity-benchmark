import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    clauses = []
    idx = 2
    for _ in range(m):
        c = [int(input_data[idx]), int(input_data[idx + 1]), int(input_data[idx + 2])]
        idx += 3
        # Remove duplicate literals in a clause
        c = list(set(c))
        # If clause has x and -x, it's trivially satisfied, ignore it
        has_opposite = False
        for lit in c:
            if -lit in c:
                has_opposite = True
                break
        if not has_opposite:
            clauses.append(c)

    assignment = [None] * (n + 1)

    def dpll(assigned_count):
        # Unit propagation
        trail = []
        while True:
            unit_found = False
            for c in clauses:
                unassigned_lits = []
                satisfied = False
                for lit in c:
                    var = abs(lit)
                    val = assignment[var]
                    if val is not None:
                        if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                            satisfied = True
                            break
                    else:
                        unassigned_lits.append(lit)
                if satisfied:
                    continue
                if len(unassigned_lits) == 0:
                    # Conflict
                    for var in trail:
                        assignment[var] = None
                    return False
                if len(unassigned_lits) == 1:
                    unit_lit = unassigned_lits[0]
                    var = abs(unit_lit)
                    val = 1 if unit_lit > 0 else 0
                    if assignment[var] is None:
                        assignment[var] = val
                        trail.append(var)
                        unit_found = True
                    elif assignment[var] != val:
                        # Conflict
                        for v in trail:
                            assignment[v] = None
                        return False
            if not unit_found:
                break

        # Check if all satisfied
        all_satisfied = True
        weights_pos = [0.0] * (n + 1)
        weights_neg = [0.0] * (n + 1)
        
        for c in clauses:
            unassigned_lits = []
            satisfied = False
            for lit in c:
                var = abs(lit)
                val = assignment[var]
                if val is not None:
                    if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                        satisfied = True
                        break
                else:
                    unassigned_lits.append(lit)
            if satisfied:
                continue
            all_satisfied = False
            if len(unassigned_lits) == 0:
                for var in trail:
                    assignment[var] = None
                return False
            
            # Jeroslow-Wang weights
            w = 2.0 ** (-len(unassigned_lits))
            for lit in unassigned_lits:
                var = abs(lit)
                if lit > 0:
                    weights_pos[var] += w
                else:
                    weights_neg[var] += w

        if all_satisfied:
            return True

        # Choose branching variable using Jeroslow-Wang heuristic
        best_var = -1
        max_weight = -1.0
        for var in range(1, n + 1):
            if assignment[var] is None:
                total_w = weights_pos[var] + weights_neg[var]
                if total_w > max_weight:
                    max_weight = total_w
                    best_var = var

        if best_var == -1:
            return True

        # Branch
        first_val = 1 if weights_pos[best_var] >= weights_neg[best_var] else 0
        second_val = 1 - first_val

        assignment[best_var] = first_val
        if dpll(assigned_count + 1 + len(trail)):
            return True

        assignment[best_var] = second_val
        if dpll(assigned_count + 1 + len(trail)):
            return True

        assignment[best_var] = None
        for var in trail:
            assignment[var] = None
        return False

    if dpll(0):
        # Fill any remaining unassigned variables with 0
        for i in range(1, n + 1):
            if assignment[i] is None:
                assignment[i] = 0
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()