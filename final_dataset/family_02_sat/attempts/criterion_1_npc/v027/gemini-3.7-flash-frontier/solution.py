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
        # Simplify clause (remove duplicates)
        c_set = set(c)
        # If clause contains both x and -x, it is trivially satisfied
        tautology = False
        for lit in c_set:
            if -lit in c_set:
                tautology = True
                break
        if not tautology:
            clauses.append(list(c_set))
            
    # DPLL Implementation
    # Assignment: None (unassigned), True, False
    assignment = [None] * (n + 1)
    
    def get_lit_val(lit):
        var = abs(lit)
        val = assignment[var]
        if val is None:
            return None
        return val if lit > 0 else not val

    def unit_propagate():
        trail = []
        while True:
            propagated = False
            for clause in clauses:
                unassigned = []
                satisfied = False
                for lit in clause:
                    val = get_lit_val(lit)
                    if val is True:
                        satisfied = True
                        break
                    elif val is None:
                        unassigned.append(lit)
                
                if satisfied:
                    continue
                if len(unassigned) == 0:
                    # Conflict
                    for var in trail:
                        assignment[var] = None
                    return False, []
                elif len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    val = (lit > 0)
                    assignment[var] = val
                    trail.append(var)
                    propagated = True
            if not propagated:
                break
        return True, trail

    # Jeroslow-Wang heuristic for branching
    def pick_branching_literal():
        # Score each literal
        scores = {}
        for clause in clauses:
            satisfied = False
            unassigned = []
            for lit in clause:
                val = get_lit_val(lit)
                if val is True:
                    satisfied = True
                    break
                elif val is None:
                    unassigned.append(lit)
            if not satisfied:
                weight = 2.0 ** (-len(unassigned))
                for lit in unassigned:
                    scores[lit] = scores.get(lit, 0.0) + weight
        if not scores:
            return None
        return max(scores, key=scores.get)

    def dpll():
        ok, trail = unit_propagate()
        if not ok:
            return False
        
        # Check if all satisfied
        lit = pick_branching_literal()
        if lit is None:
            # All remaining unassigned variables can be assigned arbitrary values
            return True
        
        var = abs(lit)
        val = (lit > 0)
        
        # Try preferred branch
        assignment[var] = val
        if dpll():
            return True
        assignment[var] = None
        
        # Try opposite branch
        assignment[var] = not val
        if dpll():
            return True
        assignment[var] = None
        
        # Undo unit propagation
        for v in trail:
            assignment[v] = None
        return False

    sys.setrecursionlimit(2000)
    if dpll():
        print("YES")
        res = []
        for i in range(1, n + 1):
            if assignment[i] is True:
                res.append("1")
            else:
                res.append("0")
        print(" ".join(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()