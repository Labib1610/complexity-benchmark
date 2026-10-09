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

    # Each rule forbids exactly one assignment to its 3 referenced switches:
    # the one where all three conditions are contradicted.
    # We use backtracking with forward checking over switches 1..n.

    # Precompute for each switch the list of rules it participates in.
    rule_of_switch = [[] for _ in range(n+1)]
    for r_idx, (a, b, c) in enumerate(rules):
        for v in (a, b, c):
            sw = abs(v)
            rule_of_switch[sw].append(r_idx)

    # For each rule, store the forbidden pattern as a dict switch->bit
    forbidden = []
    for a, b, c in rules:
        d = {}
        d[abs(a)] = 1 if a < 0 else 0   # contradicted means opposite of expected
        d[abs(b)] = 1 if b < 0 else 0
        d[abs(c)] = 1 if c < 0 else 0
        forbidden.append(d)

    # Track how many conditions of each rule are already contradicted by current assignment.
    contradicted_count = [0]*m
    # Track which switches in each rule are already assigned.
    assigned_count = [0]*m
    assignment = [0]*(n+1)
    assigned = [False]*(n+1)

    # Order switches by number of rules they appear in (most constrained first).
    order = sorted(range(1, n+1), key=lambda s: -len(rule_of_switch[s]))

    def backtrack(pos):
        if pos == len(order):
            return True
        sw = order[pos]
        for val in (0, 1):
            ok = True
            affected = []
            for r_idx in rule_of_switch[sw]:
                if forbidden[r_idx].get(sw) == val:
                    contradicted_count[r_idx] += 1
                    affected.append(r_idx)
                assigned_count[r_idx] += 1
                # If all 3 switches of this rule are assigned and all 3 contradicted -> violation
                if assigned_count[r_idx] == 3 and contradicted_count[r_idx] == 3:
                    ok = False
            if ok:
                assignment[sw] = val
                assigned[sw] = True
                if backtrack(pos+1):
                    return True
                assigned[sw] = False
            # undo
            for r_idx in rule_of_switch[sw]:
                if forbidden[r_idx].get(sw) == val:
                    contradicted_count[r_idx] -= 1
                assigned_count[r_idx] -= 1
        return False

    if backtrack(0):
        out = ["YES"]
        out.append(" ".join(str(assignment[i]) for i in range(1, n+1)))
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()