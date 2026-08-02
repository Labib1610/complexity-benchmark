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
            
            assignment[index] = 1
            if backtrack(index + 1):
                return True
            
            assignment[index] = 2
            if backtrack(index + 1):
                return True
            
            return False
        
        if backtrack(0):
            return assignment
        else:
            return None
    
    assignment = find_assignment()
    
    if assignment:
        print("YES")
        print(*assignment)
    else:
        print("NO")

solve()