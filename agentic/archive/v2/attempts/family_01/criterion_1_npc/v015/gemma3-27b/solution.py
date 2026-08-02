def solve():
    n, m = map(int, input().split())
    incompatible = []
    for _ in range(m):
        u, v = map(int, input().split())
        incompatible.append((u, v))
    
    assignment = [0] * n
    
    def is_valid(tech, window):
        for i in range(tech):
            if assignment[i] == window:
                for u, v in incompatible:
                    if (u == tech + 1 and v == i + 1) or (v == tech + 1 and u == i + 1):
                        return False
        return True
    
    def backtrack(tech):
        if tech == n:
            return True
        
        for window in range(1, 4):
            if is_valid(tech, window):
                assignment[tech] = window
                if backtrack(tech + 1):
                    return True
                assignment[tech] = 0  # Backtrack
        
        return False
    
    if backtrack(0):
        print("YES")
        print(*assignment)
    else:
        print("NO")

solve()