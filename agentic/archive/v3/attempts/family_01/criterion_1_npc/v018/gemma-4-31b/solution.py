import sys

def solve():
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

    # State: assignments for workers 0 to n-1
    # We want the lexicographically smallest sequence, so we try 1, then 2, then 3 for each worker.
    assignment = [0] * n

    def is_safe(worker, color):
        for neighbor in adj[worker]:
            if neighbor < worker: # Only check already assigned workers
                if assignment[neighbor] == color:
                    return False
        return True

    # Since n is small (up to 40), a simple backtracking with pruning might be too slow
    # but we can optimize it. However, 3-coloring is NP-complete.
    # Given n=40, we need an efficient backtracking.
    
    def backtrack(worker):
        if worker == n:
            return True
        
        # Try colors in increasing order for lexicographical smallest result
        for color in [1, 2, 3]:
            if is_safe(worker, color):
                assignment[worker] = color
                # Heuristic: we could use forward checking or MRV, 
                # but for lexicographical smallest, we must process workers in order 0..n-1.
                if backtrack(worker + 1):
                    return True
                assignment[worker] = 0
        return False

    # To optimize for n=40, we can use bitmasking for constraints
    # constraints[i] will store which colors are taken by neighbors of i
    # But the order of assignment is fixed (0 to n-1).
    
    # Re-implementing with a slightly more optimized approach
    def solve_recursive(worker):
        if worker == n:
            return True
        
        # Find which colors are used by neighbors that are already assigned
        used = 0
        for neighbor in adj[worker]:
            if neighbor < worker:
                used |= (1 << assignment[neighbor])
        
        for color in [1, 2, 3]:
            if not (used & (1 << color)):
                assignment[worker] = color
                if solve_recursive(worker + 1):
                    return True
        
        assignment[worker] = 0
        return False

    if solve_recursive(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == "__main__":
    # Increase recursion depth for n=40
    sys.setrecursionlimit(2000)
    solve()