def solve():
    n, m = map(int, input().split())
    conflicts = []
    for _ in range(m):
        u, v = map(int, input().split())
        conflicts.append((u, v))
    
    assignment = [0] * n
    
    def is_valid(worker, shift):
        for u, v in conflicts:
            if (u == worker + 1 and assignment[v - 1] == shift) or \
               (v == worker + 1 and assignment[u - 1] == shift):
                return False
        return True
    
    def backtrack(worker):
        if worker == n:
            return True
        
        for shift in range(1, 4):
            if is_valid(worker, shift):
                assignment[worker] = shift
                if backtrack(worker + 1):
                    return True
                assignment[worker] = 0  # Backtrack
        
        return False
    
    if backtrack(0):
        print("YES")
        print(*assignment)
    else:
        print("NO")

solve()