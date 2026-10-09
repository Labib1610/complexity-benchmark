import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    idx = 2
    clauses = []
    for _ in range(m):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        clauses.append((a, b, c))
    
    # Each lever i has two literals: i (UP) and -i (DOWN).
    # Literal l: if l>0 -> lever l UP; if l<0 -> lever -l DOWN.
    # We need to pick exactly one literal per lever (UP or DOWN).
    # Each clause requires at least one of its 3 literals to be true.
    
    # Greedy: repeatedly find a lever whose both orientations are "forced"
    # (i.e., one orientation makes some unsatisfied clause impossible to satisfy
    #  because all its literals would be false), and fix the other orientation.
    
    state = [0] * (n + 1)  # 0 = unset, 1 = UP, -1 = DOWN
    decided = [False] * (n + 1)
    
    changed = True
    while changed:
        changed = False
        for (a, b, c) in clauses:
            # check if clause is already satisfied
            sat = False
            for lit in (a, b, c):
                lever = abs(lit)
                if decided[lever]:
                    val = state[lever]
                    if (lit > 0 and val == 1) or (lit < 0 and val == -1):
                        sat = True
                        break
            if sat:
                continue
            # clause unsatisfied so far; find unset levers among its literals
            unset_lits = []
            for lit in (a, b, c):
                lever = abs(lit)
                if not decided[lever]:
                    unset_lits.append(lit)
            if len(unset_lits) == 1:
                lit = unset_lits[0]
                lever = abs(lit)
                if lit > 0:
                    state[lever] = 1
                else:
                    state[lever] = -1
                decided[lever] = True
                changed = True
    
    # After greedy, try to satisfy remaining clauses by search over unset levers.
    # Collect unset levers.
    unset = [i for i in range(1, n+1) if not decided[i]]
    
    # Precompute for efficiency: for each clause, list of (lever, required_val)
    clause_lits = []
    for (a, b, c) in clauses:
        lits = []
        for lit in (a, b, c):
            lever = abs(lit)
            val = 1 if lit > 0 else -1
            lits.append((lever, val))
        clause_lits.append(lits)
    
    # Build mapping from lever to clauses it appears in
    lever_to_clauses = [[] for _ in range(n+1)]
    for ci, lits in enumerate(clause_lits):
        for (lever, val) in lits:
            lever_to_clauses[lever].append(ci)
    
    # Current assignment including decided ones
    assign = [0] * (n + 1)
    for i in range(1, n+1):
        if decided[i]:
            assign[i] = state[i]
    
    # Check which clauses are already satisfied
    clause_sat = [False] * m
    unsat_count = 0
    for ci, lits in enumerate(clause_lits):
        s = False
        for (lever, val) in lits:
            if decided[lever] and assign[lever] == val:
                s = True
                break
        clause_sat[ci] = s
        if not s:
            unsat_count += 1
    
    if unsat_count == 0:
        # all satisfied, fill unset arbitrarily
        out = []
        for i in range(1, n+1):
            if decided[i]:
                out.append(1 if state[i] == 1 else 0)
            else:
                out.append(0)
        print("YES")
        print(' '.join(map(str, out)))
        return
    
    # Backtracking over unset levers
    # Order unset levers by number of unsat clauses they appear in (descending)
    def lever_unsat_count(lever):
        cnt = 0
        for ci in lever_to_clauses[lever]:
            if not clause_sat[ci]:
                cnt += 1
        return cnt
    
    unset_sorted = sorted(unset, key=lambda x: -lever_unsat_count(x))
    pos = {lever: i for i, lever in enumerate(unset_sorted)}
    
    # We'll do recursive search
    import sys
    sys.setrecursionlimit(10000)
    
    # Precompute list of unsat clauses for quick checking
    # We'll maintain clause_sat and unsat_count during search
    
    # For each unset lever, the two possible values
    # We try value that satisfies more unsat clauses first
    
    def count_satisfied_if_set(lever, val):
        cnt = 0
        for ci in lever_to_clauses[lever]:
            if not clause_sat[ci]:
                # check if setting lever=val satisfies ci
                for (lv, vv) in clause_lits[ci]:
                    if lv == lever and vv == val:
                        cnt += 1
                        break
        return cnt
    
    def backtrack(k):
        nonlocal unsat_count
        if unsat_count == 0:
            return True
        if k == len(unset_sorted):
            return False
        lever = unset_sorted[k]
        # try both values, prefer one satisfying more unsat clauses
        v1 = 1
        v2 = -1
        c1 = count_satisfied_if_set(lever, v1)
        c2 = count_satisfied_if_set(lever, v2)
        if c2 > c1:
            v1, v2 = v2, v1
        for val in (v1, v2):
            assign[lever] = val
            newly_sat = []
            for ci in lever_to_clauses[lever]:
                if not clause_sat[ci]:
                    for (lv, vv) in clause_lits[ci]:
                        if lv == lever and vv == val:
                            clause_sat[ci] = True
                            newly_sat.append(ci)
                            break
            unsat_count -= len(newly_sat)
            if backtrack(k+1):
                return True
            # undo
            for ci in newly_sat:
                clause_sat[ci] = False
            unsat_count += len(newly_sat)
            assign[lever] = 0
        return False
    
    if backtrack(0):
        out = []
        for i in range(1, n+1):
            v = assign[i]
            if v == 0:
                v = 1  # arbitrary for any remaining unset (shouldn't happen if unsat_count==0)
            out.append(1 if v == 1 else 0)
        print("YES")
        print(' '.join(map(str, out)))
    else:
        print("NO")

solve()