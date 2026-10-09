def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Create adjacency list for conflicts
    conflicts = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        conflicts[u].append(v)
        conflicts[v].append(u)
        idx += 2
    
    # Try all possible assignments in lexicographical order
    assignment = [0] * (n + 1)  # 1-indexed
    
    def is_valid(asset, fund):
        for neighbor in conflicts[asset]:
            if assignment[neighbor] == fund:
                return False
        return True
    
    def backtrack(asset):
        if asset > n:
            return True
            
        for fund in [1, 2, 3]:
            if is_valid(asset, fund):
                assignment[asset] = fund
                if backtrack(asset + 1):
                    return True
                assignment[asset] = 0
        return False
    
    if backtrack(1):
        print("YES")
        print(" ".join(map(str, assignment[1:])))
    else:
        print("NO")

solve()