import sys
import random

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        clauses.append((l1, l2, l3))
    
    # If no clauses, any assignment works
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # WalkSAT-like randomized search
    max_tries = 100
    max_flips = 300
    
    for _ in range(max_tries):
        # Random initial assignment
        assignment = [random.randint(0, 1) for _ in range(n)]
        
        for _ in range(max_flips):
            # Find unsatisfied clauses
            unsatisfied = []
            for clause in clauses:
                satisfied = False
                for lit in clause:
                    var = abs(lit) - 1
                    val = assignment[var]
                    if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                        satisfied = True
                        break
                if not satisfied:
                    unsatisfied.append(clause)
            
            if not unsatisfied:
                print("YES")
                print(" ".join(str(x) for x in assignment))
                return
            
            # Pick a random unsatisfied clause
            clause = random.choice(unsatisfied)
            
            # Choose a literal to flip
            # With some probability, pick a random literal; otherwise pick the one that minimizes unsatisfied clauses
            if random.random() < 0.5:
                lit = random.choice(clause)
            else:
                # Greedy: pick literal that minimizes unsatisfied count
                best_lit = None
                best_count = len(unsatisfied)
                for lit in clause:
                    var = abs(lit) - 1
                    # Flip this variable
                    assignment[var] ^= 1
                    # Count unsatisfied after flip
                    count = 0
                    for c in clauses:
                        sat = False
                        for l in c:
                            v = abs(l) - 1
                            val = assignment[v]
                            if (l > 0 and val == 1) or (l < 0 and val == 0):
                                sat = True
                                break
                        if not sat:
                            count += 1
                    # Revert
                    assignment[var] ^= 1
                    if count < best_count:
                        best_count = count
                        best_lit = lit
                if best_lit is None:
                    lit = random.choice(clause)
                else:
                    lit = best_lit
            
            # Flip the chosen variable
            var = abs(lit) - 1
            assignment[var] ^= 1
    
    print("NO")

if __name__ == "__main__":
    solve()