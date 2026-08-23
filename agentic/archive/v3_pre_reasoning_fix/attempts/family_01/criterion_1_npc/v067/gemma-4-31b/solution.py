import sys

def solve():
    # Set recursion limit for deep backtracking
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

    # assignment[i] stores the shift for individual i (1-indexed)
    assignment = [0] * (n + 1)

    def is_valid(node, shift):
        for neighbor in adj[node]:
            if assignment[neighbor] == shift:
                return False
        return True

    def backtrack(node):
        if node > n:
            return True
        
        # To get the lexicographically smallest sequence, 
        # try shifts 1, 2, 3 in order.
        for shift in range(1, 4):
            if is_valid(node, shift):
                assignment[node] = shift
                if backtrack(node + 1):
                    return True
                assignment[node] = 0
        return False

    # For n=40, simple backtracking might be too slow, but 3-coloring is NP-complete.
    # However, the constraints and the "lexicographically smallest" requirement 
    # suggest a backtracking approach. To optimize, we can use a simple 
    # pruning or a more efficient check. 
    # Given n=40, we can try backtracking.
    
    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()