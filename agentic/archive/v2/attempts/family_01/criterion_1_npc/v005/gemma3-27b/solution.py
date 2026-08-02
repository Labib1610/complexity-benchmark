def solve():
    n, m = map(int, input().split())
    incompatible = []
    for _ in range(m):
        u, v = map(int, input().split())
        incompatible.append((u, v))

    assignment = [0] * n

    def is_valid(worker, slot):
        for u, v in incompatible:
            if (u == worker + 1 and assignment[v - 1] == slot) or \
               (v == worker + 1 and assignment[u - 1] == slot):
                return False
        return True

    def backtrack(worker):
        if worker == n:
            return True

        for slot in range(1, 4):
            if is_valid(worker, slot):
                assignment[worker] = slot
                if backtrack(worker + 1):
                    return True
                assignment[worker] = 0  # Backtrack

        return False

    if backtrack(0):
        print("YES")
        print(*assignment)
    else:
        print("NO")

solve()