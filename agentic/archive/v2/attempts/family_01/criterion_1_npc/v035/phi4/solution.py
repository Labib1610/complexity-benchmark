from sys import stdin, stdout

def can_assign_shifts(n, m, incompatible_pairs):
    # Create adjacency matrix for incompatible pairs
    adj = [[False] * n for _ in range(n)]
    for u, v in incompatible_pairs:
        adj[u - 1][v - 1] = True
        adj[v - 1][u - 1] = True

    def is_valid_assignment(shifts):
        # Check if current assignment of shifts is valid
        for i in range(n):
            for j in range(i + 1, n):
                if adj[i][j] and shifts[i] == shifts[j]:
                    return False
        return True

    def backtrack(index):
        if index == n:
            # All workers are assigned a shift
            return True
        
        for shift in [1, 2, 3]:
            shifts[index] = shift
            if is_valid_assignment(shifts):
                if backtrack(index + 1):
                    return True
        shifts[index] = 0
        return False

    # Initialize shifts array
    shifts = [0] * n

    if not backtrack(0):
        return "NO"
    
    result = ["YES"] + list(map(str, shifts))
    return "\n".join(result)

# Read input
input_data = stdin.read().strip().split()
n, m = int(input_data[0]), int(input_data[1])
incompatible_pairs = []
index = 2
for _ in range(m):
    u, v = int(input_data[index]), int(input_data[index + 1])
    incompatible_pairs.append((u, v))
    index += 2

# Compute and print the result
stdout.write(can_assign_shifts(n, m, incompatible_pairs) + '\n')