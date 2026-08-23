def is_valid_assignment(n, edges, assignment):
    for u, v in edges:
        if assignment[u] == assignment[v]:
            return False
    return True

def dfs(n, edges, assignment, index):
    if index == n:
        return is_valid_assignment(n, edges, assignment)
    
    for freq in range(1, 4):  # Frequencies 1, 2, 3
        assignment[index] = freq
        if dfs(n, edges, assignment, index + 1):
            return True
        assignment[index] = 0  # Reset on backtrack

    return False

def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]
    
    assignment = [0] * n  # 0 means unassigned
    if dfs(n, edges, assignment, 0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

solve()