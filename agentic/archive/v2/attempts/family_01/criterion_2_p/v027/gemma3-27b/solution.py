def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    def is_valid(assignment):
        for u, v in edges:
            if assignment[u-1] == assignment[v-1]:
                return False
        return True
    
    def find_assignment():
        for i in range(2**n):
            assignment = []
            for j in range(n):
                if (i >> j) & 1:
                    assignment.append(1)
                else:
                    assignment.append(2)
            
            if is_valid(assignment):
                return assignment
        return None
    
    assignment = find_assignment()
    
    if assignment is None:
        print("NO")
    else:
        print("YES")
        print(*assignment)

solve()