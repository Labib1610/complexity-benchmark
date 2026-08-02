def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    conflicts = defaultdict(set)
    
    for i in range(1, m + 1):
        u, v = map(int, data[i].split())
        conflicts[u - 1].add(v - 1)
        conflicts[v - 1].add(u - 1)

    # Try to assign shifts
    shifts = [-1] * n  # -1 means unassigned

    def assign_shifts(worker):
        if worker == n:
            return True  # All workers assigned

        if shifts[worker] != -1:
            return assign_shifts(worker + 1)

        for s in range(3):  # Trying shifts 0, 1, 2
            can_assign = True
            for conflict in conflicts[worker]:
                if shifts[conflict] == s:
                    can_assign = False
                    break
            
            if can_assign:
                shifts[worker] = s
                if assign_shifts(worker + 1):
                    return True
                shifts[worker] = -1  # Backtrack

        return False

    if assign_shifts(0):
        print("YES")
        print(" ".join(str(s + 1) for s in shifts))
    else:
        print("NO")

if __name__ == "__main__":
    main()