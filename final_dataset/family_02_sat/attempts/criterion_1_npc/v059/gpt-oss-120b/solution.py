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
        clause = [int(next(it)), int(next(it)), int(next(it))]
        clauses.append(clause)

    # DPLL SAT solver
    def dpll(clauses, assign):
        # unit propagation
        while True:
            unit = None
            for c in clauses:
                if len(c) == 0:
                    return None
                if len(c) == 1:
                    unit = c[0]
                    break
            if unit is None:
                break
            var = abs(unit)
            val = unit > 0
            if var in assign:
                if assign[var] != val:
                    return None
            assign[var] = val
            new_clauses = []
            for c in clauses:
                if unit in c:
                    continue
                if -unit in c:
                    nc = [l for l in c if l != -unit]
                    new_clauses.append(nc)
                else:
                    new_clauses.append(c)
            clauses = new_clauses

        # pure literal elimination
        while True:
            counts = {}
            for c in clauses:
                for l in c:
                    counts[l] = counts.get(l, 0) + 1
            pure = None
            for l in counts:
                if -l not in counts:
                    pure = l
                    break
            if pure is None:
                break
            var = abs(pure)
            val = pure > 0
            if var in assign:
                if assign[var] != val:
                    return None
            assign[var] = val
            new_clauses = []
            for c in clauses:
                if pure in c:
                    continue
                new_clauses.append(c)
            clauses = new_clauses

        if not clauses:
            return assign

        # choose variable (most frequent)
        freq = {}
        for c in clauses:
            for l in c:
                v = abs(l)
                freq[v] = freq.get(v, 0) + 1
        var = max(freq, key=freq.get)
        for val in (True, False):
            lit = var if val else -var
            new_assign = assign.copy()
            new_assign[var] = val
            new_clauses = []
            conflict = False
            for c in clauses:
                if lit in c:
                    continue
                if -lit in c:
                    nc = [l for l in c if l != -lit]
                    if not nc:
                        conflict = True
                        break
                    new_clauses.append(nc)
                else:
                    new_clauses.append(c)
            if conflict:
                continue
            res = dpll(new_clauses, new_assign)
            if res is not None:
                return res
        return None

    result = dpll(clauses, {})
    if result is None:
        print("NO")
    else:
        print("YES")
        out = []
        for i in range(1, n + 1):
            out.append('1' if result.get(i, False) else '0')
        print(' '.join(out))

if __name__ == "__main__":
    solve()