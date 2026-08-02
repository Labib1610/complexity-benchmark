def solve():
    n, m = map(int, input().split())
    conflicts = []
    for _ in range(m):
        u, v = map(int, input().split())
        conflicts.append((u, v))
    
    schedule = [0] * n
    
    def is_valid(worker, shift):
        for i in range(worker):
            if schedule[i] == shift:
                for u, v in conflicts:
                    if (u == worker + 1 and v == i + 1) or (v == worker + 1 and u == i + 1):
                        return False
        return True
    
    def backtrack(worker):
        if worker == n:
            return True
        
        for shift in range(1, 4):
            if is_valid(worker, shift):
                schedule[worker] = shift
                if backtrack(worker + 1):
                    return True
                schedule[worker] = 0  # Backtrack
        
        return False
    
    if backtrack(0):
        print("YES")
        print(*schedule)
    else:
        print("NO")

solve()