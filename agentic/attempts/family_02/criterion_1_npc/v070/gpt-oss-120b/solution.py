import sys

sys.setrecursionlimit(10000)

def read_input():
    data = sys.stdin.read().strip().split()
    if not data:
        return 0, 0, []
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        clause = [int(next(it)), int(next(it)), int(next(it))]
        clauses.append(clause)
    return n, m, clauses

def simplify(clauses, assign):
    """Apply current assignment, return simplified clauses.
    If a clause becomes empty -> conflict."""
    new_clauses = []
    for cl in clauses:
        satisfied = False
        new_clause = []
        for lit in cl:
            var = abs(lit)
            if var in assign:
                val = assign[var]
                if (lit > 0 and val) or (lit < 0 and not val):
                    satisfied = True
                    break
                else:
                    continue  # false literal, drop
            else:
                new_clause.append(lit)
        if satisfied:
            continue
        if not new_clause:
            return None  # conflict
        new_clauses.append(new_clause)
    return new_clauses

def unit_propagate(clauses, assign):
    """Perform unit propagation. Return (conflict, updated assign, updated clauses)."""
    while True:
        unit = None
        for cl in clauses:
            if len(cl) == 1:
                unit = cl[0]
                break
        if unit is None:
            break
        var = abs(unit)
        val = unit > 0
        if var in assign:
            if assign[var] != val:
                return True, assign, clauses
        else:
            assign[var] = val
        clauses = simplify(clauses, {var: val})
        if clauses is None:
            return True, assign, None
    return False, assign, clauses

def pure_literal_eliminate(clauses, assign):
    """Eliminate pure literals."""
    while True:
        counts = {}
        for cl in clauses:
            for lit in cl:
                counts[lit] = counts.get(lit, 0) + 1
        pure = None
        for lit, cnt in counts.items():
            if -lit not in counts:
                pure = lit
                break
        if pure is None:
            break
        var = abs(pure)
        val = pure > 0
        if var in assign:
            if assign[var] != val:
                return None  # conflict, shouldn't happen
        else:
            assign[var] = val
        clauses = simplify(clauses, {var: val})
        if clauses is None:
            return None
    return clauses

def choose_var(clauses, assign, n):
    """Heuristic: choose variable appearing most."""
    freq = {}
    for cl in clauses:
        for lit in cl:
            v = abs(lit)
            if v in assign:
                continue
            freq[v] = freq.get(v, 0) + 1
    if not freq:
        # all assigned
        for v in range(1, n+1):
            if v not in assign:
                return v
    # pick max freq
    return max(freq, key=freq.get)

def dpll(clauses, assign, n):
    # simplify with current assign
    clauses = simplify(clauses, assign)
    if clauses is None:
        return None
    if not clauses:
        return assign
    # unit propagation
    conflict, assign, clauses = unit_propagate(clauses, assign)
    if conflict:
        return None
    if clauses is None:
        return None
    if not clauses:
        return assign
    # pure literal elimination
    clauses = pure_literal_eliminate(clauses, assign)
    if clauses is None:
        return None
    if not clauses:
        return assign
    # choose variable
    var = choose_var(clauses, assign, n)
    for val in (True, False):
        new_assign = assign.copy()
        new_assign[var] = val
        res = dpll(clauses, new_assign, n)
        if res is not None:
            return res
    return None

def solve():
    n, m, clauses = read_input()
    assign = {}
    result = dpll(clauses, assign, n)
    if result is None:
        print("NO")
    else:
        print("YES")
        out = []
        for i in range(1, n+1):
            out.append('1' if result.get(i, False) else '0')
        print(' '.join(out))

if __name__ == "__main__":
    solve()