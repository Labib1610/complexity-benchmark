def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # Try all possible assignments in lexicographical order
    # We can use backtracking
    assignment = [0] * (n + 1)
    
    def is_valid(node, grid):
        for neighbor in adj[node]:
            if assignment[neighbor] == grid:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for grid in [1, 2, 3]:
            if is_valid(node, grid):
                assignment[node] = grid
                if backtrack(node + 1):
                    return True
                assignment[node] = 0
        return False
    
    if backtrack(1):
        print("YES")
        print(' '.join(map(str, assignment[1:])))
    else:
        print("NO")

solve()