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
    
    assignment = [None] * (n + 1)  # None = unassigned, True = 1, False = 0
    
    def clause_satisfied(clause):
        for lit in clause:
            var = abs(lit)
            val = assignment[var]
            if val is not None:
                if lit > 0 and val:
                    return True
                if lit < 0 and not val:
                    return True
        return False
    
    def clause_unsat(clause):
        # returns True if all literals are assigned and false
        for lit in clause:
            var = abs(lit)
            val = assignment[var]
            if val is None:
                return False
            if lit > 0 and val:
                return False
            if lit < 0 and not val:
                return False
        return True
    
    def propagate():
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                if clause_satisfied(clause):
                    continue
                unassigned = []
                for lit in clause:
                    var = abs(lit)
                    if assignment[var] is None:
                        unassigned.append(lit)
                if len(unassigned) == 0:
                    return False  # conflict
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    val = lit > 0
                    assignment[var] = val
                    changed = True
        return True
    
    def backtrack():
        if not propagate():
            return False
        # find unassigned variable
        for i in range(1, n + 1):
            if assignment[i] is None:
                # try True
                assignment[i] = True
                if backtrack():
                    return True
                assignment[i] = False
                if backtrack():
                    return True
                assignment[i] = None
                return False
        # all assigned, check all clauses
        for clause in clauses:
            if not clause_satisfied(clause):
                return False
        return True
    
    if backtrack():
        print("YES")
        print(" ".join("1" if assignment[i] else "0" for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()