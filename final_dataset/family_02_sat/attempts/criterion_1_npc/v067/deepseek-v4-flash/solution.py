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
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        clause = []
        for v in (a, b, c):
            var = abs(v) - 1
            is_neg = v < 0
            clause.append((var, is_neg))
        clauses.append(clause)
    
    assignment = [None] * n
    
    # Watch lists for unit propagation
    # We'll implement a simple DPLL with unit propagation
    
    def propagate(assign):
        # Returns (assignment copy, conflict?) or None if conflict
        assign = assign[:]
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                # Check if clause is already satisfied
                satisfied = False
                unassigned = None
                all_false = True
                for var, is_neg in clause:
                    val = assign[var]
                    if val is None:
                        unassigned = (var, is_neg)
                    else:
                        if val == (not is_neg):
                            satisfied = True
                            break
                        # else val == is_neg -> false literal
                if satisfied:
                    continue
                if unassigned is None:
                    # conflict
                    return None
                # unit clause
                var, is_neg = unassigned
                assign[var] = not is_neg
                changed = True
        return assign
    
    def dpll(assign):
        assign = propagate(assign)
        if assign is None:
            return None
        # Check if all assigned
        if all(v is not None for v in assign):
            return assign
        # Choose unassigned variable
        var = assign.index(None)
        for val in (True, False):
            new_assign = assign[:]
            new_assign[var] = val
            res = dpll(new_assign)
            if res is not None:
                return res
        return None
    
    result = dpll(assignment)
    if result is None:
        print("NO")
    else:
        print("YES")
        print(" ".join('1' if v else '0' for v in result))

if __name__ == "__main__":
    solve()