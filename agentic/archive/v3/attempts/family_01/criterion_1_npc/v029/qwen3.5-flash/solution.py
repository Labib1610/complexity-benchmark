import sys

# Increase recursion depth to ensure deep recursion trees are handled, 
# although N=40 is well within the default limit.
sys.setrecursionlimit(2000)

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

    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
    
    # domain[i] stores the bitmask of allowed colors for vertex i
    # Colors 1, 2, 3 correspond to bits 0, 1, 2 respectively.
    # 7 (binary 111) means all colors are allowed initially.
    domain = [7] * (n + 1)
    ans = [0] * (n + 1)
    
    # Precompute neighbors that are strictly greater than u.
    # We only need to update constraints for vertices that have not been assigned yet (v > u).
    # This optimizes the forward checking step.
    adj_ge = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                adj_ge[u].append(v)
    
    # Backtracking function to find the lexicographically smallest assignment
    def backtrack(idx):
        # Base case: All vertices assigned successfully
        if idx == n + 1:
            return True
        
        # Optimization: If current vertex has no allowed colors (domain is 0), backtrack immediately
        if domain[idx] == 0:
            return False
        
        # Try colors 1, 2, 3 in ascending order to ensure lexicographically smallest solution
        for c in range(1, 4):
            # Check if color c is allowed for current vertex idx
            # (domain[idx] >> (c - 1)) & 1 checks if the (c-1)-th bit is set
            if (domain[idx] >> (c - 1)) & 1:
                
                # Assign color c to vertex idx
                ans[idx] = c
                
                # Forward checking: Update domains of neighbors v > idx
                mask = 1 << (c - 1)
                changed_indices = []
                valid_move = True
                
                for v in adj_ge[idx]:
                    # If color c is currently allowed for v (bit is set), remove it
                    if domain[v] & mask:
                        domain[v] &= ~mask
                        changed_indices.append(v)
                        # If a neighbor has no colors left, this path is invalid
                        if domain[v] == 0:
                            valid_move = False
                            break
                
                if valid_move:
                    # Recurse to the next vertex
                    if backtrack(idx + 1):
                        return True
                
                # Backtrack: Revert the changes to domains
                for v in changed_indices:
                    domain[v] |= mask
        
        return False

    # Start the backtracking from vertex 1
    if backtrack(1):
        print("YES")
        print(*(ans[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()