def solve():
    n, m = map(int, input().split())
    incompatible = []
    for _ in range(m):
        u, v = map(int, input().split())
        incompatible.append((u, v))
    
    def is_valid(assignment):
        for u, v in incompatible:
            if assignment[u-1] == assignment[v-1]:
                return False
        return True
    
    def find_assignment(index, assignment):
        if index == n:
            if is_valid(assignment):
                return assignment
            else:
                return None
        
        for vault in [1, 2, 3]:
            assignment[index] = vault
            result = find_assignment(index + 1, assignment)
            if result:
                return result
        
        return None
    
    assignment = [0] * n
    result = find_assignment(0, assignment)
    
    if result:
        print("YES")
        print(*result)
    else:
        print("NO")

solve()