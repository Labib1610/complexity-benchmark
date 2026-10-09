import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])

    # Convert literal from 1-based signed to 0-based:
    # +v -> 2*v, -v -> 2*v + 1
    def to_lit(x):
        v = abs(x)
        return 2 * v if x > 0 else 2 * v + 1

    clauses = []
    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx + 1])
        l3 = int(input_data[idx + 2])
        idx += 3

        raw = [to_lit(l1), to_lit(l2), to_lit(l3)]
        # Simplify clause: remove duplicates, check tautology
        s = set(raw)
        tautology = False
        for lit in s:
            if (lit ^ 1) in s:
                tautology = True
                break
        if tautology:
            continue
        c = list(s)
        clauses.append(c)

    # CDCL Solver setup
    # Variables: 1 to n
    num_lits = 2 * (n + 1)
    lit_val = [-1] * num_lits
    var_val = [-1] * (n + 1)
    var_level = [0] * (n + 1)
    var_reason = [None] * (n + 1)
    activity = [0.0] * (n + 1)
    var_inc = 1.0
    var_decay = 0.95

    watches = [[] for _ in range(num_lits)]
    decision_level = 0
    trail = []
    trail_lim = []

    def assign(lit, level, reason):
        v = lit >> 1
        var_val[v] = 1 if (lit & 1) == 0 else 0
        lit_val[lit] = 1
        lit_val[lit ^ 1] = 0
        var_level[v] = level
        var_reason[v] = reason
        trail.append(lit)

    def cancel_until(level):
        nonlocal decision_level
        while decision_level > level:
            lim = trail_lim.pop()
            while len(trail) > lim:
                p = trail.pop()
                v = p >> 1
                var_val[v] = -1
                lit_val[p] = -1
                lit_val[p ^ 1] = -1
                var_reason[v] = None
                var_level[v] = 0
            decision_level -= 1

    # Add initial clauses
    unit_queue = []
    all_clauses = []

    for c in clauses:
        if len(c) == 0:
            print("NO")
            return
        elif len(c) == 1:
            unit_queue.append(c[0])
        else:
            all_clauses.append(c)
            watches[c[0] ^ 1].append(c)
            watches[c[1] ^ 1].append(c)

    def propagate():
        nonlocal var_inc
        # We need a queue index in trail
        prop_idx = getattr(propagate, "qhead", 0)
        while prop_idx < len(trail):
            p = trail[prop_idx]
            prop_idx += 1
            propagate.qhead = prop_idx

            # p was set to True, so p^1 is False.
            # We must update clauses watching p^1.
            false_lit = p ^ 1
            ws = watches[false_lit]
            watches[false_lit] = []
            i = 0
            while i < len(ws):
                c = ws[i]
                # Ensure false_lit is at c[1]
                if c[0] == false_lit:
                    c[0], c[1] = c[1], c[0]

                # If c[0] is already True, clause is satisfied
                if lit_val[c[0]] == 1:
                    watches[false_lit].append(c)
                    i += 1
                    continue

                # Look for an alternative literal to watch
                found = False
                for k in range(2, len(c)):
                    if lit_val[c[k]] != 0:
                        c[1], c[k] = c[k], c[1]
                        watches[c[1] ^ 1].append(c)
                        found = True
                        break

                if found:
                    i += 1
                    continue

                # Did not find another literal to watch
                watches[false_lit].append(c)
                i += 1

                # If c[0] is False, we have a conflict
                if lit_val[c[0]] == 0:
                    # Put remaining clauses back into watches[false_lit]
                    while i < len(ws):
                        watches[false_lit].append(ws[i])
                        i += 1
                    return c
                else:
                    # Unit propagate c[0]
                    assign(c[0], decision_level, c)

        return None

    propagate.qhead = 0

    # Level 0 unit assignments
    for lit in unit_queue:
        if lit_val[lit] == 0:
            print("NO")
            return
        if lit_val[lit] == -1:
            assign(lit, 0, None)

    confl = propagate()
    if confl is not None:
        print("NO")
        return

    def analyze(confl):
        nonlocal var_inc
        learnt = []
        seen = [False] * (n + 1)
        counter = 0
        p = None
        c = confl
        idx = len(trail) - 1
        while True:
            for lit in c:
                v = lit >> 1
                if not seen[v] and var_level[v] > 0:
                    seen[v] = True
                    activity[v] += var_inc
                    if var_level[v] == decision_level:
                        counter += 1
                    else:
                        learnt.append(lit)
            while idx >= 0:
                p = trail[idx]
                idx -= 1
                if seen[p >> 1]:
                    break
            seen[p >> 1] = False
            counter -= 1
            if counter == 0:
                break
            c = var_reason[p >> 1]

        asserting_lit = p ^ 1
        learnt.insert(0, asserting_lit)

        bt_level = 0
        if len(learnt) > 1:
            max_i = 1
            for i in range(2, len(learnt)):
                if var_level[learnt[i] >> 1] > var_level[learnt[max_i] >> 1]:
                    max_i = i
            learnt[1], learnt[max_i] = learnt[max_i], learnt[1]
            bt_level = var_level[learnt[1] >> 1]

        var_inc /= var_decay
        return learnt, bt_level

    # Main CDCL loop
    while True:
        confl = propagate()
        if confl is not None:
            if decision_level == 0:
                print("NO")
                return
            learnt, bt_level = analyze(confl)
            cancel_until(bt_level)
            propagate.qhead = len(trail)

            if len(learnt) == 1:
                assign(learnt[0], 0, None)
            else:
                all_clauses.append(learnt)
                watches[learnt[0] ^ 1].append(learnt)
                watches[learnt[1] ^ 1].append(learnt)
                assign(learnt[0], bt_level, learnt)
            continue

        # Pick next decision variable
        best_v = None
        best_act = -1.0
        for v in range(1, n + 1):
            if var_val[v] == -1:
                if activity[v] > best_act:
                    best_act = activity[v]
                    best_v = v

        if best_v is None:
            # All variables assigned, SAT!
            print("YES")
            res = [var_val[v] if var_val[v] != -1 else 0 for v in range(1, n + 1)]
            print(*(res))
            return

        decision_level += 1
        trail_lim.append(len(trail))
        # Decide positive literal by default
        assign(2 * best_v, decision_level, None)


if __name__ == "__main__":
    solve()