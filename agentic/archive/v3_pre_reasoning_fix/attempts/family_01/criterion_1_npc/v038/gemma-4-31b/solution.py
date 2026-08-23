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
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # To find the lexicographically smallest sequence, we try values 1, 2, 3 in order
    # for each person from 1 to n.
    assignment = [0] * (n + 1)
    
    def is_valid(u, color):
        for v in adj[u]:
            if assignment[v] == color:
                return False
        return True

    # The constraints n <= 40 are small enough for backtracking with pruning,
    # although 3-coloring is NP-complete. However, for n=40, a well-implemented 
    # backtracking often works if the graph isn't specifically designed to be hard.
    
    def backtrack(u):
        if u > n:
            return True
        
        # Try colors in increasing order to ensure lexicographical smallest
        for color in (1, 2, 3):
            if is_valid(u, color):
                assignment[u] = color
                if backtrack(u + 1):
                    return True
                assignment[u] = 0
        return False

    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()