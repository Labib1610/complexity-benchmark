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
        # Remove duplicates
        c = list(set(c))
        # If clause contains both x and -x, it's always satisfied, so we can ignore it
        tautology = False
        seen = set()
        for lit in c:
            if -lit in seen:
                tautology = True
                break
            seen.add(lit)
        if not tautology:
            clauses.append(c)

    # Fast check: WalkSAT (SLS)
    def walksat(max_tries=50, max_flips=2000, p=0.4):
        for _ in range(max_tries):
            assignment = [random.choice([-1, 1]) for _ in range(n + 1)]
            for _ in range(max_flips):
                unsat_clauses = []
                for ci, clause in enumerate(clauses):
                    satisfied = False
                    for lit in clause:
                        var = abs(lit)
                        val = 1 if lit > 0 else -1
                        if assignment[var] == val:
                            satisfied = True
                            break
                    if not satisfied:
                        unsat_clauses.append(ci)
                
                if not unsat_clauses:
                    return assignment
                
                # Pick a random unsatisfied clause
                c_idx = random.choice(unsat_clauses)
                clause = clauses[c_idx]
                
                # Greedy or random flip
                if random.random() < p:
                    lit = random.choice(clause)
                    assignment[abs(lit)] = -assignment[abs(lit)]
                else:
                    # Pick variable that minimizes number of broken clauses
                    best_var = abs(clause[0])
                    min_breaks = float('inf')
                    for lit in clause:
                        var = abs(lit)
                        # Count how many currently satisfied clauses would become unsatisfied
                        assignment[var] = -assignment[var]
                        breaks = 0
                        for c in clauses:
                            if var in [abs(l) for l in c]:
                                # check if satisfied
                                sat = any(assignment[abs(l)] == (1 if l > 0 else -1) for l in c)
                                if not sat:
                                    breaks += 1
                        assignment[var] = -assignment[var]
                        if breaks < min_breaks:
                            min_breaks = breaks
                            best_var = var
                    assignment[best_var] = -assignment[best_var]
        return None

    # DPLL solver as complete solver
    def dpll(current_clauses, assignment):
        # Unit propagation
        changed = True
        while changed:
            changed = False
            # Find unit clauses
            unit_literals = []
            for c in current_clauses:
                if len(c) == 0:
                    return None
                if len(c) == 1:
                    unit_literals.append(c[0])
            
            if unit_literals:
                for lit in unit_literals:
                    var = abs(lit)
                    val = 1 if lit > 0 else -1
                    if assignment[var] != 0 and assignment[var] != val:
                        return None
                    assignment[var] = val
                    
                    # Simplify clauses
                    new_clauses = []
                    for c in current_clauses:
                        if lit in c:
                            continue
                        if -lit in c:
                            new_c = [l for l in c if l != -lit]
                            if len(new_c) == 0:
                                return None
                            new_clauses.append(new_c)
                        else:
                            new_clauses.append(c)
                    current_clauses = new_clauses
                    changed = True
                    break

        if not current_clauses:
            return assignment

        # Jeroslow-Wang heuristic for choosing literal
        scores = {}
        for c in current_clauses:
            weight = 2 ** (-len(c))
            for lit in c:
                scores[lit] = scores.get(lit, 0) + weight

        if not scores:
            return assignment

        chosen_lit = max(scores, key=scores.get)
        chosen_var = abs(chosen_lit)
        
        # Try chosen_lit first
        for lit in [chosen_lit, -chosen_lit]:
            val = 1 if lit > 0 else -1
            new_assign = list(assignment)
            new_assign[chosen_var] = val
            new_c = []
            conflict = False
            for c in current_clauses:
                if lit in c:
                    continue
                if -lit in c:
                    rem = [l for l in c if l != -lit]
                    if len(rem) == 0:
                        conflict = True
                        break
                    new_c.append(rem)
                else:
                    new_c.append(c)
            if not conflict:
                res = dpll(new_c, new_assign)
                if res is not None:
                    return res
        return None

    # Try walksat first if clauses exist
    if not clauses:
        print("YES")
        print(" ".join(["0"] * n))
        return

    sol = walksat(max_tries=30, max_flips=1000)
    if sol is None:
        initial_assignment = [0] * (n + 1)
        sol = dpll(clauses, initial_assignment)

    if sol is None:
        print("NO")
    else:
        print("YES")
        res = []
        for i in range(1, n + 1):
            if sol[i] == 1:
                res.append("1")
            else:
                res.append("0")
        print(" ".join(res))

if __name__ == '__main__':
    solve()