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
            
    # Check for self-loops (impossible if cycle assignment needs no dispute)
    # The problem statement says u and v are a pair, but if u == v, impossible.
    # Handled by simple graph assumption.
    
    # Deg-based tie breaker
    deg = [bin(adj[i]).count('1') for i in range(n)]
    
    pop = [0, 1, 1, 2, 1, 2, 2, 3]
    color_assignment = [0] * n
    avail = [7] * n
    
    def backtrack(uncolored_mask):
        if uncolored_mask == 0:
            return True
        
        # Pick vertex with MRV, tie-break by max degree
        best_v = -1
        best_pop = 4
        best_deg = -1
        
        temp = uncolored_mask
        while temp > 0:
            lsb = temp & -temp
            v = lsb.bit_length() - 1
            temp ^= lsb
            
            p = pop[avail[v]]
            if p < best_pop:
                best_pop = p
                best_v = v
                best_deg = deg[v]
                if p == 1:
                    break
            elif p == best_pop:
                if deg[v] > best_deg:
                    best_v = v
                    best_deg = deg[v]
        
        if best_pop == 0:
            return False
        
        v = best_v
        v_avail = avail[v]
        new_uncolored = uncolored_mask ^ (1 << v)
        
        for c in range(3):
            if (v_avail >> c) & 1:
                color_assignment[v] = c + 1
                c_mask = ~(1 << c)
                
                # Update neighbors
                changed_neighbors = []
                nbrs = adj[v] & new_uncolored
                while nbrs > 0:
                    lsb = nbrs & -nbrs
                    u = lsb.bit_length() - 1
                    nbrs ^= lsb
                    if (avail[u] >> c) & 1:
                        avail[u] &= c_mask
                        changed_neighbors.append(u)
                
                if backtrack(new_uncolored):
                    return True
                
                # Undo
                for u in changed_neighbors:
                    avail[u] |= (1 << c)
                    
        return False

    if backtrack((1 << n) - 1):
        print("YES")
        print(*(color_assignment[i] for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()