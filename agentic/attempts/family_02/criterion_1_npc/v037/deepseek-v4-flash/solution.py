import sys
sys.setrecursionlimit(1000000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    clauses = []
    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx]); l2 = int(input_data[idx+1]); l3 = int(input_data[idx+2])
        idx += 3
        clauses.append((l1, l2, l3))
    
    # DPLL solver
    def dpll(clauses, assignment):
        # Unit propagation
        changed = True
        while changed:
            changed = False
            for clause in clauses[:]:
                # Check if clause is already satisfied
                sat = False
                for lit in clause:
                    var = abs(lit)
                    val = assignment.get(var)
                    if val is not None:
                        if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                            sat = True
                            break
                    # if unassigned, can't determine
                if sat:
                    clauses.remove(clause)
                    changed = True
                    continue
                # Check if clause is unit
                unassigned = []
                for lit in clause:
                    var = abs(lit)
                    if var not in assignment:
                        unassigned.append(lit)
                if len(unassigned) == 0:
                    return None  # conflict
                elif len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    val = 1 if lit > 0 else 0
                    assignment[var] = val
                    changed = True
        if not clauses:
            return assignment
        # Choose a variable to assign
        # Pick variable from first clause
        for lit in clauses[0]:
            var = abs(lit)
            if var not in assignment:
                break
        # Try True
        assign1 = assignment.copy()
        assign1[var] = 1
        res = dpll([c[:] for c in clauses], assign1)
        if res is not None:
            return res
        # Try False
        assign2 = assignment.copy()
        assign2[var] = 0
        return dpll([c[:] for c in clauses], assign2)
    
    result = dpll(clauses, {})
    if result is None:
        print("NO")
    else:
        print("YES")
        ans = [0] * (n + 1)
        for var, val in result.items():
            if 1 <= var <= n:
                ans[var] = val
        print(' '.join(str(ans[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    solve()