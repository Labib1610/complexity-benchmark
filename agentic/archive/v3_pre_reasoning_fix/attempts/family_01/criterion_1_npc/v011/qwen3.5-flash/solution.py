import sys

# Increase recursion depth to handle N=40 safely, though 1000 is usually enough.
sys.setrecursionlimit(5000)

def solve():
    # Read all input from stdin
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
        
    # Precompute future adjacency list: neighbors > u
    # This allows us to quickly check constraints on unassigned nodes
    future_adj = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                future_adj[u].append(v)
    
    # avail[u] is a bitmask of available colors for station u
    # Bit 0 -> Color 1, Bit 1 -> Color 2, Bit 2 -> Color 3
    # Initially all colors are available for all stations
    avail = [7] * (n + 1) # 7 is binary 111
    
    # color[u] stores the assigned color for station u (0 if unassigned)
    # We don't strictly need this array for the logic, but it helps to debug or print
    # Actually, we need to output the assignment, so we can store it in a result array.
    res = [0] * (n + 1)
    
    # Backtracking function
    # u: current station we are trying to assign (from 1 to n)
    def backtrack(u):
        if u > n:
            return True
        
        # Iterate through possible colors 1, 2, 3 (bits 0, 1, 2)
        # We want lexicographically smallest, so we try 1, then 2, then 3.
        for bit in range(3):
            # Check if color (bit+1) is available for u
            # avail[u] contains colors compatible with already assigned neighbors (v < u)
            if (avail[u] >> bit) & 1:
                c = bit + 1
                
                # Check forward checking:
                # If we assign c to u, we must ensure that for all unassigned neighbors w > u:
                # w still has at least one valid color remaining.
                # i.e., avail[w] must not become 0 after removing c.
                
                valid_move = True
                changes = []
                
                for w in future_adj[u]:
                    # Check if c is currently available for w
                    if (avail[w] >> bit) & 1:
                        # c is available for w, so picking c for u will remove it from w's options
                        # If w only had c as an option, it will be left with 0 options -> Invalid
                        if avail[w] == (1 << bit):
                            valid_move = False
                            break
                        # Record this change to revert later
                        changes.append(w)
                
                if valid_move:
                    # Apply changes
                    for w in changes:
                        avail[w] &= ~(1 << bit)
                    
                    res[u] = c
                    
                    if backtrack(u + 1):
                        return True
                    
                    # Backtrack: revert changes
                    res[u] = 0
                    for w in changes:
                        avail[w] |= (1 << bit)
                        
        return False

    if backtrack(1):
        print("YES")
        print(*(res[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()