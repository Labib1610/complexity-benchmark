from collections import defaultdict
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    clauses = []
    index = 2
    for _ in range(m):
        clause = []
        for _ in range(3):
            num = int(data[index])
            index += 1
            clause.append(num)
        clauses.append(clause)
    
    # Convert to 2-SAT format by breaking 3-SAT into multiple 2-SAT clauses
    # For each clause (a or b or c), we introduce a new variable y and convert to:
    # (a or b or c) <=> (a or y) and ((not y) or c)
    # But since we have 3-SAT, we'll use a different reduction:
    # (a or b or c) is equivalent to:
    # (y1 or a) and (not y1 or y2) and (not y2 or b or c)
    # We can continue this process until everything is in 2-CNF
    
    # However, there's a simpler way: for each 3-clause (a,b,c), we can replace it with
    # four 2-clauses that together are equisatisfiable:
    # This is not correct either. The correct way is to add new variables.
    
    # Let's do the standard reduction:
    # For clause (a or b or c), introduce new var z, then:
    # (a or b or c) becomes (a or z) and ((not z) or b or c)
    # Then for (not z or b or c), introduce new var w:
    # (not z or w) and (not w or b or c)
    # Keep going until all clauses are binary.
    
    # Actually, let's implement a proper 3-SAT solver using brute-force for small n,
    # or better yet, reduce to 2-SAT if possible, but since it's 3-SAT, we need a general approach.
    
    # Since n <= 90 and m <= 400, brute force won't work (2^90 is too big).
    # We should use a SAT solver approach. But given constraints, maybe randomized local search?
    # Or implement a simple backtracking with unit propagation?
    
    # Let's try implementing a simple DPLL-style algorithm.
    
    # Map from variable (1-based) to list of clauses where it appears positively/negatively
    var_clauses = defaultdict(lambda: {'pos': [], 'neg': []})
    
    # Also store clauses as sets for faster lookup
    clause_list = []
    for i, clause in enumerate(clauses):
        clause_set = set()
        for lit in clause:
            clause_set.add(lit)
            var = abs(lit)
            if lit > 0:
                var_clauses[var]['pos'].append(i)
            else:
                var_clauses[var]['neg'].append(i)
        clause_list.append(clause_set)
    
    # Current assignment: 0 = unassigned, 1 = true, -1 = false
    assignment = [0] * (n+1)
    decision_level = [0] * (n+1)
    watch_lists = [[] for _ in range(n+1)]  # for watched literals technique
    
    # Initialize unit clauses
    unit_clauses = []
    satisfied = [False] * len(clauses)
    
    def propagate_unit(lit):
        var = abs(lit)
        val = 1 if lit > 0 else -1
        if assignment[var] == 0:
            assignment[var] = val
            # Check for conflicts
            if val == 1:
                # Check clauses where var appears negatively
                for cid in var_clauses[var]['neg']:
                    if satisfied[cid]: continue
                    # Find another literal to watch
                    found = False
                    new_watch = None
                    for l in clause_list[cid]:
                        v = abs(l)
                        if l > 0:
                            if assignment[v] != -1:  # not false
                                found = True
                                new_watch = l
                                break
                        else:
                            if assignment[v] != 1:  # not true
                                found = True
                                new_watch = l
                                break
                    if not found:
                        # All literals are false except possibly this one
                        # So this clause is unit
                        other_lit = None
                        unsat_count = 0
                        for l in clause_list[cid]:
                            v = abs(l)
                            if l > 0:
                                if assignment[v] == -1:
                                    unsat_count += 1
                                elif assignment[v] == 0:
                                    other_lit = l
                            else:
                                if assignment[v] == 1:
                                    unsat_count += 1
                                elif assignment[v] == 0:
                                    other_lit = l
                        if unsat_count == 2 and other_lit is not None:
                            unit_clauses.append(other_lit)
                        elif unsat_count == 3:
                            return False  # conflict
            else:
                # Check clauses where var appears positively
                for cid in var_clauses[var]['pos']:
                    if satisfied[cid]: continue
                    found = False
                    new_watch = None
                    for l in clause_list[cid]:
                        v = abs(l)
                        if l > 0:
                            if assignment[v] != -1:
                                found = True
                                new_watch = l
                                break
                        else:
                            if assignment[v] != 1:
                                found = True
                                new_watch = l
                                break
                    if not found:
                        other_lit = None
                        unsat_count = 0
                        for l in clause_list[cid]:
                            v = abs(l)
                            if l > 0:
                                if assignment[v] == -1:
                                    unsat_count += 1
                                elif assignment[v] == 0:
                                    other_lit = l
                            else:
                                if assignment[v] == 1:
                                    unsat_count += 1
                                elif assignment[v] == 0:
                                    other_lit = l
                        if unsat_count == 2 and other_lit is not None:
                            unit_clauses.append(other_lit)
                        elif unsat_count == 3:
                            return False
        elif assignment[var] != val:
            return False  # conflict
        return True
    
    # Initial unit propagation
    for clause in clauses:
        if len(clause) == 1:
            unit_clauses.append(clause[0])
    
    stack = []  # for backtracking
    
    while True:
        conflict = False
        while unit_clauses:
            lit = unit_clauses.pop()
            if not propagate_unit(lit):
                conflict = True
                break
        
        if conflict:
            # Backtrack
            if not stack:
                print("NO")
                return
            var, old_val, old_dl, propagated = stack.pop()
            assignment[var] = 0
            # Restore state and continue
            continue
            
        # Check if all variables assigned
        unassigned_vars = [i for i in range(1, n+1) if assignment[i] == 0]
        if not unassigned_vars:
            # Check if solution is valid
            valid = True
            for clause in clauses:
                sat = False
                for lit in clause:
                    var = abs(lit)
                    val = 1 if lit > 0 else 0
                    if (lit > 0 and assignment[var] == 1) or (lit < 0 and assignment[var] == -1):
                        sat = True
                        break
                if not sat:
                    valid = False
                    break
            if valid:
                print("YES")
                result = []
                for i in range(1, n+1):
                    if assignment[i] == 1:
                        result.append('1')
                    else:
                        result.append('0')
                print(' '.join(result))
                return
            else:
                if not stack:
                    print("NO")
                    return
                var, old_val, old_dl, propagated = stack.pop()
                assignment[var] = 0
                continue
        
        # Pick unassigned variable (simple heuristic)
        var = unassigned_vars[0]
        # Try value 1 first
        stack.append((var, assignment[var], 0, []))
        assignment[var] = 1

if __name__ == "__main__":
    main()