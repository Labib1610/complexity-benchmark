import sys

sys.setrecursionlimit(10000)

def solve_instance(n, clauses):
    assign = [-1] * n          # -1 unassigned, 0 false, 1 true
    stack = []                 # variables assigned in current branch

    # ---------- helper functions ----------
    def lit_is_true(l):
        v = abs(l) - 1
        val = assign[v]
        if val == -1:
            return None
        return (val == 1) if l > 0 else (val == 0)

    def propagate():
        """unit propagation, returns False on conflict."""
        changed = True
        while changed:
            changed = False
            for a, b, c in clauses:
                vals = [lit_is_true(a), lit_is_true(b), lit_is_true(c)]
                # if any literal already true, clause satisfied
                if any(v is True for v in vals):
                    continue
                # count falses and collect the undetermined literal
                false_cnt = sum(v is False for v in vals)
                if false_cnt == 3:
                    return False          # conflict
                if false_cnt == 2:
                    # unit clause, find the undetermined literal
                    for lit, v in zip((a, b, c), vals):
                        if v is None:
                            var = abs(lit) - 1
                            needed = 1 if lit > 0 else 0
                            if assign[var] == -1:
                                assign[var] = needed
                                stack.append(var)
                                changed = True
                            elif assign[var] != needed:
                                return False  # conflict
                            break
        return True

    # ---------- recursive DPLL ----------
    def dfs():
        # propagate current partial assignment
        if not propagate():
            return False
        # check if all assigned
        if all(v != -1 for v in assign):
            return True
        # choose first unassigned variable
        v = assign.index(-1)
        # try both values, remembering stack size to backtrack
        for val in (0, 1):
            saved_len = len(stack)
            assign[v] = val
            stack.append(v)
            if dfs():
                return True
            # backtrack
            while len(stack) > saved_len:
                var = stack.pop()
                assign[var] = -1
        return False

    if dfs():
        return True, assign
    else:
        return False, None


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        l1 = int(next(it)); l2 = int(next(it)); l3 = int(next(it))
        clauses.append((l1, l2, l3))

    sat, assignment = solve_instance(n, clauses)
    out = []
    if not sat:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(str(v) for v in assignment))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()