def solve():
    n, m = map(int, input().split())
    incompatibilities = []
    for _ in range(m):
        u, v = map(int, input().split())
        incompatibilities.append((u, v))

    def is_valid(assignment):
        for u, v in incompatibilities:
            if assignment[u-1] == assignment[v-1]:
                return False
        return True

    def find_assignment():
        assignment = [0] * n
        
        def backtrack(task_index):
            if task_index == n:
                if is_valid(assignment):
                    return assignment
                else:
                    return None
            
            for block in range(1, 4):
                assignment[task_index] = block
                result = backtrack(task_index + 1)
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