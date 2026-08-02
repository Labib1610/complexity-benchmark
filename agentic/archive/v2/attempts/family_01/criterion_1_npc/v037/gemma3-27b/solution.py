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
                    return assignment
                else:
                    return None
            
            for shift in range(1, 4):
                assignment[index] = shift
                result = backtrack(index + 1)
                if result:
                    return result
            
            return None
        
        return backtrack(0)
    
    assignment = find_assignment()
    
    if assignment:
        print("YES")
        print(*assignment)
    else:
        print("NO")

solve()