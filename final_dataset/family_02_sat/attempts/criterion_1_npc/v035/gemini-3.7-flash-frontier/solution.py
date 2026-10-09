import sys
import random

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
        # Simplify clause: remove duplicate literals
        c = list(set(c))
        # If both x and -x in clause, it's always true, so we can ignore it
        has_tautology = False
        for lit in c:
            if -lit in c:
                has_tautology = True
                break
        if not has_tautology:
            clauses.append(c)

    # Fast WalkSAT attempt
    def walksat():
        for restart in range(10):
            assignment = [random.choice([0, 1]) for _ in range(n + 1)]
            
            for step in range(1000):
                unsat = []
                for i, c in enumerate(clauses):
                    sat = False
                    for lit in c:
                        val = assignment[abs(lit)]
                        if lit > 0 and val == 1:
                            sat = True
                            break
                        elif lit < 0 and val == 0:
                            sat = True
                            break
                    if not sat:
                        unsat.append(c)
                
                if not unsat:
                    return assignment[1:]
                
                c = random.choice(unsat)
                if random.random() < 0.4:
                    var = abs(random.choice(c))
                else:
                    best_var = abs(c[0])
                    min_unsat = m + 1
                    for lit in c:
                        v = abs(lit)
                        assignment[v] ^= 1
                        # count unsat
                        cnt = 0
                        for cl in clauses:
                            sat = False
                            for l in cl:
                                val = assignment[abs(l)]
                                if (l > 0 and val == 1) or (l < 0 and val == 0):
                                    sat = True
                                    break
                            if not sat:
                                cnt += 1
                        assignment[v] ^= 1
                        if cnt < min_unsat:
                            min_unsat = cnt
                            best_var = v
                    var = best_var
                assignment[var] ^= 1
        return None

    # DPLL solver
    def dpll():
        # assignment: array of size n+1, -1: unassigned, 0: false, 1: true
        assignment = [-1] * (n + 1)
        
        def unit_propagate(assign):
            while True:
                unit_found = False
                for c in clauses:
                    unassigned_lit = None
                    is_sat = False
                    unassigned_count = 0
                    for lit in c:
                        v = abs(lit)
                        val = assign[v]
                        if val == -1:
                            unassigned_count += 1
                            unassigned_lit = lit
                        elif (lit > 0 and val == 1) or (lit < 0 and val == 0):
                            is_sat = True
                            break
                    if is_sat:
                        continue
                    if unassigned_count == 0:
                        return False, None  # Conflict
                    if unassigned_count == 1:
                        v = abs(unassigned_lit)
                        target_val = 1 if unassigned_lit > 0 else 0
                        if assign[v] != -1:
                            if assign[v] != target_val:
                                return False, None
                        else:
                            assign[v] = target_val
                            unit_found = True
                if not unit_found:
                    break
            return True, assign

        def solve_rec(assign):
            assign_copy = list(assign)
            ok, assign_copy = unit_propagate(assign_copy)
            if not ok:
                return None
            
            # Check if all clauses satisfied
            all_sat = True
            for c in clauses:
                is_sat = False
                for lit in c:
                    v = abs(lit)
                    val = assign_copy[v]
                    if val != -1:
                        if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                            is_sat = True
                            break
                if not is_sat:
                    all_sat = False
                    break
            
            if all_sat:
                # Any remaining unassigned variable can be set to 0
                for i in range(1, n + 1):
                    if assign_copy[i] == -1:
                        assign_copy[i] = 0
                return assign_copy[1:]

            # Jeroslow-Wang heuristic for branching variable
            scores = [0.0] * (n + 1)
            pos_scores = [0.0] * (n + 1)
            neg_scores = [0.0] * (n + 1)
            
            for c in clauses:
                is_sat = False
                unassigned = []
                for lit in c:
                    v = abs(lit)
                    val = assign_copy[v]
                    if val != -1:
                        if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                            is_sat = True
                            break
                    else:
                        unassigned.append(lit)
                if not is_sat:
                    weight = 2.0 ** (-len(unassigned))
                    for lit in unassigned:
                        v = abs(lit)
                        if lit > 0:
                            pos_scores[v] += weight
                        else:
                            neg_scores[v] += weight
                        scores[v] += weight
            
            best_var = -1
            best_score = -1.0
            for v in range(1, n + 1):
                if assign_copy[v] == -1 and scores[v] > best_score:
                    best_score = scores[v]
                    best_var = v
            
            if best_var == -1:
                for v in range(1, n + 1):
                    if assign_copy[v] == -1:
                        assign_copy[v] = 0
                return assign_copy[1:]
            
            first_val = 1 if pos_scores[best_var] >= neg_scores[best_var] else 0
            
            assign_copy[best_var] = first_val
            res = solve_rec(assign_copy)
            if res is not None:
                return res
            
            assign_copy[best_var] = 1 - first_val
            res = solve_rec(assign_copy)
            return res

        return solve_rec(assignment)

    # Try WalkSAT first
    sol = walksat()
    if sol is not None:
        print("YES")
        print(*(sol))
        return

    # Fall back to DPLL
    sol = dpll()
    if sol is not None:
        print("YES")
        print(*(sol))
    else:
        print("NO")

if __name__ == '__main__':
    solve()