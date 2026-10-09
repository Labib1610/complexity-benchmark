import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        if u != v:
            adj[u] |= (1 << v)
            adj[v] |= (1 << u)
            
    # Colors: 1, 2, 3 represented by bitmask 1 (1<<0), 2 (1<<1), 4 (1<<2)
    # Mask of available colors: 7 (111 in binary)
    
    colors = [0] * n
    domains = [7] * n
    
    # Precompute degree
    degrees = [bin(adj[i]).count('1') for i in range(n)]
    
    # Precompute popcount for 0..7
    popcount = [0, 1, 1, 2, 1, 2, 2, 3]
    
    assigned = 0
    all_assigned = (1 << n) - 1
    
    def backtrack(assigned_mask):
        if assigned_mask == all_assigned:
            return True
        
        # Select vertex with minimum domain size > 0 among unassigned
        # Tie breaker: maximum degree
        best_v = -1
        min_dom_size = 4
        max_deg = -1
        
        for i in range(n):
            if not (assigned_mask & (1 << i)):
                d_size = popcount[domains[i]]
                if d_size == 0:
                    return False
                if d_size < min_dom_size or (d_size == min_dom_size and degrees[i] > max_deg):
                    min_dom_size = d_size
                    max_deg = degrees[i]
                    best_v = i
                    if min_dom_size == 1:
                        break
        
        v = best_v
        v_dom = domains[v]
        
        # Try available colors
        for c in (1, 2, 3):
            c_bit = 1 << (c - 1)
            if v_dom & c_bit:
                colors[v] = c
                # Forward checking: update domains of unassigned neighbors
                # Save changes to restore
                changed = []
                valid = True
                
                nbrs = adj[v] & (~assigned_mask)
                while nbrs:
                    nbr = (nbrs & -nbrs).bit_length() - 1
                    nbrs &= nbrs - 1
                    
                    if domains[nbr] & c_bit:
                        domains[nbr] ^= c_bit
                        changed.append(nbr)
                        if domains[nbr] == 0:
                            valid = False
                            # Don't break immediately or break and restore
                            break
                
                if valid:
                    if backtrack(assigned_mask | (1 << v)):
                        return True
                
                # Restore domains
                for nbr in changed:
                    domains[nbr] |= c_bit
                    
                colors[v] = 0
                
        return False

    if backtrack(0):
        print("YES")
        print(*(colors[i] for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()