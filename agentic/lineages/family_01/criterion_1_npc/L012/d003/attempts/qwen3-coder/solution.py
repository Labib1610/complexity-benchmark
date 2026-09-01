def solve():
    import sys
    from collections import defaultdict

    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list
    adj = defaultdict(list)
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-indexed
        v = int(data[idx+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    # Try all 3^n assignments in lexicographical order
    # But we can do better with backtracking
    assignment = [0] * n  # 0 means unassigned

    def is_valid(node, color):
        for neighbor in adj[node]:
            if assignment[neighbor] == color:
                return False
        return True

    def backtrack(node):
        if node == n:
            return True
        
        for color in [1, 2, 3]:
            if is_valid(node, color):
                assignment[node] = color
                if backtrack(node + 1):
                    return True
                assignment[node] = 0
        return False

    if backtrack(0):
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

solve()