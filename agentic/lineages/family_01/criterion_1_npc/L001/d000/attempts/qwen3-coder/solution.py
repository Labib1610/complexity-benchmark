from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list for the graph
    adj = defaultdict(list)
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # Try to 3-color the graph using backtracking with lex smallest order
    color = [-1] * n  # -1 means unassigned
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
        
        for c in [1, 2, 3]:
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = -1  # Backtrack
        return False
    
    if not backtrack(0):
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, color)))

solve()