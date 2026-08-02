import sys

# Increase recursion depth to handle deep recursion if necessary
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # available[i] stores the bitmask of available colors for device i
    # Initially all colors {1, 2, 3} are available, represented by 111 (binary) = 7
    available = [7] * (n + 1)
    color = [0] * (n + 1)

    def backtrack(u):
        # Base case: all devices assigned
        if u > n:
            return True
        
        # If no colors available for current device, backtrack
        if available[u] == 0:
            return False
        
        # Try colors 1, 2, 3 in order to ensure lexicographically smallest solution
        for c in range(1, 4):
            mask = 1 << (c - 1)
            
            # Check if color c is available for u
            if not (available[u] & mask):
                continue
            
            # Forward checking: verify if assigning c to u makes any neighbor
            # (with index > u) have no available colors.
            # A neighbor v becomes invalid if available[v] == mask (only c was available)
            
            valid_assignment = True
            for v in adj[u]:
                if v > u:
                    if available[v] == mask:
                        valid_assignment = False
                        break
            
            if valid_assignment:
                # Assign color c to u
                color[u] = c
                
                # Update available colors for neighbors v > u
                # We must update before recursing
                for v in adj[u]:
                    if v > u:
                        available[v] &= ~mask
                
                # Recurse
                if backtrack(u + 1):
                    return True
                
                # Backtrack: restore available colors
                for v in adj[u]:
                    if v > u:
                        available[v] |= mask
                
                color[u] = 0
        
        return False

    if backtrack(1):
        print("YES")
        print(*(color[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()