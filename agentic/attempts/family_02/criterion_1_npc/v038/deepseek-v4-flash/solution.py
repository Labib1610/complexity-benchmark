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
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        clauses.append((a, b, c))
    
    # Variable assignment: 0 = unassigned, 1 = True, -1 = False
    assignment = [0] * (n + 1)
    
    def propagate(assign):
        # Returns (new_assign, conflict)
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                # Check if clause is already satisfied
                satisfied = False
                unassigned = []
                for lit in clause:
                    var = abs(lit)
                    val = assign[var]
                    if val == 0:
                        unassigned.append(lit)
                    elif (lit > 0 and val == 1) or (lit < 0 and val == -1):
                        satisfied = True
                        break
                if satisfied:
                    continue
                if len(unassigned) == 0:
                    return None, True  # conflict
                if len(unassigned) == 1:
                    # Must set this literal to True
                    lit = unassigned[0]
                    var = abs(lit)
                    val = 1 if lit > 0 else -1
                    if assign[var] != 0 and assign[var] != val:
                        return None, True
                    if assign[var] == 0:
                        assign[var] = val
                        changed = True
        return assign, False
    
    def pure_literal_elimination(assign):
        # Find pure literals among unassigned variables
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
        for var in range(1, n+1):
            if assign[var] == 0:
                p = pos_count.get(var, 0)
                q = neg_count.get(var, 0)
                if p > 0 and q == 0:
                    assign[var] = 1
                elif q > 0 and p == 0:
                    assign[var] = -1
    
    def backtrack(assign):
        assign, conflict = propagate(assign[:])
        if conflict:
            return None
        # Check if all clauses satisfied
        all_sat = True
        for clause in clauses:
            sat = False
            for lit in clause:
                var = abs(lit)
                val = assign[var]
                if (lit > 0 and val == 1) or (lit < 0 and val == -1):
                    sat = True
                    break
            if not sat:
                all_sat = False
                break
        if all_sat:
            return assign
        
        # Choose an unassigned variable
        var = None
        for i in range(1, n+1):
            if assign[i] == 0:
                var = i
                break
        if var is None:
            return None
        
        # Try True
        assign1 = assign[:]
        assign1[var] = 1
        res = backtrack(assign1)
        if res is not None:
            return res
        
        # Try False
        assign2 = assign[:]
        assign2[var] = -1
        res = backtrack(assign2)
        if res is not None:
            return res
        
        return None
    
    # Initial propagation and pure literal elimination
    assign, conflict = propagate(assignment[:])
    if conflict:
        print("NO")
        return
    pure_literal_elimination(assign)
    
    result = backtrack(assign)
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