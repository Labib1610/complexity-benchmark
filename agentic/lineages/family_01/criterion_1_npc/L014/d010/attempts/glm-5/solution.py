import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Precompute L(x, y) for x, y in {1, 2, 3}
    # L(x, y) = (x-y)^4 - 5(x-y)^2 + 10
    L = [[0]*4 for _ in range(4)]
    for x in range(1, 4):
        for y in range(1, 4):
            d = x - y
            L[x][y] = d**4 - 5*d**2 + 10
    
    # DP: dp[mask] = minimum total load for assigned departments in mask
    # We build masks incrementally by department index
    INF = float('inf')
    dp = [INF] * (1 << n)
    parent = [(-1, -1)] * (1 << n)  # (prev_mask, agency_assigned)
    
    dp[0] = 0
    
    for mask in range(1 << n):
        if dp[mask] == INF:
            continue
        
        # Find first unassigned department
        i = 0
        while i < n and (mask >> i) & 1:
            i += 1
        
        if i == n:
            continue
        
        # Try assigning agency 1, 2, 3 to department i
        for agency in range(1, 4):
            new_mask = mask | (1 << i)
            added_load = 0
            
            # Calculate load contribution from edges between i and assigned departments
            for j in adj[i]:
                if (mask >> j) & 1:  # j is already assigned
                    # We need to know agency of j, but we don't store it directly
                    # We need to track assignments differently
                    pass
            
            # We need a different approach: track assignments
            # Let's use a different DP state
    
    # Alternative approach: since n <= 40, we can use meet-in-the-middle
    # Split into two halves of size n1 and n2
    # But tracking exact assignments for lexicographically smallest is complex
    
    # Simpler approach: backtracking with pruning
    # Since we need lexicographically smallest, try agencies in order 1, 2, 3
    # Use memoization with (mask, current_load) -> possible or not
    
    # Actually, let's use iterative DP with assignment tracking
    # dp[mask] = (min_load, assignment_tuple)
    
    # For n <= 40, 2^40 is too large, but we can use the constraint
    # that total load <= 6m, which limits the search space
    
    # Let's try backtracking with memoization
    assignment = [0] * n
    memo = {}
    
    def backtrack(i, current_load):
        if current_load > 6 * m:
            return False
        if i == n:
            return True
        
        key = (i, tuple(assignment[:i]))
        if key in memo:
            return memo[key]
        
        for agency in range(1, 4):
            assignment[i] = agency
            added = 0
            for j in adj[i]:
                if j < i:  # j is already assigned
                    added += L[agency][assignment[j]]
            if backtrack(i + 1, current_load + added):
                memo[key] = True
                return True
        
        memo[key] = False
        return False
    
    if backtrack(0, 0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

solve()