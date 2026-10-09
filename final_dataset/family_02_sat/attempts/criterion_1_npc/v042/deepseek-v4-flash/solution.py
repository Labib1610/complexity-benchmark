import sys
sys.setrecursionlimit(10000)

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
    
    def propagate(assignment):
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                unassigned = []
                satisfied = False
                for lit in clause:
                    var = abs(lit)
                    val = assignment[var]
                    if val == 0:
                        unassigned.append(lit)
                    elif (lit > 0 and val == 1) or (lit < 0 and val == -1):
                        satisfied = True
                        break
                if satisfied:
                    continue
                if len(unassigned) == 0:
                    return False
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    if lit > 0:
                        assignment[var] = 1
                    else:
                        assignment[var] = -1
                    changed = True
        return True
    
    def backtrack(assignment):
        # Propagate
        if not propagate(assignment):
            return False
        
        # Check if all clauses satisfied
        all_satisfied = True
        for clause in clauses:
            sat = False
            for lit in clause:
                var = abs(lit)
                val = assignment[var]
                if val == 0:
                    all_satisfied = False
                elif (lit > 0 and val == 1) or (lit < 0 and val == -1):
                    sat = True
                    break
            if not sat:
                return False
        if all_satisfied:
            return True
        
        # Choose an unassigned variable
        var = None
        for i in range(1, n + 1):
            if assignment[i] == 0:
                var = i
                break
        if var is None:
            return True
        
        # Try True
        assignment[var] = 1
        if backtrack(assignment):
            return True
        assignment[var] = -1
        if backtrack(assignment):
            return True
        assignment[var] = 0
        return False
    
    if backtrack(assignment):
        print("YES")
        res = []
        for i in range(1, n + 1):
            if assignment[i] == 1:
                res.append("1")
            else:
                res.append("0")
        print(" ".join(res))
    else:
        print("NO")

if __name__ == "__main__":
    solve()