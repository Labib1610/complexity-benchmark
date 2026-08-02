def solve():
    n, m = map(int, input().split())
    incompatibilities = []
    for _ in range(m):
        u, v = map(int, input().split())
        incompatibilities.append((u, v))

    def is_valid(assignment):
        for u, v in incompatibilities:
            if assignment[u-1] * assignment[v-1] not in [2, 3, 6]:
                return False
        return True

    def find_assignment():
        import itertools
        
        for assignment in itertools.product([1, 2, 3], repeat=n):
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