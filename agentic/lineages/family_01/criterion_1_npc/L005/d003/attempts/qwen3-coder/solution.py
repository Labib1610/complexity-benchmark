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
    
    # Try all 3^n assignments in lexicographical order using backtracking
    assignment = [0] * (n + 1)
    
    def is_valid(node):
        for neighbor in adj[node]:
            if assignment[neighbor] != 0 and (assignment[node] ^ assignment[neighbor]) == 0:
                return False
        return True
    
    def backtrack(pos):
        if pos > n:
            return True
            
        for val in [1, 2, 3]:
            assignment[pos] = val
            if is_valid(pos):
                if backtrack(pos + 1):
                    return True
            assignment[pos] = 0
        return False
    
    if backtrack(1):
        print("YES")
        print(' '.join(map(str, assignment[1:])))
    else:
        print("NO")

solve()