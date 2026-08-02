import sys

def solve():
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

    # Assignment array: 0 means unassigned
    assignment = [0] * (n + 1)

    def is_valid(node, color):
        for neighbor in adj[node]:
            if assignment[neighbor] == color:
                return False
        return True

    def backtrack(node):
        if node > n:
            return True
        
        # Try colors 1, 2, 3 in order for lexicographical minimum
        for color in [1, 2, 3]:
            if is_valid(node, color):
                assignment[node] = color
                if backtrack(node + 1):
                    return True
                assignment[node] = 0
        return False

    # Since n is small (up to 40), a simple backtracking with 
    # pruning or efficient check might work. However, 3-coloring 
    # is NP-complete. Given n=40, standard backtracking might be slow 
    # without heuristics, but let's try the basic approach first.
    # To optimize, we can use a bitmask or a more advanced check.
    
    # To improve the search, we can use the fact that we need the 
    # lexicographically smallest solution.
    
    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    # Increase recursion depth for deep backtracking trees
    sys.setrecursionlimit(2000)
    solve()