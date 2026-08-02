def solve():
    n, m = map(int, input().split())
    conflicts = []
    for _ in range(m):
        u, v = map(int, input().split())
        conflicts.append((u, v))
    
    def is_valid(assignment):
        for u, v in conflicts:
            if assignment[u-1] == assignment[v-1]:
                return False
        return True
    
    def find_assignment():
        assignment = [0] * n
        
        def backtrack(index):
            if index == n:
                if is_valid(assignment):
                    return True
                else:
                    return False
            
            for shift in range(1, 4):
                assignment[index] = shift
                if backtrack(index + 1):
                    return True
            
            return False
        
        if backtrack(0):
            return assignment
        else:
            return None
    
    assignment = find_assignment()
    
    if assignment is None:
        print("NO")
    else:
        print("YES")
        print(*assignment)

solve()