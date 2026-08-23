import sys

# Increase recursion depth to handle deep recursion trees if necessary
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

    # Adjacency list. adj[u] will store neighbors v such that v > u.
    # This allows us to efficiently update masks for unassigned nodes.
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        # Store edge such that smaller index points to larger index
        if u < v:
            adj[u].append(v)
        else:
            adj[v].append(u)
            
    # mask[i] stores the bitmask of available colors for node i.
    # 1 -> bit 0 (1), 2 -> bit 1 (2), 3 -> bit 2 (4).
    # Initially all colors are available (1 | 2 | 4 = 7).
    mask = [7] * (n + 1)
    assignment = [0] * (n + 1)
    
    def backtrack(u):
        # If we have assigned all technicians, we found a solution
        if u > n:
            return True
        
        # If no colors are available for current technician u, backtrack
        if mask[u] == 0:
            return False
            
        # Try assigning colors 1, 2, 3 in order to find lexicographically smallest solution
        for c in (1, 2, 3):
            # Check if color c is allowed for u (based on already assigned neighbors v < u)
            # mask[u] is maintained by neighbors v < u
            if (mask[u] >> (c - 1)) & 1:
                
                # Forward checking: ensure assigning c to u doesn't leave any unassigned neighbor v > u with 0 options
                can_assign = True
                for v in adj[u]:
                    # Check if mask[v] becomes 0 if we remove color c
                    # mask[v] & ~(1 << (c - 1)) should be non-zero
                    if (mask[v] & ~(1 << (c - 1))) == 0:
                        can_assign = False
                        break
                
                if can_assign:
                    assignment[u] = c
                    
                    # Update masks for neighbors v > u
                    # We only need to update if the bit was set
                    updated_v = []
                    for v in adj[u]:
                        if mask[v] & (1 << (c - 1)):
                            mask[v] &= ~(1 << (c - 1))
                            updated_v.append(v)
                    
                    # Recurse to next technician
                    if backtrack(u + 1):
                        return True
                    
                    # Backtrack: restore masks
                    for v in updated_v:
                        mask[v] |= (1 << (c - 1))
                    
                    # Reset assignment
                    assignment[u] = 0
        
        return False

    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()