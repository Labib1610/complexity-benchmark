import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        clauses.append([a, b, c])

    # occurrence lists for pure literal detection
    occ_pos = [[] for _ in range(n + 1)]
    occ_neg = [[] for _ in range(n + 1)]
    for idx, cl in enumerate(clauses):
        for lit in cl:
            v = abs(lit)
            if lit > 0:
                occ_pos[v].append(idx)
            else:
                occ_neg[v].append(idx)

    # clause state: number of still possibly true literals, and a representative literal
    cnt = [3] * m
    rep = [cl[0] for cl in clauses]   # any literal, will be updated

    assign = {}          # var -> 0/1
    stack_assign = []    # for backtracking: list of (var, old_value or None)
    stack_clause = []    # for backtracking clause state changes

    # ---------- helper functions ----------
    def set_literal(lit):
        """assign variable according to literal, return False on conflict."""
        var = abs(lit)
        val = 1 if lit > 0 else 0
        if var in assign:
            return assign[var] == val
        # record assignment for backtrack
        stack_assign.append((var, None))
        assign[var] = val
        # update clauses where this literal appears positively (i.e. satisfied)
        for ci in (occ_pos[var] if val == 1 else occ_neg[var]):
            if cnt[ci] == 0:
                continue
            # clause becomes satisfied, mark cnt=0
            stack_clause.append((ci, cnt[ci], rep[ci]))
            cnt[ci] = 0
        # update clauses where opposite literal appears (now one less possible true)
        opp = occ_neg[var] if val == 1 else occ_pos[var]
        for ci in opp:
            if cnt[ci] == 0:
                continue
            # remove one possible true literal
            stack_clause.append((ci, cnt[ci], rep[ci]))
            cnt[ci] -= 1
            # find a new representative literal that is not yet false
            # we just scan the three literals
            for l in clauses[ci]:
                v = abs(l)
                if v in assign:
                    if (l > 0 and assign[v] == 1) or (l < 0 and assign[v] == 0):
                        # clause already satisfied, will be handled by previous loop
                        pass
                else:
                    rep[ci] = l
                    break
            else:
                # all literals assigned false -> conflict
                return False
        return True

    def propagate():
        """perform unit propagation, return True if no conflict."""
        # queue of unit literals
        q = []
        for i in range(m):
            if cnt[i] == 1:
                q.append(rep[i])
        while q:
            lit = q.pop()
            if not set_literal(lit):
                return False
            # after setting, new unit clauses may appear
            for i in range(m):
                if cnt[i] == 1:
                    q.append(rep[i])
        return True

    def pure_eliminate():
        """assign all pure literals, return False on conflict."""
        while True:
            pure = None
            for v in range(1, n + 1):
                if v in assign:
                    continue
                pos = any(cnt[ci] > 0 for ci in occ_pos[v])
                neg = any(cnt[ci] > 0 for ci in occ_neg[v])
                if pos and not neg:
                    pure = v   # must be true
                    lit = v
                elif neg and not pos:
                    pure = v
                    lit = -v
                else:
                    continue
                if pure is not None:
                    if not set_literal(lit):
                        return False
                    if not propagate():
                        return False
                    break
            else:
                break
        return True

    # ---------- DPLL ----------
    def dpll():
        # check if all clauses satisfied
        if all(c == 0 for c in cnt):
            return True
        # conflict?
        if any(c == 0 and not any((l > 0 and assign.get(abs(l)) == 1) or
                                 (l < 0 and assign.get(abs(l)) == 0) for l in clauses[i])
               for i, c in enumerate(cnt)):
            return False
        # pure literal elimination
        if not pure_eliminate():
            return False
        # choose variable with highest occurrence
        best = None
        best_deg = -1
        for v in range(1, n + 1):
            if v in assign:
                continue
            deg = len(occ_pos[v]) + len(occ_neg[v])
            if deg > best_deg:
                best_deg = deg
                best = v
        var = best
        # try true then false
        for val in (1, 0):
            # save state
            saved_assign_len = len(stack_assign)
            saved_clause_len = len(stack_clause)
            saved_assign_snapshot = assign.copy()
            # assign
            if set_literal(var if val == 1 else -var):
                if propagate():
                    if dpll():
                        return True
            # backtrack
            while len(stack_assign) > saved_assign_len:
                v, _ = stack_assign.pop()
                assign.pop(v, None)
            while len(stack_clause) > saved_clause_len:
                ci, old_cnt, old_rep = stack_clause.pop()
                cnt[ci] = old_cnt
                rep[ci] = old_rep
        return False

    # initial propagation (none yet)
    if dpll():
        out = ['YES']
        out.append(' '.join(str(assign.get(i, 0)) for i in range(1, n + 1)))
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()