import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    clauses = []                     # list of list of (var, val)
    occ = [[] for _ in range(n)]    # clause indices per variable
    for idx in range(m):
        lits = []
        for _ in range(3):
            x = int(next(it))
            var = abs(x) - 1
            val = 1 if x > 0 else 0
            lits.append((var, val))
            occ[var].append(idx)
        clauses.append(lits)

    assign = [-1] * n                # -1 unassigned, else 0/1
    trail = []                       # stack of assigned variables (for undo)

    # ---------- propagation ----------
    def propagate(stack):
        while stack:
            v = stack.pop()
            for cid in occ[v]:
                clause = clauses[cid]
                satisfied = False
                unassigned_cnt = 0
                last_unassigned = None
                for var, want in clause:
                    a = assign[var]
                    if a == -1:
                        unassigned_cnt += 1
                        last_unassigned = (var, want)
                    elif a == want:
                        satisfied = True
                        break
                if satisfied:
                    continue
                if unassigned_cnt == 0:
                    return False          # conflict
                if unassigned_cnt == 1:
                    var, want = last_unassigned
                    if assign[var] == -1:
                        assign[var] = want
                        trail.append(var)
                        stack.append(var)
        return True

    # ---------- variable ordering ----------
    degree = [len(occ[i]) for i in range(n)]
    order = sorted(range(n), key=lambda x: -degree[x])

    def choose_var():
        for v in order:
            if assign[v] == -1:
                return v
        return -1

    # ---------- DPLL ----------
    def dfs() -> bool:
        # check if all assigned
        if all(a != -1 for a in assign):
            return True
        v = choose_var()
        saved_trail_len = len(trail)
        for val in (0, 1):
            assign[v] = val
            trail.append(v)
            if propagate([v]):
                if dfs():
                    return True
            # undo
            while len(trail) > saved_trail_len:
                u = trail.pop()
                assign[u] = -1
        return False

    if dfs():
        out = ['YES', ' '.join(str(assign[i]) for i in range(n))]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()