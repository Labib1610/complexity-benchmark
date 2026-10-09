from collections import defaultdict
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    clauses = []
    idx = 2
    for _ in range(m):
        clause = []
        for _ in range(3):
            c = int(data[idx])
            idx += 1
            valve = abs(c)
            req = 1 if c > 0 else 0
            clause.append((valve, req))
        clauses.append(clause)
    
    # We will try all 2^n possible configurations
    # But since n <= 90, this is infeasible.
    # Instead, we model this as a 3-SAT problem and use a heuristic or brute-force for small n,
    # but given constraints, let's think differently.
    
    # Actually, let's try to solve it with a SAT approach or brute force for small n.
    # Since n <= 90, brute force is not feasible.
    # However, we can encode this as a 2-SAT-like problem or use backtracking with pruning.
    
    # Let's attempt a solution using backtracking with constraint propagation.
    
    # For each valve, we have two possible values: 0 (CLOSED) or 1 (OPEN)
    # We need to find an assignment such that for every clause (list of 3 conditions),
    # at least one condition is satisfied.
    
    # This is exactly 3-SAT, which is NP-complete.
    # But given the constraints, perhaps intended solution is to try all assignments for small n,
    # or use a SAT solver approach.
    
    # Given that n <= 90 and m <= 400, a full enumeration is impossible.
    # But let's recheck the limits. Maybe I misread.
    # Ah, n <= 90, that's too large for brute force.
    
    # Let's implement a backtracking solution with early termination.
    
    # Let's represent the state:
    # assignment[i] = 0 or 1 or None (unassigned)
    assignment = [None] * (n + 1)  # 1-indexed
    
    def is_clause_satisfied(clause):
        """Check if a clause is satisfied by current assignment"""
        for valve, req in clause:
            if assignment[valve] is not None:
                if assignment[valve] == req:
                    return True
        return False
    
    def is_current_state_valid():
        """Check if all assigned clauses are satisfied so far"""
        for clause in clauses:
            # If all variables in clause are assigned and none satisfy it, then invalid
            all_assigned = True
            satisfied = False
            for valve, req in clause:
                if assignment[valve] is None:
                    all_assigned = False
                    break
                elif assignment[valve] == req:
                    satisfied = True
                    break
            if all_assigned and not satisfied:
                return False
        return True
    
    def backtrack(var):
        if var == n + 1:
            # Check if all clauses are satisfied
            for clause in clauses:
                satisfied = False
                for valve, req in clause:
                    if assignment[valve] == req:
                        satisfied = True
                        break
                if not satisfied:
                    return False
            return True
        
        # Try assigning 0 (CLOSED)
        assignment[var] = 0
        if is_current_state_valid():
            if backtrack(var + 1):
                return True
        
        # Try assigning 1 (OPEN)
        assignment[var] = 1
        if is_current_state_valid():
            if backtrack(var + 1):
                return True
        
        # Backtrack
        assignment[var] = None
        return False
    
    # Start backtracking from variable 1
    if backtrack(1):
        print("YES")
        result = []
        for i in range(1, n + 1):
            result.append(str(assignment[i]))
        print(" ".join(result))
    else:
        print("NO")

if __name__ == "__main__":
    main()