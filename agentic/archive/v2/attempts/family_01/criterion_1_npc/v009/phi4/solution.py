from itertools import permutations

def solve_shift_conflicts():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    conflicts = [tuple(map(int, data[i:i+2])) for i in range(2, 2 + 2*m, 2)]
    
    def is_valid_assignment(shifts):
        for u, v in conflicts:
            if shifts[u-1] == shifts[v-1]:
                return False
        return True
    
    min_shifts = None
    
    # Generate all possible shift assignments (3^n possibilities)
    for shifts in permutations(range(1, 4), n):
        if is_valid_assignment(shifts):
            if min_shifts is None or shifts < min_shifts:
                min_shifts = shifts
                
    if min_shifts:
        print("YES")
        print(*min_shifts)
    else:
        print("NO")

# The function solve_shift_conflicts reads from standard input and writes to standard output