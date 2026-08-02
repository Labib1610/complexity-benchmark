import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    assignment = [0] * (n + 1)
    
    def is_valid(node, band):
        for neighbor in adj[node]:
            if assignment[neighbor] == band:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
        
        for band in range(1, 4):
            if is_valid(node, band):
                assignment[node] = band
                if backtrack(node + 1):
                    return True
                assignment[node] = 0
        return False
    
    # Since n <= 40, simple backtracking might be slow if not careful.
    # However, for 3-coloring, the search space is limited by constraints.
    # The problem asks for the lexicographically smallest assignment.
    # We can greedily try 1, 2, 3 for each node in order.
    
    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

solve()