def solve():
    n, m = map(int, input().split())
    reactive_pairs = []
    for _ in range(m):
        u, v = map(int, input().split())
        reactive_pairs.append((u, v))

    def is_safe(assignment):
        for u, v in reactive_pairs:
            if assignment[u-1] == assignment[v-1]:
                return False
        return True

    def find_assignment(index, current_assignment):
        if index == n:
            if is_safe(current_assignment):
                return current_assignment
            else:
                return None

        for unit in [1, 2, 3]:
            new_assignment = current_assignment[:]
            new_assignment[index] = unit
            result = find_assignment(index + 1, new_assignment)
            if result:
                return result

        return None

    assignment = find_assignment(0, [0] * n)

    if assignment:
        print("YES")
        print(*assignment)
    else:
        print("NO")

solve()