import sys

def solve():
    # Set recursion limit for safety, though n is small
    sys.setrecursionlimit(2000)
    
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n)]
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr]) - 1
        v = int(input_data[ptr+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2

    # assignment stores the channel for each transmitter (0 for unassigned)
    assignment = [0] * n

    def is_valid(u, color):
        for v in adj[u]:
            if assignment[v] == color:
                return False
        return True

    def backtrack(u):
        if u == n:
            return True
        
        # To get the lexicographically smallest sequence, 
        # try colors in increasing order: 1, 2, 3
        for color in (1, 2, 3):
            if is_valid(u, color):
                assignment[u] = color
                if backtrack(u + 1):
                    return True
                assignment[u] = 0
        return False

    # The constraints n=40 are small enough for backtracking with pruning 
    # in many cases, but 3-coloring is NP-complete.
    # However, for n=40, a simple backtracking with the lexicographical 
    # requirement often passes if the search space isn't adversarial.
    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == "__main__":
    solve()