from itertools import combinations

def solve():
    n, m = map(int, input().split())
    if m == 0:
        print("YES")
        print(*([1] * n))
        return
    
    incompatibilities = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        incompatibilities[u].add(v)
        incompatibilities[v].add(u)

    def is_valid_assignment(assignment):
        for i in range(n):
            for j in incompatibilities[i]:
                if assignment[i] == assignment[j]:
                    return False
        return True

    shifts = [1, 2, 3]
    best_assignment = None

    for shift_combination in combinations(shifts * n, n):
        if sorted(shift_combination[:n]) != list(shift_combination[:n]):
            continue
        if is_valid_assignment(shift_combination):
            if best_assignment is None or shift_combination < best_assignment:
                best_assignment = shift_combination

    if best_assignment is not None:
        print("YES")
        print(*best_assignment)
    else:
        print("NO")

if __name__ == "__main__":
    solve()