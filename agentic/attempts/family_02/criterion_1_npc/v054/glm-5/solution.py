import sys
from random import randint

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    clauses = []
    for _ in range(m):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        c = int(input_data[idx]); idx += 1
        clauses.append((a, b, c))
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    max_restarts = 2000
    max_flips = 500
    
    for _ in range(max_restarts):
        assign = [randint(0, 1) for _ in range(n + 1)]
        
        for _ in range(max_flips):
            unsat = []
            for clause in clauses:
                a, b, c = clause
                va = assign[abs(a)] if a > 0 else 1 - assign[abs(a)]
                vb = assign[abs(b)] if b > 0 else 1 - assign[abs(b)]
                vc = assign[abs(c)] if c > 0 else 1 - assign[abs(c)]
                if not (va or vb or vc):
                    unsat.append(clause)
            
            if not unsat:
                print("YES")
                print(" ".join(str(assign[i]) for i in range(1, n + 1)))
                return
            
            clause = unsat[randint(0, len(unsat) - 1)]
            var_idx = randint(0, 2)
            var = abs(clause[var_idx])
            assign[var] = 1 - assign[var]
    
    print("NO")

solve()