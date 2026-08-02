def solve():
    import sys
    from collections import defaultdict
    
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    incompatibilities = defaultdict(list)
    
    for i in range(1, m + 1):
        u, v = map(int, data[i].split())
        incompatibilities[u - 1].append(v - 1)
        incompatibilities[v - 1].append(u - 1)

    # To store the assigned time windows
    assignment = [-1] * n
    
    def is_valid_assignment(operator, window):
        for neighbor in incompatibilities[operator]:
            if assignment[neighbor] == window:
                return False
        return True

    def assign(operator):
        if operator == n:
            return True  # All operators assigned
        
        for window in range(1, 4):  # Try windows 1, 2, 3
            if is_valid_assignment(operator, window):
                assignment[operator] = window
                if assign(operator + 1):
                    return True
                assignment[operator] = -1  # Backtrack
        
        return False

    if assign(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")