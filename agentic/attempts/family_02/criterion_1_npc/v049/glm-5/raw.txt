```python
import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    idx = 2
    rules = []
    for _ in range(m):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        rules.append((a, b, c))
    
    # assignment[i] = 1 means warm, 0 means cool, -1 means unassigned
    assignment = [-1] * (n + 1)
    
    # Precompute rule literals
    rule_lits = []
    for a, b, c in rules:
        lits = []
        for x in (a, b, c):
            var = abs(x)
            val = 1 if x > 0 else 0
            lits.append((var, val))
        rule_lits.append(lits)
    
    # Precompute rules_by_var
    rules_by_var = [[] for _ in range(n + 1)]
    for r_idx, lits in enumerate(rule_lits):
        seen = set()
        for var, val in lits:
            if var not in seen:
                rules_by_var[var].append(r_idx)
                seen.add(var)
    
    # Precompute rule_var_count
    rule_var_count = []
    for lits in rule_lits:
        seen = set()
        for var, val in lits:
            seen.add(var)
        rule_var_count.append(len(seen))
    
    # Precompute rule_unassigned
    rule_unassigned = [0] * m
    for r_idx, lits in enumerate(rule_lits):
        cnt = 0
        seen = set()
        for var, val in lits:
            if var not in seen:
                if assignment[var] == -1:
                    cnt += 1
                seen.add(var)
        rule_unassigned[r_idx] = cnt
    
    # Precompute rule_satisfied
    rule_satisfied = [False] * m
    for r_idx, lits in enumerate(rule_lits):
        sat = False
        for var, val in lits:
            if assignment[var] == val:
                sat = True
                break
        rule_satisfied[r_idx] = sat
    
    # Precompute rule_unassigned_vars
    rule_unassigned_vars = []
    for lits in rule_lits:
        seen = set()
        for var, val in lits:
            seen.add(var)
        rule_unassigned_vars.append(list(seen))
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_satisfied_count
    rule_satisfied_count = []
    for r_idx in range(m):
        cnt = 0
        for var, val in rule_lits[r_idx]:
            if assignment[var] == val:
                cnt += 1
        rule_satisfied_count.append(cnt)
    
    # Precompute rule_unassigned_vars_set
    rule_unassigned_vars_set = []
    for r_idx in range(m):
        s = set()
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                s.add(var)
        rule_unassigned_vars_set.append(s)
    
    # Precompute rule_unassigned_count
    rule_unassigned_count = []
    for r_idx in range(m):
        cnt = 0
        for var in rule_unassigned_vars[r_idx]:
            if assignment[var] == -1:
                cnt += 1
        rule_unassigned_count.append(cnt)
    
    # Precompute rule_s