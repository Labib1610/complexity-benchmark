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
        # Remove duplicates within clause
        c = list(set(c))
        # If clause contains both x and -x, it's trivially satisfied, ignore
        has_tautology = False
        for lit in c:
            if -lit in c:
                has_tautology = True
                break
        if not has_tautology:
            clauses.append(c)

    # Fast WalkSAT first for satisfiable instances
    import random
    import time
    start_time = time.time()

    def walksat(max_flips=100000, p=0.4):
        assignment = [random.choice([-1, 1]) for _ in range(n + 1)]
        for _ in range(max_flips):
            unsat_clauses = []
            for i, cl in enumerate(clauses):
                sat = False
                for lit in cl:
                    var = abs(lit)
                    val = 1 if lit > 0 else -1
                    if assignment[var] == val:
                        sat = True
                        break
                if not sat:
                    unsat_clauses.append(cl)
            
            if not unsat_clauses:
                return assignment
            
            cl = random.choice(unsat_clauses)
            if random.random() < p:
                var = abs(random.choice(cl))
            else:
                # Find variable that minimizes unsat clauses when flipped
                best_var = abs(cl[0])
                best_breaks = float('inf')
                for lit in cl:
                    v = abs(lit)
                    # Count breaks
                    assignment[v] = -assignment[v]
                    breaks = 0
                    for c_check in clauses:
                        sat = False
                        for l in c_check:
                            var_c = abs(l)
                            val_c = 1 if l > 0 else -1
                            if assignment[var_c] == val_c:
                                sat = True
                                break
                        if not sat:
                            breaks += 1
                    assignment[v] = -assignment[v]
                    if breaks < best_breaks:
                        best_breaks = breaks
                        best_var = v
                var = best_var
            assignment[var] = -assignment[var]
        return None

    # Run a few tries of WalkSAT
    for _ in range(5):
        res = walksat(max_flips=4000)
        if res is not None:
            print("YES")
            ans = [1 if res[i] == 1 else 0 for i in range(1, n + 1)]
            print(*(ans))
            return
        if time.time() - start_time > 0.4:
            break

    # DPLL with Jeroslow-Wang heuristic
    def dpll(clauses_current, assignment):
        # Unit propagation
        while True:
            unit_clauses = [c for c in clauses_current if len(c) == 1]
            if not unit_clauses:
                break
            unit_lit = unit_clauses[0][0]
            var = abs(unit_lit)
            val = 1 if unit_lit > 0 else -1
            if var in assignment:
                if assignment[var] != val:
                    return None
            else:
                assignment[var] = val
            
            new_clauses = []
            for c in clauses_current:
                if unit_lit in c:
                    continue
                if -unit_lit in c:
                    nc = [l for l in c if l != -unit_lit]
                    if not nc:
                        return None
                    new_clauses.append(nc)
                else:
                    new_clauses.append(c)
            clauses_current = new_clauses

        if not clauses_current:
            return assignment

        # Jeroslow-Wang 2-sided heuristic
        weights = {}
        for c in clauses_current:
            w = 2.0 ** (-len(c))
            for lit in c:
                weights[lit] = weights.get(lit, 0.0) + w

        # Pick literal with highest combined weight
        best_var = None
        best_score = -1
        for var in range(1, n + 1):
            if var not in assignment:
                pos_w = weights.get(var, 0.0)
                neg_w = weights.get(-var, 0.0)
                score = pos_w + neg_w
                if score > best_score:
                    best_score = score
                    best_var = var

        if best_var is None:
            return assignment

        first_val = 1 if weights.get(best_var, 0.0) >= weights.get(-best_var, 0.0) else -1

        for val in [first_val, -first_val]:
            lit = best_var if val == 1 else -best_var
            new_assign = dict(assignment)
            new_assign[best_var] = val
            new_clauses = []
            conflict = False
            for c in clauses_current:
                if lit in c:
                    continue
                if -lit in c:
                    nc = [l for l in c if l != -lit]
                    if not nc:
                        conflict = True
                        break
                    new_clauses.append(nc)
                else:
                    new_clauses.append(c)
            if conflict:
                continue
            res = dpll(new_clauses, new_assign)
            if res is not None:
                return res

        return None

    res = dpll(clauses, {})
    if res is None:
        print("NO")
    else:
        print("YES")
        ans = [1 if res.get(i, 1) == 1 else 0 for i in range(1, n + 1)]
        print(*(ans))

if __name__ == '__main__':
    solve()