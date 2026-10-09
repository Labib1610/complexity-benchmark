import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    clauses = []
    for _ in range(m):
        f1, f2, f3 = map(int, input().split())
        clause = []
        for f in (f1, f2, f3):
            var = abs(f) - 1
            if f > 0:
                clause.append(var)
            else:
                clause.append(~var)
        clauses.append(clause)
    
    # We need to find assignment to n boolean vars such that each clause has at least one true literal.
    # This is 3-SAT, but with small constraints (n <= 90, m <= 400, total literals <= 1200).
    # Use DPLL with unit propagation and pure literal elimination.
    
    assignment = [None] * n
    
    def propagate(clauses, assignment):
        changed = True
        while changed:
            changed = False
            # unit propagation
            for clause in clauses:
                unassigned = []
                satisfied = False
                for lit in clause:
                    var = lit if lit >= 0 else ~lit
                    val = assignment[var]
                    if val is not None:
                        if (lit >= 0 and val == 1) or (lit < 0 and val == 0):
                            satisfied = True
                            break
                    else:
                        unassigned.append(lit)
                if satisfied:
                    continue
                if len(unassigned) == 0:
                    return False
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = lit if lit >= 0 else ~lit
                    val = 1 if lit >= 0 else 0
                    if assignment[var] is not None and assignment[var] != val:
                        return False
                    if assignment[var] is None:
                        assignment[var] = val
                        changed = True
        return True
    
    def pure_literal_elimination(clauses, assignment):
        # find pure literals
        pos = set()
        neg = set()
        for clause in clauses:
            for lit in clause:
                var = lit if lit >= 0 else ~lit
                if assignment[var] is not None:
                    continue
                if lit >= 0:
                    pos.add(var)
                else:
                    neg.add(var)
        pure = (pos - neg) | (neg - pos)
        for var in pure:
            if assignment[var] is None:
                assignment[var] = 1 if var in pos else 0
    
    def simplify(clauses, assignment):
        new_clauses = []
        for clause in clauses:
            satisfied = False
            new_clause = []
            for lit in clause:
                var = lit if lit >= 0 else ~lit
                val = assignment[var]
                if val is not None:
                    if (lit >= 0 and val == 1) or (lit < 0 and val == 0):
                        satisfied = True
                        break
                else:
                    new_clause.append(lit)
            if not satisfied:
                if len(new_clause) == 0:
                    return None
                new_clauses.append(new_clause)
        return new_clauses
    
    def dpll(clauses, assignment):
        # simplify
        clauses = simplify(clauses, assignment)
        if clauses is None:
            return False
        if not clauses:
            return True
        
        # unit propagation
        if not propagate(clauses, assignment):
            return False
        
        clauses = simplify(clauses, assignment)
        if clauses is None:
            return False
        if not clauses:
            return True
        
        # pure literal
        pure_literal_elimination(clauses, assignment)
        clauses = simplify(clauses, assignment)
        if clauses is None:
            return False
        if not clauses:
            return True
        
        # choose variable with most occurrences
        from collections import Counter
        cnt = Counter()
        for clause in clauses:
            for lit in clause:
                var = lit if lit >= 0 else ~lit
                cnt[var] += 1
        if not cnt:
            return True
        var = max(cnt, key=cnt.get)
        
        # try true
        assignment[var] = 1
        if dpll(clauses, assignment):
            return True
        assignment[var] = 0
        if dpll(clauses, assignment):
            return True
        assignment[var] = None
        return False
    
    if dpll(clauses, assignment):
        print("YES")
        print(" ".join(str(1 if x == 1 else 0) for x in assignment))
    else:
        print("NO")

if __name__ == "__main__":
    solve()