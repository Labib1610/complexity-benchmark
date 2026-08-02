import sys

def solve():
    # Set recursion limit for safety, though n=40 is small
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
        v = int(input_data[ptr+1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
        
    # We need the lexicographically smallest assignment.
    # We can use backtracking with pruning.
    # Since n=40 is small, a simple DFS with pruning might work, 
    # but 3^40 is too large. However, the constraints on graph coloring
    # for small n often allow backtracking to find the first solution quickly.
    
    assignment = [0] * (n + 1)
    
    def is_valid(u, color):
        for v in adj[u]:
            if assignment[v] == color:
                return False
        return True

    def backtrack(u):
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in order to ensure lexicographical smallest result
        for color in range(1, 4):
            if is_valid(u, color):
                assignment[u] = color
                if backtrack(u + 1):
                    return True
                assignment[u] = 0
        return False

    # For n=40, simple backtracking might be too slow for some cases.
    # But the problem asks for the lexicographically smallest, meaning
    # we must try colors in order 1, 2, 3 for operator 1, then 2, etc.
    # To optimize, we could use a more advanced 3-coloring algorithm, 
    # but given the constraints and the "lexicographically smallest" requirement,
    # standard backtracking is the most direct approach.
    
    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()