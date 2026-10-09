def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    clauses = []
    index = 2
    for _ in range(m):
        clause = []
        for _ in range(3):
            lit = int(data[index])
            index += 1
            clause.append(lit)
        clauses.append(clause)
    
    # Try all 2^n assignments
    for mask in range(1 << n):
        assignment = [((mask >> i) & 1) for i in range(n)]
        satisfied = True
        
        for clause in clauses:
            clause_satisfied = False
            for lit in clause:
                if lit > 0:
                    var_index = lit - 1
                    if assignment[var_index] == 1:
                        clause_satisfied = True
                        break
                else:
                    var_index = -lit - 1
                    if assignment[var_index] == 0:
                        clause_satisfied = True
                        break
            if not clause_satisfied:
                satisfied = False
                break
        
        if satisfied:
            print("YES")
            print(' '.join(map(str, assignment)))
            return
    
    print("NO")

solve()