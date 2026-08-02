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
    
    def find_lexicographically_smallest_assignment():
        for i in range(1 << n):
            assignment = []
            for j in range(n):
                if (i >> j) & 1:
                    assignment.append(1)
                else:
                    assignment.append(2)
            
            if is_valid(assignment):
                return assignment
        return None
    
    assignment = find_lexicographically_smallest_assignment()
    
    if assignment is None:
        print("NO")
    else:
        print("YES")
        print(*assignment)

solve()