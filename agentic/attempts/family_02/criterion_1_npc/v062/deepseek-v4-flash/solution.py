import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    clauses = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        clauses.append((a, b, c))
    
    val = [-1] * (n + 1)
    
    # returns True if assignment consistent, False otherwise
    def propagate():
        changed = True
        while changed:
            changed = False
            for (a, b, c) in clauses:
                # count true and false literals
                true_lits = []
                false_lits = []
                unknown_lits = []
                for lit in (a, b, c):
                    var = abs(lit)
                    need = 1 if lit > 0 else 0
                    if val[var] == -1:
                        unknown_lits.append(lit)
                    elif val[var] == need:
                        true_lits.append(lit)
                    else:
                        false_lits.append(lit)
                if true_lits:
                    continue  # already satisfied
                # none true, so if 2 false -> set third true
                if len(false_lits) == 2 and len(unknown_lits) == 1:
                    lit = unknown_lits[0]
                    var = abs(lit)
                    need = 1 if lit > 0 else 0
                    if val[var] == -1:
                        val[var] = need
                        changed = True
                    elif val[var] != need:
                        return False
                elif len(false_lits) == 3:
                    return False
        return True
    
    def backtrack():
        if not propagate():
            return False
        # find unassigned var
        for i in range(1, n+1):
            if val[i] == -1:
                # try 0 and 1
                for v in (0, 1):
                    val[i] = v
                    if backtrack():
                        return True
                    val[i] = -1
                return False
        # no unassigned variables, check all satisfied
        for (a,b,c) in clauses:
            ok = False
            for lit in (a,b,c):
                var = abs(lit)
                need = 1 if lit > 0 else 0
                if val[var] == need:
                    ok = True
                    break
            if not ok:
                return False
        return True
    
    if backtrack():
        print("YES")
        print(" ".join(str(val[i]) for i in range(1, n+1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()