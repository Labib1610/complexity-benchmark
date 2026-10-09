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
            
    # Self-loops mean not 3-colorable
    # But usually simple graph. If self-loop, immediately NO.
    
    # We will use backtracking with MRV (DSATUR) heuristic
    color = [-1] * n
    avail = [7] * n  # mask of available colors: 1 (color 1), 2 (color 2), 4 (color 3)
    
    # Popcount lookup for masks 0..7
    popcount = [0, 1, 1, 2, 1, 2, 2, 3]
    
    deg = [bin(adj[i]).count('1') for i in range(n)]
    
    def backtrack(uncolored_count):
        if uncolored_count == 0:
            return True
        
        # Find vertex with minimum available colors
        best_u = -1
        min_c = 4
        max_d = -1
        
        for u in range(n):
            if color[u] == -1:
                c = popcount[avail[u]]
                if c < min_c:
                    min_c = c
                    max_d = deg[u]
                    best_u = u
                elif c == min_c and deg[u] > max_d:
                    max_d = deg[u]
                    best_u = u
        
        if min_c == 0:
            return False
        
        u = best_u
        mask = avail[u]
        
        # Try colors
        for c_idx in range(3):
            c_bit = 1 << c_idx
            if mask & c_bit:
                color[u] = c_idx + 1
                
                # Update neighbors
                changed = []
                possible = True
                u_adj = adj[u]
                
                # Iterate over neighbors of u
                v = 0
                temp = u_adj
                while temp > 0:
                    lsb = temp & -temp
                    v = (lsb).bit_length() - 1
                    if color[v] == -1 and (avail[v] & c_bit):
                        avail[v] ^= c_bit
                        changed.append(v)
                        if avail[v] == 0:
                            possible = False
                    temp ^= lsb
                
                if possible and backtrack(uncolored_count - 1):
                    return True
                
                # Undo
                for v in changed:
                    avail[v] |= c_bit
                color[u] = -1
                
        return False

    if backtrack(n):
        print("YES")
        print(*(color[i] for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()