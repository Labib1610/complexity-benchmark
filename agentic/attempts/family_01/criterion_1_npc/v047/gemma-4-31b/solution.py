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

    # The condition is: if (u, v) is an incompatible pair, 
    # s_u * s_v must be in {2, 3, 6}.
    # Possible values for s_i are {1, 2, 3}.
    # Possible products:
    # 1*1 = 1 (Not allowed)
    # 1*2 = 2 (Allowed)
    # 1*3 = 3 (Allowed)
    # 2*2 = 4 (Not allowed)
    # 2*3 = 6 (Allowed)
    # 3*3 = 9 (Not allowed)
    # 
    # In other words:
    # If s_u = 1, s_v must be 2 or 3.
    # If s_u = 2, s_v must be 1 or 3.
    # If s_u = 3, s_v must be 1 or 2.
    # This is exactly the condition for a 3-coloring of the graph!
    # Two adjacent vertices must have different colors.
    
    # We need the lexicographically smallest sequence (s_1, s_2, ..., s_n).
    # Since n is small (up to 40), we can use backtracking with pruning.
    
    assignment = [0] * (n + 1)
    
    def is_valid(u, color):
        for v in adj[u]:
            if assignment[v] == color:
                return False
        return True

    def backtrack(u):
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in increasing order to ensure lexicographical smallest
        for color in [1, 2, 3]:
            if is_valid(u, color):
                assignment[u] = color
                if backtrack(u + 1):
                    return True
                assignment[u] = 0
        return False

    # To optimize backtracking for n=40, we can use basic pruning or 
    # a more sophisticated approach, but simple backtracking often works for n=40
    # if the graph is not a "hard" instance of 3-coloring.
    # Given the time limit of 2s, we can attempt standard backtracking.
    
    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()