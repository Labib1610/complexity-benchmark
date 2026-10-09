import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))

    raw_clauses = []
    for _ in range(m):
        c = [int(next(it)), int(next(it)), int(next(it))]
        raw_clauses.append(c)

    # Preprocess clauses:
    # 1. Remove duplicate literals in the same clause
    # 2. If both x and -x in clause, clause is always true, ignore it
    # 3. If empty clause, unsatisfiable immediately
    clauses = []
    for c in raw_clauses:
        # eliminate duplicates
        s = set(c)
        if any(-x in s for x in s):
            continue  # tautology
        clauses.append(list(s))

    num_clauses = len(clauses)

    pos_occ = [[] for _ in range(n + 1)]
    neg_occ = [[] for _ in range(n + 1)]

    for cid, c in enumerate(clauses):
        for lit in c:
            if lit > 0:
                pos_occ[lit].append(cid)
            else:
                neg_occ[-lit].append(cid)

    # State
    # assign: 1 (True), 0 (False), None (Unassigned)
    assign = [None] * (n + 1)
    num_sat = [0] * num_clauses
    num_unassigned = [len(c) for c in clauses]

    # Pre-check for clauses of length 0 (if any were initially empty)
    for c in clauses:
        if len(c) == 0:
            print("NO")
            return

    trail = []

    def set_literal(lit):
        var = abs(lit)
        val = 1 if lit > 0 else 0
        assign[var] = val
        trail.append(lit)

        # Update sat
        sat_list = pos_occ[var] if val == 1 else neg_occ[var]
        for cid in sat_list:
            num_sat[cid] += 1

        # Update unassigned
        unsat_list = neg_occ[var] if val == 1 else pos_occ[var]
        for cid in unsat_list:
            num_unassigned[cid] -= 1

    def unset_literal(lit):
        var = abs(lit)
        val = 1 if lit > 0 else 0
        assign[var] = None

        sat_list = pos_occ[var] if val == 1 else neg_occ[var]
        for cid in sat_list:
            num_sat[cid] -= 1

        unsat_list = neg_occ[var] if val == 1 else pos_occ[var]
        for cid in unsat_list:
            num_unassigned[cid] += 1

    def unit_propagate():
        # Find unit clauses
        prop_idx = len(trail)
        # Check initial unit clauses or propagated ones
        while True:
            # Look for conflicts or units
            unit_found = False
            for cid in range(num_clauses):
                if num_sat[cid] == 0:
                    if num_unassigned[cid] == 0:
                        return False  # Conflict
                    if num_unassigned[cid] == 1:
                        # Find the unassigned literal
                        for lit in clauses[cid]:
                            v = abs(lit)
                            if assign[v] is None:
                                set_literal(lit)
                                unit_found = True
                                break
            if not unit_found:
                break
        return True

    def dpll():
        checkpoint = len(trail)

        # Propagate units
        # We need a robust unit propagation loop
        conflict = False
        queue = []

        # Find existing unit clauses
        for cid in range(num_clauses):
            if num_sat[cid] == 0:
                if num_unassigned[cid] == 0:
                    conflict = True
                    break
                elif num_unassigned[cid] == 1:
                    for lit in clauses[cid]:
                        v = abs(lit)
                        if assign[v] is None:
                            queue.append(lit)
                            break

        if not conflict:
            head = 0
            while head < len(queue):
                lit = queue[head]
                head += 1
                v = abs(lit)
                desired_val = 1 if lit > 0 else 0
                if assign[v] is not None:
                    if assign[v] != desired_val:
                        conflict = True
                        break
                    continue

                set_literal(lit)

                # Check newly affected clauses
                unsat_list = neg_occ[v] if desired_val == 1 else pos_occ[v]
                for cid in unsat_list:
                    if num_sat[cid] == 0:
                        if num_unassigned[cid] == 0:
                            conflict = True
                            break
                        elif num_unassigned[cid] == 1:
                            for l in clauses[cid]:
                                if assign[abs(l)] is None:
                                    queue.append(l)
                                    break
                if conflict:
                    break

        if conflict:
            while len(trail) > checkpoint:
                unset_literal(trail.pop())
            return False

        # Choose next variable using Jeroslow-Wang heuristic
        best_lit = 0
        max_score = -1.0
        power2 = [1.0, 0.5, 0.25, 0.125, 0.0625]

        # Check if all variables assigned
        unassigned_vars = [i for i in range(1, n + 1) if assign[i] is None]
        if not unassigned_vars:
            return True

        scores = {}
        for var in unassigned_vars:
            scores[var] = 0.0
            scores[-var] = 0.0

        for cid in range(num_clauses):
            if num_sat[cid] == 0:
                rem = num_unassigned[cid]
                weight = power2[rem] if rem < len(power2) else (2.0 ** -rem)
                for lit in clauses[cid]:
                    if assign[abs(lit)] is None:
                        scores[lit] += weight

        for var in unassigned_vars:
            sp = scores[var]
            sn = scores[-var]
            if sp + sn > max_score:
                max_score = sp + sn
                best_lit = var if sp >= sn else -var

        # Branch
        for lit in [best_lit, -best_lit]:
            sub_checkpoint = len(trail)
            set_literal(lit)
            if dpll():
                return True
            while len(trail) > sub_checkpoint:
                unset_literal(trail.pop())

        while len(trail) > checkpoint:
            unset_literal(trail.pop())
        return False

    if dpll():
        print("YES")
        res = [str(assign[i] if assign[i] is not None else 0) for i in range(1, n + 1)]
        print(" ".join(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()