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
    
    # variable assignment: 0 = unassigned, 1 = True, -1 = False
    assignment = [0] * (n + 1)
    
    # We'll implement DPLL with unit propagation and pure literal elimination.
    
    def evaluate_literal(lit, assign):
        var = abs(lit)
        val = assign[var]
        if val == 0:
            return None  # unknown
        if lit > 0:
            return val == 1
        else:
            return val == -1
    
    def propagate(clauses, assign):
        changed = True
        while changed:
            changed = False
            # unit propagation
            for clause in clauses:
                unknown = []
                satisfied = False
                for lit in clause:
                    res = evaluate_literal(lit, assign)
                    if res is True:
                        satisfied = True
                        break
                    elif res is None:
                        unknown.append(lit)
                if satisfied:
                    continue
                if len(unknown) == 0:
                    return False  # conflict
                if len(unknown) == 1:
                    lit = unknown[0]
                    var = abs(lit)
                    val = 1 if lit > 0 else -1
                    if assign[var] != 0 and assign[var] != val:
                        return False
                    if assign[var] == 0:
                        assign[var] = val
                        changed = True
            # pure literal elimination
            # find pure literals
            pos_count = {}
            neg_count = {}
            for clause in clauses:
                for lit in clause:
                    var = abs(lit)
                    if assign[var] != 0:
                        continue
                    if lit > 0:
                        pos_count[var] = pos_count.get(var, 0) + 1
                    else:
                        neg_count[var] = neg_count.get(var, 0) + 1
            for var in list(pos_count.keys()):
                if assign[var] != 0:
                    continue
                if var not in neg_count:
                    assign[var] = 1
                    changed = True
            for var in list(neg_count.keys()):
                if assign[var] != 0:
                    continue
                if var not in pos_count:
                    assign[var] = -1
                    changed = True
        return True
    
    def dpll(clauses, assign):
        # propagate
        assign_copy = assign[:]
        if not propagate(clauses, assign_copy):
            return None
        # check if all satisfied
        all_sat = True
        for clause in clauses:
            sat = False
            for lit in clause:
                res = evaluate_literal(lit, assign_copy)
                if res is True:
                    sat = True
                    break
            if not sat:
                all_sat = False
                break
        if all_sat:
            return assign_copy
        # choose unassigned variable
        var = None
        for i in range(1, n+1):
            if assign_copy[i] == 0:
                var = i
                break
        if var is None:
            return None
        # try True
        assign_copy[var] = 1
        res = dpll(clauses, assign_copy)
        if res is not None:
            return res
        # try False
        assign_copy[var] = -1
        res = dpll(clauses, assign_copy)
        if res is not None:
            return res
        return None
    
    result = dpll(clauses, assignment)
    if result is None:
        print("NO")
    else:
        print("YES")
        out = []
        for i in range(1, n+1):
            out.append('1' if result[i] == 1 else '0')
        print(' '.join(out))

if __name__ == "__main__":
    solve()