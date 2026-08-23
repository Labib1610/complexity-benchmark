def solve():
    import sys
    from collections import defaultdict

    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    incompatible_pairs = [tuple(map(int, line.split())) for line in data[1:m + 1]]
    
    # Create an adjacency list for the incompatibilities
    incompatibilities = defaultdict(set)
    
    for u, v in incompatible_pairs:
        incompatibilities[u].add(v)
        incompatibilities[v].add(u)
    
    # Result shifts for workers
    shifts = [0] * (n + 1)  # shifts[0] is unused, using 1-based indexing

    def is_valid(worker, shift):
        for incompatible in incompatibilities[worker]:
            if shifts[incompatible] == shift:
                return False
        return True

    def assign_shifts(worker):
        if worker > n:
            return True  # All workers have been assigned
        
        for shift in range(1, 4):  # Try shifts 1, 2, 3
            if is_valid(worker, shift):
                shifts[worker] = shift
                if assign_shifts(worker + 1):
                    return True
                shifts[worker] = 0  # Backtrack

        return False
    
    if assign_shifts(1):
        print("YES")
        print(" ".join(map(str, shifts[1:])))
    else:
        print("NO")