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
        c = [int(next(it)) for _ in range(3)]
        clauses.append(c)

    # assignment: -1 unknown, 0 false, 1 true
    assign = [-1] * (n + 1)

    # precompute variable occurrences for heuristic
    var_pos = [0] * (n + 1)
    var_neg = [0] * (n + 1)
    for cl in clauses:
        for lit in cl:
            v = abs(lit)
            if lit > 0:
                var_pos[v] += 1
            else:
                var_neg[v] += 1

    # order variables by total occurrence descending
    var_order = sorted(range(1, n + 1), key=lambda v: var_pos[v] + var_neg[v], reverse=True)

    def literal_value(lit, a):
        v = abs(lit)
        val = a[v]
        if val == -1:
            return -1
        return val if lit > 0 else 1 - val

    def propagate(a):
        """returns (True, changed) if no conflict, else (False, _)."""
        changed = True
        while changed:
            changed = False
            # unit propagation
            for cl in clauses:
                sat = False
                unassigned = []
                for lit in cl:
                    val = literal_value(lit, a)
                    if val == 1:
                        sat = True
                        break
                    elif val == -1:
                        unassigned.append(lit)
                if sat:
                    continue
                if not unassigned:          # all false -> conflict
                    return False, False
                if len(unassigned) == 1:   # unit clause
                    lit = unassigned[0]
                    v = abs(lit)
                    needed = 1 if lit > 0 else 0
                    if a[v] == -1:
                        a[v] = needed
                        changed = True
                    elif a[v] != needed:
                        return False, False
        return True, True

    def pure_literal_assign(a):
        """assign pure literals, return False if conflict (shouldn't happen)."""
        while True:
            pos_cnt = [0] * (n + 1)
            neg_cnt = [0] * (n + 1)
            for cl in clauses:
                # clause already satisfied?
                if any(literal_value(lit, a) == 1 for lit in cl):
                    continue
                for lit in cl:
                    v = abs(lit)
                    if a[v] != -1:
                        continue
                    if lit > 0:
                        pos_cnt[v] += 1
                    else:
                        neg_cnt[v] += 1
            assigned = False
            for v in range(1, n + 1):
                if a[v] == -1:
                    if pos_cnt[v] > 0 and neg_cnt[v] == 0:
                        a[v] = 1
                        assigned = True
                    elif neg_cnt[v] > 0 and pos_cnt[v] == 0:
                        a[v] = 0
                        assigned = True
            if not assigned:
                break
            ok, _ = propagate(a)
            if not ok:
                return False
        return True

    def dfs(a):
        ok, _ = propagate(a)
        if not ok:
            return None
        if not pure_literal_assign(a):
            return None
        # check if all clauses satisfied
        all_sat = True
        for cl in clauses:
            if not any(literal_value(lit, a) == 1 for lit in cl):
                all_sat = False
                break
        if all_sat:
            return a
        # pick unassigned variable
        for v in var_order:
            if a[v] == -1:
                var = v
                break
        # try true then false
        for val in (1, 0):
            a2 = a[:]
            a2[var] = val
            res = dfs(a2)
            if res is not None:
                return res
        return None

    result = dfs(assign)
    if result is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(result[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()