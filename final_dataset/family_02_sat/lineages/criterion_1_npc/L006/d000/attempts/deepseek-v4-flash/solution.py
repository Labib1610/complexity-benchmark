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
        l1 = int(input_data[idx])
        l2 = int(input_data[idx+1])
        l3 = int(input_data[idx+2])
        idx += 3
        clauses.append((l1, l2, l3))
    
    assignment = [None] * (n + 1)  # None = unassigned, True/False = value
    
    # Preprocess: remove duplicate literals in each clause
    processed_clauses = []
    for clause in clauses:
        s = set()
        for lit in clause:
            var = abs(lit)
            val = lit > 0
            s.add((var, val))
        processed_clauses.append(list(s))
    
    clauses = processed_clauses
    
    def propagate():
        changed = True
        while changed:
            changed = False
            # Unit propagation
            for clause in clauses:
                unassigned = []
                satisfied = False
                for var, val in clause:
                    if assignment[var] is None:
                        unassigned.append((var, val))
                    elif assignment[var] == val:
                        satisfied = True
                        break
                if satisfied:
                    continue
                if len(unassigned) == 0:
                    return False
                if len(unassigned) == 1:
                    var, val = unassigned[0]
                    if assignment[var] is None:
                        assignment[var] = val
                        changed = True
                    elif assignment[var] != val:
                        return False
            # Pure literal elimination
            # Count occurrences
            pos_count = {}
            neg_count = {}
            for clause in clauses:
                satisfied = False
                for var, val in clause:
                    if assignment[var] is not None and assignment[var] == val:
                        satisfied = True
                        break
                if satisfied:
                    continue
                for var, val in clause:
                    if assignment[var] is None:
                        if val:
                            pos_count[var] = pos_count.get(var, 0) + 1
                        else:
                            neg_count[var] = neg_count.get(var, 0) + 1
            for var in list(pos_count.keys()):
                if var not in neg_count:
                    if assignment[var] is None:
                        assignment[var] = True
                        changed = True
            for var in list(neg_count.keys()):
                if var not in pos_count:
                    if assignment[var] is None:
                        assignment[var] = False
                        changed = True
        return True
    
    def backtrack():
        # Propagate first
        if not propagate():
            return False
        # Find unassigned variable
        var = None
        for i in range(1, n+1):
            if assignment[i] is None:
                var = i
                break
        if var is None:
            return True  # all assigned
        # Try both values
        for val in (True, False):
            assignment[var] = val
            saved = assignment[:]
            if backtrack():
                return True
            assignment[:] = saved
        assignment[var] = None
        return False
    
    if backtrack():
        print("YES")
        print(" ".join('1' if assignment[i] else '0' for i in range(1, n+1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()