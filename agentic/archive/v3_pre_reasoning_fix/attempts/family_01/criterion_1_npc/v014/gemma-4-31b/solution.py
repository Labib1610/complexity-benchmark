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
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    # shift_assignment[i] stores the shift for worker i (0 if not assigned)
    shift_assignment = [0] * (n + 1)

    def is_safe(worker, shift):
        """Check if assigning 'shift' to 'worker' is compatible with neighbors."""
        for neighbor in adj[worker]:
            if shift_assignment[neighbor] == shift:
                return False
        return True

    def backtrack(worker):
        """Try assigning shifts 1, 2, 3 to workers sequentially to find lexicographically smallest."""
        if worker > n:
            return True
        
        # To ensure lexicographical smallest, try shift 1, then 2, then 3
        for shift in (1, 2, 3):
            if is_safe(worker, shift):
                shift_assignment[worker] = shift
                if backtrack(worker + 1):
                    return True
                shift_assignment[worker] = 0
        
        return False

    # The problem asks for the lexicographically smallest sequence (s1, s2, ..., sn).
    # Since we iterate through workers 1 to n and try shifts 1, 2, 3 in order,
    # the first valid assignment found will be the lexicographically smallest.
    if backtrack(1):
        print("YES")
        print(*(shift_assignment[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()