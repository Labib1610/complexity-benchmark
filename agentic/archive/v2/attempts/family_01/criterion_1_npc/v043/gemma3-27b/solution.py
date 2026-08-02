def solve():
    n, m = map(int, input().split())
    exclusions = []
    for _ in range(m):
        u, v = map(int, input().split())
        exclusions.append((u, v))

    def is_valid(assignment):
        for u, v in exclusions:
            if assignment[u - 1] == assignment[v - 1]:
                return False
        return True

    def find_lexicographically_smallest_assignment():
        assignment = [0] * n
        
        def backtrack(index):
            if index == n:
                if is_valid(assignment):
                    return assignment
                else:
                    return None

            for shift in [1, 2, 3]:
                assignment[index] = shift
                result = backtrack(index + 1)
                if result:
                    return result
            return None
        
        return backtrack(0)

    result = find_lexicographically_smallest_assignment()

    if result is None:
        print("NO")
    else:
        print("YES")
        print(*result)

solve()