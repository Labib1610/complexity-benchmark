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
    
    # Convert clause to list of (var, value) where value True means var is True
    # For literal x: (var, True) means x is True
    # For literal -x: (var, False) means x is False
    clause_list = []
    for c in clauses:
        clause = []
        for lit in c:
            var = abs(lit)
            val = lit > 0
            clause.append((var, val))
        clause_list.append(clause)
    
    # Unit propagation and pure literal elimination
    def propagate():
        changed = True
        while changed:
            changed = False
            # Unit propagation
            for clause in clause_list:
                unassigned = []
                satisfied = False
                for var, val in clause:
                    if assignment[var] == 0:
                        unassigned.append((var, val))
                    elif (assignment[var] == 1) == val:
                        satisfied = True
                        break
                if satisfied:
                    continue
                if len(unassigned) == 0:
                    return False
                if len(unassigned) == 1:
                    var, val = unassigned[0]
                    if assignment[var] == 0:
                        assignment[var] = 1 if val else -1
                        changed = True
                    else:
                        # already assigned but not satisfied -> contradiction
                        return False
            # Pure literal elimination
            # Count occurrences of each literal
            pos_count = [0] * (n + 1)
            neg_count = [0] * (n + 1)
            for clause in clause_list:
                for var, val in clause:
                    if assignment[var] == 0:
                        if val:
                            pos_count[var] += 1
                        else:
                            neg_count[var] += 1
            for var in range(1, n + 1):
                if assignment[var] == 0:
                    if pos_count[var] > 0 and neg_count[var] == 0:
                        assignment[var] = 1
                        changed = True
                    elif neg_count[var] > 0 and pos_count[var] == 0:
                        assignment[var] = -1
                        changed = True
        return True
    
    def backtrack():
        # Find first unassigned variable
        var = -1
        for i in range(1, n + 1):
            if assignment[i] == 0:
                var = i
                break
        if var == -1:
            return True
        
        # Try True
        assignment[var] = 1
        saved = assignment[:]
        if propagate():
            if backtrack():
                return True
        assignment[:] = saved
        
        # Try False
        assignment[var] = -1
        saved = assignment[:]
        if propagate():
            if backtrack():
                return True
        assignment[:] = saved
        
        assignment[var] = 0
        return False
    
    if not propagate():
        print("NO")
        return
    if backtrack():
        print("YES")
        print(' '.join('1' if assignment[i] == 1 else '0' for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()