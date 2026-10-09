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
        c1 = int(input_data[idx])
        c2 = int(input_data[idx+1])
        c3 = int(input_data[idx+2])
        idx += 3
        # Remove duplicates within clause
        lits = list(set([c1, c2, c3]))
        # If clause contains both x and -x, it's always satisfied, skip it
        has_tautology = False
        lit_set = set(lits)
        for l in lits:
            if -l in lit_set:
                has_tautology = True
                break
        if not has_tautology:
            clauses.append(lits)

    # WalkSAT
    def walksat(max_restarts=50, max_flips=10000):
        if not clauses:
            return [0] * n

        num_clauses = len(clauses)
        
        # Precompute which clauses contain which literals
        pos_in = [[] for _ in range(n + 1)]
        neg_in = [[] for _ in range(n + 1)]
        for ci, c in enumerate(clauses):
            for l in c:
                if l > 0:
                    pos_in[l].append(ci)
                else:
                    neg_in[-l].append(ci)

        for _ in range(max_restarts):
            # random assignment: 1..n -> 0 or 1
            assign = [random.randint(0, 1) for _ in range(n + 1)]
            
            # Count satisfied literals in each clause
            num_true = [0] * num_clauses
            unsat_clauses = []
            clause_unsat_idx = [-1] * num_clauses
            
            for ci, c in enumerate(clauses):
                cnt = 0
                for l in c:
                    v = l if l > 0 else -l
                    if (l > 0 and assign[v] == 1) or (l < 0 and assign[v] == 0):
                        cnt += 1
                num_true[ci] = cnt
                if cnt == 0:
                    clause_unsat_idx[ci] = len(unsat_clauses)
                    unsat_clauses.append(ci)

            if not unsat_clauses:
                return assign[1:]

            for _ in range(max_flips):
                ci = random.choice(unsat_clauses)
                c = clauses[ci]
                
                # Choose variable to flip
                if random.random() < 0.4:
                    flip_lit = random.choice(c)
                    flip_v = abs(flip_lit)
                else:
                    best_v = abs(c[0])
                    min_break = 1000000
                    for l in c:
                        v = abs(l)
                        # calculate break count (clauses that become unsatisfied)
                        # if assign[v] == 1, flipping will make true literals in pos_in[v] decrease by 1
                        make_false_clauses = pos_in[v] if assign[v] == 1 else neg_in[v]
                        break_cnt = sum(1 for c_idx in make_false_clauses if num_true[c_idx] == 1)
                        if break_cnt < min_break:
                            min_break = break_cnt
                            best_v = v
                    flip_v = best_v

                # Flip assign[flip_v]
                old_val = assign[flip_v]
                assign[flip_v] = 1 - old_val
                
                make_true_clauses = pos_in[flip_v] if assign[flip_v] == 1 else neg_in[flip_v]
                make_false_clauses = neg_in[flip_v] if assign[flip_v] == 1 else pos_in[flip_v]
                
                for c_idx in make_true_clauses:
                    if num_true[c_idx] == 0:
                        # remove from unsat_clauses
                        pos = clause_unsat_idx[c_idx]
                        last_c = unsat_clauses[-1]
                        unsat_clauses[pos] = last_c
                        clause_unsat_idx[last_c] = pos
                        unsat_clauses.pop()
                        clause_unsat_idx[c_idx] = -1
                    num_true[c_idx] += 1
                    
                for c_idx in make_false_clauses:
                    num_true[c_idx] -= 1
                    if num_true[c_idx] == 0:
                        # add to unsat_clauses
                        clause_unsat_idx[c_idx] = len(unsat_clauses)
                        unsat_clauses.append(c_idx)

                if not unsat_clauses:
                    return assign[1:]
        return None

    # DPLL solver as fallback (also proves UNSAT)
    def dpll_solve():
        # assignment: array of size n+1, values: -1 (unassigned), 0, 1
        assign = [-1] * (n + 1)

        def unit_propagate(cur_clauses, cur_assign):
            while True:
                unit_clause = None
                for c in cur_clauses:
                    unresolved = []
                    sat = False
                    for l in c:
                        v = abs(l)
                        val = cur_assign[v]
                        if val != -1:
                            if (l > 0 and val == 1) or (l < 0 and val == 0):
                                sat = True
                                break
                        else:
                            unresolved.append(l)
                    if sat:
                        continue
                    if len(unresolved) == 0:
                        return False, cur_clauses # conflict
                    if len(unresolved) == 1:
                        unit_clause = unresolved[0]
                        break
                
                if unit_clause is None:
                    break
                
                v = abs(unit_clause)
                val = 1 if unit_clause > 0 else 0
                if cur_assign[v] != -1 and cur_assign[v] != val:
                    return False, cur_clauses
                cur_assign[v] = val

            return True, cur_clauses

        def backtrack(cur_assign):
            # simplify & check
            new_assign = list(cur_assign)
            ok, _ = unit_propagate(clauses, new_assign)
            if not ok:
                return None
            
            # Check if all satisfied
            all_sat = True
            unassigned_counts = {}
            for c in clauses:
                sat = False
                unres = []
                for l in c:
                    v = abs(l)
                    val = new_assign[v]
                    if val != -1:
                        if (l > 0 and val == 1) or (l < 0 and val == 0):
                            sat = True
                            break
                    else:
                        unres.append(l)
                if not sat:
                    all_sat = False
                    for l in unres:
                        v = abs(l)
                        unassigned_counts[v] = unassigned_counts.get(v, 0) + 1

            if all_sat:
                return [1 if x == 1 else 0 for x in new_assign[1:]]

            # Choose variable with most occurrences in unsatisfied clauses (DLCS / MOM)
            best_var = max(unassigned_counts, key=unassigned_counts.get)

            for val in [1, 0]:
                new_assign[best_var] = val
                res = backtrack(new_assign)
                if res is not None:
                    return res
                new_assign[best_var] = -1

            return None

        return backtrack(assign)

    res = walksat(max_restarts=40, max_flips=5000)
    if res is not None:
        print("YES")
        print(*(res))
        return

    res = dpll_solve()
    if res is not None:
        print("YES")
        print(*(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()