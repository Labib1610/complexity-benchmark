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
    
    # Variable assignment: 0 = unassigned, 1 = True, -1 = False
    assignment = [0] * (n + 1)
    
    def is_satisfied(clause):
        for lit in clause:
            var = abs(lit)
            val = assignment[var]
            if val != 0:
                if (lit > 0 and val == 1) or (lit < 0 and val == -1):
                    return True
        return False
    
    def unit_propagate():
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                unassigned = []
                satisfied = False
                for lit in clause:
                    var = abs(lit)
                    val = assignment[var]
                    if val != 0:
                        if (lit > 0 and val == 1) or (lit < 0 and val == -1):
                            satisfied = True
                            break
                    else:
                        unassigned.append(lit)
                if satisfied:
                    continue
                if len(unassigned) == 0:
                    return False  # conflict
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    val = 1 if lit > 0 else -1
                    if assignment[var] == 0:
                        assignment[var] = val
                        changed = True
                    elif assignment[var] != val:
                        return False
        return True
    
    def backtrack():
        # Unit propagation
        if not unit_propagate():
            return False
        
        # Find unassigned variable
        var = -1
        for i in range(1, n + 1):
            if assignment[i] == 0:
                var = i
                break
        if var == -1:
            return True  # all assigned
        
        # Try True
        assignment[var] = 1
        saved = assignment[:]
        if backtrack():
            return True
        assignment[:] = saved
        
        # Try False
        assignment[var] = -1
        saved = assignment[:]
        if backtrack():
            return True
        assignment[:] = saved
        
        assignment[var] = 0
        return False
    
    if backtrack():
        print("YES")
        res = []
        for i in range(1, n + 1):
            res.append('1' if assignment[i] == 1 else '0')
        print(' '.join(res))
    else:
        print("NO")

if __name__ == "__main__":
    solve()