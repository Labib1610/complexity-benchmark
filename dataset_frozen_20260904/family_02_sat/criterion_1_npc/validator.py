def _satisfiable(n, clauses, var_cl):
    import sys
    sys.setrecursionlimit(1 << 20)
    assign = [None] * (n + 1)

    def lit_val(l):
        v = assign[abs(l)]
        if v is None:
            return None
        return (v == 1) if l > 0 else (v == 0)

    def bcp(seed):
        forced = []
        queue = list(seed)
        while queue:
            var = queue.pop()
            for ci in var_cl[var]:
                unassigned = None; cnt = 0; sat = False
                for l in clauses[ci]:
                    tv = lit_val(l)
                    if tv is True:
                        sat = True; break
                    if tv is None:
                        cnt += 1; unassigned = l
                if sat:
                    continue
                if cnt == 0:
                    for v in forced:
                        assign[v] = None
                    return False, None
                if cnt == 1:
                    av = abs(unassigned)
                    assign[av] = 1 if unassigned > 0 else 0
                    forced.append(av); queue.append(av)
        return True, forced

    def dpll():
        v = 1
        while v <= n and assign[v] is not None:
            v += 1
        if v > n:
            return True
        for val in (1, 0):
            assign[v] = val
            ok, forced = bcp([v])
            if ok and dpll():
                return True
            if forced:
                for u in forced:
                    assign[u] = None
            assign[v] = None
        return False

    return dpll()


def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    n = int(data[idx]); m = int(data[idx + 1]); idx += 2
    clauses = []
    var_cl = [[] for _ in range(n + 1)]
    for ci in range(m):
        a = int(data[idx]); b = int(data[idx + 1]); c = int(data[idx + 2]); idx += 3
        clauses.append((a, b, c))
        for l in (a, b, c):
            var_cl[abs(l)].append(ci)

    feasible = _satisfiable(n, clauses, var_cl)

    toks = output_text.split()
    if not toks:
        return False, "empty output"
    head = toks[0].upper()
    if head == "NO":
        if feasible:
            return False, "reported NO but a satisfying assignment exists"
        return True, "correctly reported unsatisfiable"
    if head != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"
    if not feasible:
        return False, "reported YES but the formula is unsatisfiable"

    try:
        vals = [int(t) for t in toks[1:]]
    except ValueError:
        return False, "non-integer state"
    if len(vals) != n:
        return False, f"expected {n} states, got {len(vals)}"
    if any(s not in (0, 1) for s in vals):
        return False, "each state must be 0 or 1"
    a = [0] + vals
    for cl in clauses:
        ok = False
        for l in cl:
            if (l > 0 and a[l] == 1) or (l < 0 and a[-l] == 0):
                ok = True; break
        if not ok:
            return False, f"clause {cl} is not satisfied"
    return True, "valid satisfying assignment"
