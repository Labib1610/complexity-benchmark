import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

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
        # Remove duplicate literals within the clause
        c_set = set(c)
        # If both x and -x are in the clause, it is always satisfied
        tautology = False
        for lit in c_set:
            if -lit in c_set:
                tautology = True
                break
        if not tautology:
            clauses.append(list(c_set))
            
    assignment = {}

    def simplify(clauses, lit):
        new_clauses = []
        for c in clauses:
            if lit in c:
                continue
            if -lit in c:
                new_c = [l for l in c if l != -lit]
                if not new_c:
                    return None  # conflict
                new_clauses.append(new_c)
            else:
                new_clauses.append(c)
        return new_clauses

    def dpll(clauses, assign):
        # Unit propagation
        while True:
            unit_lit = None
            for c in clauses:
                if len(c) == 1:
                    unit_lit = c[0]
                    break
            if unit_lit is None:
                break
            
            var = abs(unit_lit)
            val = 1 if unit_lit > 0 else 0
            if var in assign and assign[var] != val:
                return False
            assign[var] = val
            clauses = simplify(clauses, unit_lit)
            if clauses is None:
                return False

        if not clauses:
            return True

        # Check for conflict
        for c in clauses:
            if len(c) == 0:
                return False

        # Jeroslow-Wang Heuristic
        weight = {}
        for c in clauses:
            w = 2 ** (-len(c))
            for lit in c:
                weight[lit] = weight.get(lit, 0.0) + w

        best_var = None
        best_score = -1.0
        for var in range(1, n + 1):
            if var not in assign:
                pos = weight.get(var, 0.0)
                neg = weight.get(-var, 0.0)
                score = pos + neg
                if score > best_score:
                    best_score = score
                    best_var = var

        if best_var is None:
            return True

        pos_w = weight.get(best_var, 0.0)
        neg_w = weight.get(-best_var, 0.0)
        first_lit = best_var if pos_w >= neg_w else -best_var
        second_lit = -first_lit

        # Try first literal
        c1 = simplify(clauses, first_lit)
        if c1 is not None:
            a1 = assign.copy()
            a1[best_var] = 1 if first_lit > 0 else 0
            if dpll(c1, a1):
                assign.clear()
                assign.update(a1)
                return True

        # Try second literal
        c2 = simplify(clauses, second_lit)
        if c2 is not None:
            a2 = assign.copy()
            a2[best_var] = 1 if second_lit > 0 else 0
            if dpll(c2, a2):
                assign.clear()
                assign.update(a2)
                return True

        return False

    if dpll(clauses, assignment):
        print("YES")
        res = [str(assignment.get(i, 0)) for i in range(1, n + 1)]
        print(" ".join(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()