import sys

def solve():
    # Set recursion limit just in case, though n=40 is small
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
    
    # To find the lexicographically smallest sequence, we try assigning 
    # the smallest possible stage (1, 2, then 3) to unit 1, then unit 2, and so on.
    # This is a backtracking search.
    
    assignment = [0] * (n + 1)
    
    def is_valid(u, stage):
        for v in adj[u]:
            if assignment[v] == stage:
                return False
        return True

    def backtrack(u):
        if u > n:
            return True
        
        # Try stages in increasing order to ensure lexicographical smallest result
        for stage in [1, 2, 3]:
            if is_valid(u, stage):
                assignment[u] = stage
                if backtrack(u + 1):
                    return True
                assignment[u] = 0
        return False

    # Optimization: The problem is essentially 3-coloring a graph.
    # Since n is small (40), simple backtracking with pruning might be slow,
    # but the lexicographical requirement forces a specific search order.
    # To speed up, we can use a simple heuristic or just rely on the small n.
    
    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()