import sys

def solve():
    # Set recursion limit just in case, though we use iterative/backtracking
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
        
    # assignment[i] will store the shift for member i (1, 2, or 3)
    assignment = [0] * (n + 1)
    
    def is_valid(u, shift):
        for v in adj[u]:
            if assignment[v] == shift:
                return False
        return True

    def backtrack(u):
        if u > n:
            return True
        
        # Try shifts 1, 2, 3 in order for lexicographical smallest result
        for shift in [1, 2, 3]:
            if is_valid(u, shift):
                assignment[u] = shift
                if backtrack(u + 1):
                    return True
                assignment[u] = 0
        return False

    # Since n is small (up to 40), a simple backtracking with pruning
    # might be slow in worst case (3^40), but the constraints on 3-coloring
    # are often tight enough that it works or fails fast.
    # However, to optimize for 3-coloring, we can use a more efficient approach.
    # Given n=40, we can use backtracking with a bit of heuristics or simply
    # try the smallest shift first.
    
    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()