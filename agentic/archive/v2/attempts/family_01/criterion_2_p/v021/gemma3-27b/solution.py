def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u - 1, v - 1))

    def is_valid(assignment):
        for u, v in edges:
            if assignment[u] == assignment[v]:
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
            
            # Try channel 1
            assignment[index] = 1
            result = backtrack(index + 1)
            if result:
                return result
            
            # Try channel 2
            assignment[index] = 2
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