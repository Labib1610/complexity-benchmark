import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    clauses = []
    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx+1])
        l3 = int(input_data[idx+2])
        idx += 3
        clauses.append((l1, l2, l3))
    
    # variable values: None = unassigned, True = primary, False = secondary
    assignment = [None] * (n + 1)
    
    def propagate(clauses, assignment):
        # returns (new_clauses, new_assignment) or None if conflict
        changed = True
        while changed:
            changed = False
            # unit propagation
            for clause in clauses[:]:
                unassigned = []
                satisfied = False
                for lit in clause:
                    var = abs(lit)
                    val = assignment[var]
                    if val is not None:
                        if (lit > 0 and val) or (lit < 0 and not val):
                            satisfied = True
                            break
                    else:
                        unassigned.append(lit)
                if satisfied:
                    clauses.remove(clause)
                    changed = True
                elif len(unassigned) == 0:
                    return None, None
                elif len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    val = lit > 0
                    if assignment[var] is not None and assignment[var] != val:
                        return None, None
                    assignment[var] = val
                    clauses.remove(clause)
                    changed = True
        return clauses, assignment
    
    def pure_literal_elimination(clauses, assignment):
        # find pure literals
        pos_count = {}
        neg_count = {}
        for clause in clauses:
            for lit in clause:
                var = abs(lit)
                if lit > 0:
                    pos_count[var] = pos_count.get(var, 0) + 1
                else:
                    neg_count[var] = neg_count.get(var, 0) + 1
        for var in range(1, n+1):
            if assignment[var] is not None:
                continue
            p = pos_count.get(var, 0)
            q = neg_count.get(var, 0)
            if p > 0 and q == 0:
                assignment[var] = True
            elif q > 0 and p == 0:
                assignment[var] = False
            else:
                continue
            # remove clauses containing this var
            new_clauses = []
            for clause in clauses:
                if any(abs(lit) == var for lit in clause):
                    continue
                new_clauses.append(clause)
            clauses = new_clauses
        return clauses, assignment
    
    def backtrack(clauses, assignment):
        clauses, assignment = propagate(clauses[:], assignment[:])
        if clauses is None:
            return None
        clauses, assignment = pure_literal_elimination(clauses, assignment)
        if not clauses:
            return assignment
        # choose a variable that appears
        var = None
        for clause in clauses:
            for lit in clause:
                v = abs(lit)
                if assignment[v] is None:
                    var = v
                    break
            if var is not None:
                break
        if var is None:
            return assignment
        # try True
        assign1 = assignment[:]
        assign1[var] = True
        res = backtrack(clauses, assign1)
        if res is not None:
            return res
        # try False
        assign2 = assignment[:]
        assign2[var] = False
        return backtrack(clauses, assign2)
    
    result = backtrack(clauses, assignment)
    if result is None:
        print("NO")
    else:
        print("YES")
        print(" ".join('1' if result[i] else '0' for i in range(1, n+1)))

if __name__ == "__main__":
    solve()