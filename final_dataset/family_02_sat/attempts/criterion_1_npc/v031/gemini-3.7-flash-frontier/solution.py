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
        c = [int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])]
        idx += 3
        # Simplify clause: remove duplicates, check for tautologies
        c_set = set(c)
        tautology = False
        for lit in c_set:
            if -lit in c_set:
                tautology = True
                break
        if not tautology:
            clauses.append(list(c_set))
            
    # Try WalkSAT first
    import random
    
    def try_walksat(max_flips=100000, p=0.4):
        assignment = [random.choice([0, 1]) for _ in range(n + 1)]
        
        for _ in range(max_flips):
            unsat = []
            for i, c in enumerate(clauses):
                satisfied = False
                for lit in c:
                    var = abs(lit)
                    val = assignment[var]
                    if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                        satisfied = True
                        break
                if not satisfied:
                    unsat.append(i)
            
            if not unsat:
                return assignment
            
            clause_idx = random.choice(unsat)
            c = clauses[clause_idx]
            
            if random.random() < p:
                lit = random.choice(c)
                var = abs(lit)
            else:
                # Greedy choice: minimize number of broken clauses
                best_var = abs(c[0])
                min_broken = float('inf')
                for lit in c:
                    var = abs(lit)
                    assignment[var] ^= 1
                    broken = 0
                    for ci in clauses:
                        sat = False
                        for l in ci:
                            v = abs(l)
                            if (l > 0 and assignment[v] == 1) or (l < 0 and assignment[v] == 0):
                                sat = True
                                break
                        if not sat:
                            broken += 1
                    assignment[var] ^= 1
                    if broken < min_broken:
                        min_broken = broken
                        best_var = var
                var = best_var
            
            assignment[var] ^= 1
            
        return None

    # Run quick WalkSAT
    walk_res = try_walksat(max_flips=10000)
    if walk_res is not None:
        print("YES")
        print(*(walk_res[i] for i in range(1, n + 1)))
        return

    # DPLL Solver
    def dpll(assignment, current_clauses):
        # Unit propagation
        while True:
            unit_literals = []
            for c in current_clauses:
                if len(c) == 0:
                    return None
                if len(c) == 1:
                    unit_literals.append(c[0])
            
            if not unit_literals:
                break
            
            # Pick a unit literal
            unit = unit_literals[0]
            var = abs(unit)
            val = 1 if unit > 0 else 0
            
            if var in assignment and assignment[var] != val:
                return None
            assignment[var] = val
            
            new_clauses = []
            for c in current_clauses:
                if unit in c:
                    continue
                if -unit in c:
                    new_c = [l for l in c if l != -unit]
                    new_clauses.append(new_c)
                else:
                    new_clauses.append(c)
            current_clauses = new_clauses

        if not current_clauses:
            return assignment

        # Jeroslow-Wang branching heuristic
        scores = {}
        for c in current_clauses:
            weight = 2.0 ** (-len(c))
            for lit in c:
                scores[lit] = scores.get(lit, 0.0) + weight

        # Choose literal with maximum score
        best_lit = None
        max_score = -1
        for lit, score in scores.items():
            opposite_score = scores.get(-lit, 0.0)
            total_score = score + opposite_score
            if total_score > max_score:
                max_score = total_score
                best_lit = lit if score >= opposite_score else -lit

        var = abs(best_lit)
        for chosen_lit in [best_lit, -best_lit]:
            val = 1 if chosen_lit > 0 else 0
            new_assign = assignment.copy()
            new_assign[var] = val
            
            new_clauses = []
            for c in current_clauses:
                if chosen_lit in c:
                    continue
                if -chosen_lit in c:
                    new_clauses.append([l for l in c if l != -chosen_lit])
                else:
                    new_clauses.append(c)
                    
            res = dpll(new_assign, new_clauses)
            if res is not None:
                return res

        return None

    res = dpll({}, clauses)
    if res is None:
        print("NO")
    else:
        print("YES")
        ans = [res.get(i, 0) for i in range(1, n + 1)]
        print(*ans)

if __name__ == '__main__':
    solve()