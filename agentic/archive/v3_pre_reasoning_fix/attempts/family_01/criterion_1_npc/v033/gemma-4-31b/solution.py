import sys

def solve():
    # Increase recursion depth for deep backtracking
    sys.setrecursionlimit(2000)
    
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    # current_assignment stores the channel for process 1 to n
    assignment = [0] * (n + 1)

    def is_valid(node, color):
        for neighbor in adj[node]:
            if assignment[neighbor] == color:
                return False
        return True

    def backtrack(node):
        if node > n:
            return True
        
        # Try colors 1, 2, 3 in increasing order to ensure lexicographical smallest
        for color in (1, 2, 3):
            if is_valid(node, color):
                assignment[node] = color
                if backtrack(node + 1):
                    return True
                assignment[node] = 0
        return False

    # The constraints n <= 40 are small enough for backtracking with pruning 
    # since we only have 3 colors (3-coloring problem is NP-complete, but n=40 
    # often passes if the graph isn't specifically designed to thwart simple DFS).
    # However, to be safer, we can use a slightly more optimized check or 
    # simple DFS as requested.
    
    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()