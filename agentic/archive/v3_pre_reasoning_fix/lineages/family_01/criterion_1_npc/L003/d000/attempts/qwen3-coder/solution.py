from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list for the graph
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Try to color the graph with 3 colors using backtracking
    # Colors: 1, 2, 3 (work periods)
    colors = [0] * (n + 1)  # colors[i] represents the color of employee i
    
    def is_valid(node, color):
        # Check if assigning 'color' to 'node' is valid
        for neighbor in adj[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for color in range(1, 4):  # Try colors 1, 2, 3 in order for lex smallest
            if is_valid(node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0  # Backtrack
                
        return False
    
    # Start backtracking from employee 1
    if backtrack(1):
        print("YES")
        print(*colors[1:])
    else:
        print("NO")

solve()