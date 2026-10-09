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
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        clauses.append((a, b, c))
    
    # Convert to 0-indexed variables: positive x -> var x-1, negative -x -> var x-1
    # We'll store clauses as list of (var, is_true) where is_true means literal is positive.
    clause_list = []
    for a, b, c in clauses:
        clause = []
        for lit in (a, b, c):
            var = abs(lit) - 1
            is_pos = lit > 0
            clause.append((var, is_pos))
        clause_list.append(clause)
    
    assignment = [None] * n  # None = unassigned, True/False = value
    
    # Watch lists for unit propagation
    watch = [[] for _ in range(2 * n)]  # index: var*2 + (0 if neg, 1 if pos)
    for idx, clause in enumerate(clause_list):
        for var, is_pos in clause:
            watch[var * 2 + (1 if is_pos else 0)].append(idx)
    
    # For each clause, keep count of unassigned literals and satisfied status
    satisfied = [False] * m
    unassigned_count = [len(clause) for clause in clause_list]
    
    def literal_value(var, is_pos):
        val = assignment[var]
        if val is None:
            return None
        return val == is_pos
    
    def set_var(var, val):
        assignment[var] = val
        # Update clauses
        for idx in watch[var * 2 + (1 if val else 0)]:
            if satisfied[idx]:
                continue
            # Check if this clause is now satisfied
            for v, p in clause_list[idx]:
                lv = literal_value(v, p)
                if lv is True:
                    satisfied[idx] = True
                    break
            if satisfied[idx]:
                continue
            # Not satisfied, decrement unassigned count
            unassigned_count[idx] -= 1
    
    def unset_var(var):
        val = assignment[var]
        assignment[var] = None
        for idx in watch[var * 2 + (1 if val else 0)]:
            if satisfied[idx]:
                # Recompute satisfaction
                sat = False
                for v, p in clause_list[idx]:
                    lv = literal_value(v, p)
                    if lv is True:
                        sat = True
                        break
                if not sat:
                    satisfied[idx] = False
                    # Recompute unassigned count
                    cnt = 0
                    for v, p in clause_list[idx]:
                        if assignment[v] is None:
                            cnt += 1
                    unassigned_count[idx] = cnt
            else:
                unassigned_count[idx] += 1
    
    # Pure literal elimination: if a variable appears only in one polarity, set it
    def apply_pure_literal():
        pos_count = [0] * n
        neg_count = [0] * n
        for clause in clause_list:
            for var, is_pos in clause:
                if is_pos:
                    pos_count[var] += 1
                else:
                    neg_count[var] += 1
        changed = False
        for var in range(n):
            if assignment[var] is None:
                if pos_count[var] > 0 and neg_count[var] == 0:
                    set_var(var, True)
                    changed = True
                elif neg_count[var] > 0 and pos_count[var] == 0:
                    set_var(var, False)
                    changed = True
        return changed
    
    # Unit propagation: if a clause has exactly one unassigned literal and is not satisfied, set it
    def unit_propagate():
        changed = False
        for idx in range(m):
            if satisfied[idx]:
                continue
            if unassigned_count[idx] == 1:
                # find the unassigned literal
                for var, is_pos in clause_list[idx]:
                    if assignment[var] is None:
                        set_var(var, is_pos)
                        changed = True
                        break
        return changed
    
    # Backtracking search
    def backtrack():
        # Apply pure literal and unit propagation repeatedly
        while True:
            p1 = apply_pure_literal()
            p2 = unit_propagate()
            if not p1 and not p2:
                break
        
        # Check if all clauses satisfied
        if all(satisfied):
            return True
        
        # Choose an unassigned variable (heuristic: most occurrences)
        best_var = -1
        best_count = -1
        for var in range(n):
            if assignment[var] is None:
                cnt = 0
                for clause in clause_list:
                    for v, p in clause:
                        if v == var:
                            cnt += 1
                if cnt > best_count:
                    best_count = cnt
                    best_var = var
        if best_var == -1:
            return False
        
        # Try True then False
        for val in (True, False):
            set_var(best_var, val)
            if backtrack():
                return True
            unset_var(best_var)
        return False
    
    if backtrack():
        print("YES")
        print(" ".join("1" if assignment[i] else "0" for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()