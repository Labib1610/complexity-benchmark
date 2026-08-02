import sys

def assign_slots(n, m, pairs):
    # Create adjacency matrix for incompatible pairs
    adj = [[False] * n for _ in range(n)]
    for u, v in pairs:
        adj[u - 1][v - 1] = True
        adj[v - 1][u - 1] = True

    def is_valid(assignment):
        # Check if current assignment is valid
        for i in range(n):
            for j in range(i + 1, n):
                if adj[i][j] and assignment[i] == assignment[j]:
                    return False
        return True

    def dfs(k):
        if k == n:
            return True
        
        for slot in [1, 2, 3]:
            assignment[k] = slot
            if is_valid(assignment):
                if dfs(k + 1):
                    return True
            assignment[k] = 0

        return False

    # Try to find a valid assignment using DFS
    assignment = [0] * n
    if dfs(0):
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

# Read input from standard input
input_data = sys.stdin.read().split()
n = int(input_data[0])
m = int(input_data[1])
pairs = [(int(input_data[i]), int(input_data[i + 1])) for i in range(2, len(input_data), 2)]

assign_slots(n, m, pairs)