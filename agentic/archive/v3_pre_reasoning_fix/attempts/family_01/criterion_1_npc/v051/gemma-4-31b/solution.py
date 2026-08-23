import sys

def solve():
    # Increase recursion depth for deep backtracking if necessary
    sys.setrecursionlimit(2000)
    
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
        
    # assignment stores the shift for each person (1 to n)
    assignment = [0] * (n + 1)
    
    def is_valid(u, color):
        for v in adj[u]:
            if assignment[v] == color:
                return False
        return True

    def backtrack(u):
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in order to find the lexicographically smallest sequence
        for color in (1, 2, 3):
            if is_valid(u, color):
                assignment[u] = color
                if backtrack(u + 1):
                    return True
                assignment[u] = 0
        return False

    # Since n is small (up to 40), simple backtracking with pruning/ordering 
    # might be slow in worst cases, but the lexicographical requirement 
    # forces a specific search order. 
    # However, for n=40, 3^40 is huge. But 3-coloring is NP-complete.
    # Given the constraints and the "lexicographically smallest" requirement,
    # we must try 1, then 2, then 3 for each node sequentially.
    
    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()