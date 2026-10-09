import sys

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
            
    # Pre-check for self loops
    for i in range(n):
        if (adj[i] >> i) & 1:
            print("NO")
            return

    color = [-1] * n
    domain = [7] * n  # bitmask: 1=color 1, 2=color 2, 4=color 3
    
    # Precompute bit count for numbers 0..7
    popcount = [0, 1, 1, 2, 1, 2, 2, 3]

    def backtrack(unassigned_count):
        if unassigned_count == 0:
            return True
        
        # MRV: find vertex with minimum domain size > 0
        best_v = -1
        min_dom = 4
        
        for i in range(n):
            if color[i] == -1:
                sz = popcount[domain[i]]
                if sz == 0:
                    return False
                if sz < min_dom:
                    min_dom = sz
                    best_v = i
                    if sz == 1:
                        break
        
        v = best_v
        v_dom = domain[v]
        
        # Try each color in domain[v]
        for c in (0, 1, 2):
            if (v_dom >> c) & 1:
                color[v] = c + 1
                bit_to_remove = ~(1 << c)
                
                # Forward checking
                valid = True
                changed = []
                mask = adj[v]
                while mask > 0:
                    u = (mask & -mask).bit_length() - 1
                    mask &= mask - 1
                    if color[u] == -1 and ((domain[u] >> c) & 1):
                        changed.append(u)
                        domain[u] &= bit_to_remove
                        if domain[u] == 0:
                            valid = False
                            # Do not break immediately because we need to revert properly,
                            # but we can stop forward checking the rest.
                            break
                
                if valid:
                    if backtrack(unassigned_count - 1):
                        return True
                
                # Revert
                for u in changed:
                    domain[u] |= (1 << c)
                color[v] = -1
                
        return False

    if backtrack(n):
        print("YES")
        print(*(color[i] for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()