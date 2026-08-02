def solve():
    n, m = map(int, input().split())
    conflicts = []
    for _ in range(m):
        u, v = map(int, input().split())
        conflicts.append((u - 1, v - 1))

    def is_valid(assignment):
        for u, v in conflicts:
            if assignment[u] == assignment[v]:
                return False
        return True

    def find_assignment(index, current_assignment):
        if index == n:
            if is_valid(current_assignment):
                return current_assignment
            else:
                return None

        for shift in range(1, 4):
            result = find_assignment(index + 1, current_assignment + [shift])
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