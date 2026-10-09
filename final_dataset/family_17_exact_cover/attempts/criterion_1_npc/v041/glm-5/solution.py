import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    n = 3 * q
    triples = []
    idx = 2
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        triples.append((a, b, c))
    
    # Build adjacency: for each pair, list of triple indices containing that pair
    pair_to_triples = {}
    for ti, (a, b, c) in enumerate(triples):
        for x, y in ((a, b), (a, c), (b, c)):
            key = (x, y) if x < y else (y, x)
            pair_to_triples.setdefault(key, []).append(ti)
    
    # For each triple, list of conflicting triples (sharing at least one member)
    conflict = [set() for _ in range(t)]
    member_to_triples = {}
    for ti, (a, b, c) in enumerate(triples):
        for m in (a, b, c):
            member_to_triples.setdefault(m, []).append(ti)
    for m, lst in member_to_triples.items():
        L = len(lst)
        for i in range(L):
            for j in range(i+1, L):
                conflict[lst[i]].add(lst[j])
                conflict[lst[j]].add(lst[i])
    
    # Greedy with conflict tracking
    used_member = [False] * (n + 1)
    used_triple = [False] * t
    chosen = []
    
    # Order triples by degree (number of conflicts) ascending to pick less constrained first
    order = sorted(range(t), key=lambda ti: len(conflict[ti]))
    
    for ti in order:
        a, b, c = triples[ti]
        if used_member[a] or used_member[b] or used_member[c]:
            continue
        used_member[a] = True
        used_member[b] = True
        used_member[c] = True
        used_triple[ti] = True
        chosen.append((a, b, c))
        if len(chosen) == q:
            break
    
    if len(chosen) == q:
        out = ["YES"]
        for a, b, c in chosen:
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out) + "\n")
        return
    
    # Fallback: exact cover via backtracking with pruning
    # Reset
    used_member = [False] * (n + 1)
    chosen = []
    
    # Precompute for each member the list of triples containing it
    member_triples = {}
    for ti, (a, b, c) in enumerate(triples):
        for m in (a, b, c):
            member_triples.setdefault(m, []).append(ti)
    
    # Sort members by fewest available triples (most constrained)
    members = list(range(1, n+1))
    
    def backtrack(count):
        if count == q:
            return True
        # Find unassigned member with fewest options
        best_m = -1
        best_opts = None
        best_len = 10**9
        for m in members:
            if used_member[m]:
                continue
            opts = []
            for ti in member_triples.get(m, []):
                a, b, c = triples[ti]
                if not used_member[a] and not used_member[b] and not used_member[c]:
                    opts.append(ti)
            if len(opts) < best_len:
                best_len = len(opts)
                best_m = m
                best_opts = opts
                if best_len == 0:
                    return False
                if best_len == 1:
                    break
        if best_m == -1:
            return count == q
        if best_len == 0:
            return False
        for ti in best_opts:
            a, b, c = triples[ti]
            used_member[a] = True
            used_member[b] = True
            used_member[c] = True
            chosen.append((a, b, c))
            if backtrack(count + 1):
                return True
            chosen.pop()
            used_member[a] = False
            used_member[b] = False
            used_member[c] = False
        return False
    
    if backtrack(0):
        out = ["YES"]
        for a, b, c in chosen:
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()