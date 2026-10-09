import sys

# Set recursion depth just in case
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
        # Simplify clause: remove duplicate literals
        # If clause contains both x and -x, it's always true, so ignore it
        s = set(c)
        tautology = False
        for x in s:
            if -x in s:
                tautology = True
                break
        if not tautology:
            clauses.append(list(s))

    # assignment: index 1..n, values: 1 (True), 0 (False), None (unassigned)
    assignment = [None] * (n + 1)

    def bcp(clauses, assignment):
        """Boolean Constraint Propagation (Unit Propagation)"""
        while True:
            unit_found = False
            for c in clauses:
                unassigned = []
                satisfied = False
                for lit in c:
                    var = abs(lit)
                    val = assignment[var]
                    if val is not None:
                        if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                            satisfied = True
                            break
                    else:
                        unassigned.append(lit)
                
                if satisfied:
                    continue
                if len(unassigned) == 0:
                    return False  # Conflict
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    val = 1 if lit > 0 else 0
                    assignment[var] = val
                    unit_found = True
                    break  # Restart scanning after assigning
            if not unit_found:
                break
        return True

    def dpll(assignment):
        # Apply Unit Propagation
        assign_copy = list(assignment)
        if not bcp(clauses, assign_copy):
            return None

        # Check if all clauses are satisfied
        all_satisfied = True
        remaining_clauses = []
        for c in clauses:
            sat = False
            for lit in c:
                var = abs(lit)
                val = assign_copy[var]
                if val is not None and ((lit > 0 and val == 1) or (lit < 0 and val == 0)):
                    sat = True
                    break
            if not sat:
                all_satisfied = False
                # Filter unassigned literals
                rem = [lit for lit in c if assign_copy[abs(lit)] is None]
                if not rem:
                    return None
                remaining_clauses.append(rem)

        if all_satisfied:
            # Set any unassigned to 0 (default)
            for i in range(1, n + 1):
                if assign_copy[i] is None:
                    assign_copy[i] = 0
            return assign_copy

        # Jeroslow-Wang heuristic for variable selection
        score_pos = {}
        score_neg = {}
        for c in remaining_clauses:
            weight = 2 ** (-len(c))
            for lit in c:
                var = abs(lit)
                if lit > 0:
                    score_pos[var] = score_pos.get(var, 0) + weight
                else:
                    score_neg[var] = score_neg.get(var, 0) + weight

        best_var = None
        max_score = -1
        for var in range(1, n + 1):
            if assign_copy[var] is None:
                s = score_pos.get(var, 0) + score_neg.get(var, 0)
                if s > max_score:
                    max_score = s
                    best_var = var

        if best_var is None:
            for i in range(1, n + 1):
                if assign_copy[i] is None:
                    assign_copy[i] = 0
            return assign_copy

        # Decide which value to try first
        if score_pos.get(best_var, 0) >= score_neg.get(best_var, 0):
            branches = [1, 0]
        else:
            branches = [0, 1]

        for val in branches:
            assign_copy[best_var] = val
            res = dpll(assign_copy)
            if res is not None:
                return res
            assign_copy[best_var] = None

        return None

    res = dpll(assignment)
    if res is not None:
        print("YES")
        print(*(res[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()