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
        l1 = int(input_data[idx]); l2 = int(input_data[idx+1]); l3 = int(input_data[idx+2])
        idx += 3
        clauses.append((l1, l2, l3))
    
    # Convert to 0-indexed variables: 0..n-1
    # literal: positive x -> (var, True), negative -x ->(var, False)
    def lit_to_pair(lit):
        if lit > 0:
            return (lit-1, True)
        else:
            return (-lit-1, False)
    
    clauses = [tuple(lit_to_pair(l) for l in c) for c in clauses]
    
    assignment = [None] * n
    
    def propagate(assign):
        # assign: list of None/True/False
        changed = True
        while changed:
            changed = False
            # Check for empty clauses
            for clause in clauses:
                unassigned = []
                satisfied = False
                for var, val in clause:
                    if assign[var] is None:
                        unassigned.append((var, val))
                    elif assign[var] == val:
                        satisfied = True
                        break
                if satisfied:
                    continue
                if not unassigned:
                    return False
                if len(unassigned) == 1:
                    var, val = unassigned[0]
                    if assign[var] is None:
                        assign[var] = val
                        changed = True
                    # if already assigned opposite, would have been caught
            # Pure literal elimination
            # Count occurrences of each literal in unresolved clauses
            pos_count = [0]*n
            neg_count = [0]*n
            active_clauses = []
            for clause in clauses:
                sat = False
                for var, val in clause:
                    if assign[var] is not None and assign[var] == val:
                        sat = True
                        break
                if sat:
                    continue
                # clause not satisfied
                active_clauses.append(clause)
                for var, val in clause:
                    if assign[var] is None:
                        if val:
                            pos_count[var] += 1
                        else:
                            neg_count[var] += 1
            # If any pure literal exists, assign it
            for var in range(n):
                if assign[var] is None:
                    if pos_count[var] > 0 and neg_count[var] == 0:
                        assign[var] = True
                        changed = True
                    elif neg_count[var] > 0 and pos_count[var] == 0:
                        assign[var] = False
                        changed = True
        return True
    
    def backtrack(assign):
        # Propagate first
        if not propagate(assign):
            return False
        # Find unassigned variable
        try:
            var = next(i for i in range(n) if assign[i] is None)
        except StopIteration:
            return True
        # Try True then False
        for val in (True, False):
            assign[var] = val
            if backtrack(assign):
                return True
            assign[var] = None
        return False
    
    if backtrack(assignment):
        print("YES")
        print(" ".join('1' if v else '0' for v in assignment))
    else:
        print("NO")

if __name__ == "__main__":
    solve()