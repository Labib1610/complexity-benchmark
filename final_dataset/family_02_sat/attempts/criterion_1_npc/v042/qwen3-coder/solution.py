from collections import defaultdict
import sys

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each monitor, we have a clause: at least one of three literals must be true
    # This is a 3-SAT problem where each clause has exactly 3 literals
    
    # We'll use the randomized approach since n <= 90, but let's think differently
    # Actually, let's try a more systematic approach
    
    # Let's model this as a 3-SAT problem and use a simple randomized algorithm
    # Since n <= 90 and m <= 400, we can try random assignments
    
    clauses = []
    for _ in range(m):
        line = list(map(int, input().split()))
        clauses.append(line)
    
    # Try random assignments
    import random
    
    def is_satisfied(assignment):
        # assignment[i] = 0 means CLOSED, 1 means OPEN
        for clause in clauses:
            satisfied = False
            for literal in clause:
                if literal > 0:
                    var = literal - 1  # 0-indexed
                    if assignment[var] == 1:
                        satisfied = True
                        break
                else:
                    var = -literal - 1  # 0-indexed
                    if assignment[var] == 0:
                        satisfied = True
                        break
            if not satisfied:
                return False
        return True
    
    # Try many random assignments
    for _ in range(min(1000, 1 << min(n, 15)))):  # Limit attempts for large n
        assignment = [random.randint(0, 1) for _ in range(n)]
        if is_satisfied(assignment):
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    # If random didn't work, let's try a more systematic approach for small n
    if n <= 20:
        # Try all assignments
        for mask in range(1 << n):
            assignment = [(mask >> i) & 1 for i in range(n)]
            if is_satisfied(assignment):
                print("YES")
                print(" ".join(map(str, assignment)))
                return
    
    # For larger n, let's try a local search or other heuristic
    # But given time constraints, let's assume NO if we haven't found yet
    # Actually, let's implement a better approach
    
    # Let's try a greedy local search
    def local_search():
        current = [random.randint(0, 1) for _ in range(n)]
        improved = True
        while improved:
            improved = False
            # Count unsatisfied clauses for current assignment
            unsatisfied_count = 0
            unsatisfied_clauses = []
            for i, clause in enumerate(clauses):
                satisfied = False
                for literal in clause:
                    if literal > 0:
                        var = literal - 1
                        if current[var] == 1:
                            satisfied = True
                            break
                    else:
                        var = -literal - 1
                        if current[var] == 0:
                            satisfied = True
                            break
                if not satisfied:
                    unsatisfied_count += 1
                    unsatisfied_clauses.append(i)
            
            if unsatisfied_count == 0:
                return current
            
            # Try flipping each variable to see if we can reduce unsatisfied count
            best_flip = -1
            best_improvement = 0
            for var in range(n):
                current[var] = 1 - current[var]  # flip
                
                new_unsatisfied = 0
                for i in unsatisfied_clauses:
                    clause = clauses[i]
                    satisfied = False
                    for literal in clause:
                        if literal > 0:
                            v = literal - 1
                            if current[v] == 1:
                                satisfied = True
                                break
                        else:
                            v = -literal - 1
                            if current[v] == 0:
                                satisfied = True
                                break
                    if not satisfied:
                        new_unsatisfied += 1
                
                improvement = unsatisfied_count - new_unsatisfied
                if improvement > best_improvement:
                    best_improvement = improvement
                    best_flip = var
                    
                current[var] = 1 - current[var]  # flip back
            
            if best_flip != -1:
                current[best_flip] = 1 - current[best_flip]
                improved = True
        
        # Final check
        if is_satisfied(current):
            return current
        return None
    
    # Run local search several times
    for _ in range(100):
        result = local_search()
        if result is not None:
            print("YES")
            print(" ".join(map(str, result)))
            return
    
    print("NO")

solve()