def solve():
    n, m = map(int, input().split())
    constraints = []
    for _ in range(m):
        l1, l2 = map(int, input().split())
        constraints.append((l1, l2))
    
    def check(assignment):
        for l1, l2 in constraints:
            if not ( (assignment[abs(l1) - 1] == 1 and l1 > 0) or (assignment[abs(l1) - 1] == 0 and l1 < 0) or
                     (assignment[abs(l2) - 1] == 1 and l2 > 0) or (assignment[abs(l2) - 1] == 0 and l2 < 0) ):
                return False
        return True

    for i in range(1 << n):
        assignment = []
        for j in range(n):
            if (i >> j) & 1:
                assignment.append(1)
            else:
                assignment.append(0)
        
        if check(assignment):
            print("YES")
            print(*assignment)
            return
    
    print("NO")

solve()