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

    def find_assignment(index, current_assignment):
        if index == n:
            if is_valid(current_assignment):
                return current_assignment
            else:
                return None
        
        for chamber in [1, 2]:
            result = find_assignment(index + 1, current_assignment + [chamber])
            if result:
                return result
        
        return None

    assignment = find_assignment(0, [])
    
    if assignment:
        print("YES")
        print(*assignment)
    else:
        print("NO")

solve()