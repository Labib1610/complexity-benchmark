import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # Each protocol is a clause: (subsys, mode) OR (subsys, mode) OR (subsys, mode)
    # mode: 1 for ACTIVE, 0 for STANDBY
    # Positive c_i -> ACTIVE (1), Negative c_i -> STANDBY (0)
    clauses = []
    for _ in range(m):
        clause = []
        for _ in range(3):
            c = int(next(it))
            subsys = abs(c)
            mode = 1 if c > 0 else 0
            clause.append((subsys, mode))
        clauses.append(clause)
    
    # Try all 2^n configurations
    for mask in range(1 << n):
        valid = True
        for clause in clauses:
            clause_satisfied = False
            for subsys, mode in clause:
                # subsystem subsys (1-indexed) has state (mask >> (subsys-1)) & 1
                if ((mask >> (subsys - 1)) & 1) == mode:
                    clause_satisfied = True
                    break
            if not clause_satisfied:
                valid = False
                break
        if valid:
            print("YES")
            states = [str((mask >> i) & 1) for i in range(n)]
            print(" ".join(states))
            return
    
    print("NO")

if __name__ == "__main__":
    solve()