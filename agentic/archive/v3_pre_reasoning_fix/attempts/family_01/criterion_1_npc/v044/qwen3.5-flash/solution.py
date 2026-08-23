import sys

# Increase recursion depth to handle N=40 comfortably
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency masks: adj[u] is a bitmask where the v-th bit is set if u and v are connected
    # Since n <= 40, bitwise operations are efficient.
    adj = [0] * n
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # masks[c] stores the bitmask of nodes assigned color c+1 (0-indexed color c)
    # We use a list to allow modification in the recursive function
    masks = [0, 0, 0]
    
    # ans array to store the assigned channel for each technician (1-based)
    ans = [0] * n
    
    # Depth First Search to find the lexicographically smallest assignment
    # We try to assign channel 1, then 2, then 3 to the current technician u.
    # This ensures that the first valid assignment found is lexicographically smallest.
    def dfs(u):
        # Base case: all technicians assigned
        if u == n:
            return True
        
        # Try assigning channel 1 (corresponding to mask index 0)
        # Check if any neighbor of u is already assigned channel 1
        if (masks[0] & adj[u]) == 0:
            masks[0] |= (1 << u)
            ans[u] = 1
            if dfs(u + 1):
                return True
            # Backtrack
            masks[0] &= ~(1 << u)
            
        # Try assigning channel 2 (corresponding to mask index 1)
        if (masks[1] & adj[u]) == 0:
            masks[1] |= (1 << u)
            ans[u] = 2
            if dfs(u + 1):
                return True
            # Backtrack
            masks[1] &= ~(1 << u)
            
        # Try assigning channel 3 (corresponding to mask index 2)
        if (masks[2] & adj[u]) == 0:
            masks[2] |= (1 << u)
            ans[u] = 3
            if dfs(u + 1):
                return True
            # Backtrack
            masks[2] &= ~(1 << u)
            
        return False

    if dfs(0):
        print("YES")
        print(*(ans))
    else:
        print("NO")

if __name__ == '__main__':
    solve()