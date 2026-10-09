import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        c = [int(next(it)), int(next(it)), int(next(it))]
        clauses.append(c)

    # For each variable keep list of clause indices where it appears
    var_pos = [[] for _ in range(n + 1)]
    var_neg = [[] for _ in range(n + 1)]
    for idx, cl in enumerate(clauses):
        for lit in cl:
            v = abs(lit)
            if lit > 0:
                var_pos[v].append(idx)
            else:
                var_neg[v].append(idx)

    assign = {}                     # var -> 0/1
    trail = []                      # (clause_index, old_clause_copy)

    # ---------- helper functions ----------
    def clause_is_satisfied(cl):
        for lit in cl:
            v = abs(lit)
            if v in assign:
                val = assign[v]
                if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                    return True
        return False

    def unit_literal(cl):
        # return the only literal that is not yet falsified, or None
        unk = None
        for lit in cl:
            v = abs(lit)
            if v not in assign:
                if unk is not None:
                    return None
                unk = lit
            else:
                val = assign[v]
                if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                    return None  # clause already satisfied
        return unk

    def propagate() -> bool:
        """unit propagation, returns False on conflict."""
        queue = []
        # initial unit clauses
        for idx, cl in enumerate(clauses):
            if clause_is_satisfied(cl):
                continue
            u = unit_literal(cl)
            if u is not None:
                queue.append(u)

        while queue:
            lit = queue.pop()
            var = abs(lit)
            val = 1 if lit > 0 else 0
            if var in assign:
                if assign[var] != val:
                    return False
                continue
            assign[var] = val
            # update clauses containing var
            affected = var_pos[var] if val == 1 else var_neg[var]
            for ci in affected:
                old = clauses[ci]
                if old is None:   # already satisfied
                    continue
                # save copy
                trail.append((ci, old))
                # remove falsified literals
                new = [l for l in old if not (abs(l) == var and ((l > 0) != (val == 1)))]
                # if clause becomes satisfied, mark as None
                sat = False
                for l in new:
                    v = abs(l)
                    if v in assign:
                        vv = assign[v]
                        if (l > 0 and vv == 1) or (l < 0 and vv == 0):
                            sat = True
                            break
                if sat:
                    clauses[ci] = None
                    continue
                if not new:          # empty clause -> conflict
                    return False
                clauses[ci] = new
                if len(new) == 1:
                    queue.append(new[0])
        return True

    def undo(trail_sz):
        while len(trail) > trail_sz:
            ci, old = trail.pop()
            clauses[ci] = old
        # remove assignments that were added after the saved point
        # we cannot know exactly which vars, so recompute from clauses:
        # simpler: keep a stack of assigned vars
        # We'll maintain a separate assign_stack
        while assign_stack and len(assign_stack) > assign_sz:
            v = assign_stack.pop()
            del assign[v]

    # To be able to undo assignments we keep a stack
    assign_stack = []
    assign_sz = 0

    # ---------- DPLL ----------
    def dpll() -> bool:
        # check if all clauses satisfied
        all_sat = True
        for cl in clauses:
            if cl is None:
                continue
            all_sat = False
            break
        if all_sat:
            return True

        # pure literal elimination (optional, cheap)
        while True:
            pos = [0] * (n + 1)
            neg = [0] * (n + 1)
            for cl in clauses:
                if cl is None:
                    continue
                for lit in cl:
                    v = abs(lit)
                    if v in assign:
                        continue
                    if lit > 0:
                        pos[v] = 1
                    else:
                        neg[v] = 1
            pure_found = False
            for v in range(1, n + 1):
                if v in assign:
                    continue
                if pos[v] and not neg[v]:
                    # set to 1
                    assign[v] = 1
                    assign_stack.append(v)
                    if not propagate():
                        return False
                    pure_found = True
                    break
                if neg[v] and not pos[v]:
                    assign[v] = 0
                    assign_stack.append(v)
                    if not propagate():
                        return False
                    pure_found = True
                    break
            if not pure_found:
                break

        # choose variable
        for v in range(1, n + 1):
            if v not in assign:
                var = v
                break
        else:
            return True  # all assigned

        for val in (0, 1):
            saved_trail = len(trail)
            saved_assign_sz = len(assign_stack)
            assign[var] = val
            assign_stack.append(var)
            if propagate():
                if dpll():
                    return True
            # backtrack
            undo(saved_trail)
            while len(assign_stack) > saved_assign_sz:
                vv = assign_stack.pop()
                del assign[vv]
        return False

    # initial propagation (none)
    if dpll():
        out = ['YES']
        res = [str(assign.get(i, 0)) for i in range(1, n + 1)]
        out.append(' '.join(res))
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()