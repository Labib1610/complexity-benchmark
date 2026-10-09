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
            
    # Find connected components
    visited = 0
    components = []
    for i in range(n):
        if not (visited & (1 << i)):
            comp = []
            queue = [i]
            visited |= (1 << i)
            for u in queue:
                comp.append(u)
                nbrs = adj[u] & ~visited
                while nbrs:
                    lsb = nbrs & -nbrs
                    v = lsb.bit_length() - 1
                    visited |= (1 << v)
                    queue.append(v)
                    nbrs &= nbrs - 1
            components.append(comp)

    colors = [0] * n
    
    popcount = [0] * 8
    for i in range(8):
        popcount[i] = bin(i).count('1')

    def solve_component(comp):
        comp_mask = 0
        for u in comp:
            comp_mask |= (1 << u)
            
        dom = [7] * n
        assigned = 0
        
        # Symmetry breaking: color first vertex with color 0 (module 1)
        first_v = comp[0]
        
        def backtrack(assigned_mask):
            if assigned_mask == comp_mask:
                return True
            
            # Find unassigned vertex with minimum domain size (MRV)
            best_v = -1
            best_count = 4
            
            # Iterate through vertices in comp
            for v in comp:
                if not (assigned_mask & (1 << v)):
                    cnt = popcount[dom[v]]
                    if cnt < best_count:
                        best_count = cnt
                        best_v = v
                        if cnt <= 1:
                            break
            
            if best_count == 0:
                return False
            
            v = best_v
            v_dom = dom[v]
            
            for c in range(3):
                c_mask = 1 << c
                if v_dom & c_mask:
                    # Assign color c to vertex v
                    colors[v] = c + 1
                    # Forward checking: remove c from neighbors
                    affected = []
                    nbrs = adj[v] & comp_mask & ~assigned_mask
                    valid = True
                    while nbrs:
                        lsb = nbrs & -nbrs
                        u = lsb.bit_length() - 1
                        nbrs &= nbrs - 1
                        if dom[u] & c_mask:
                            dom[u] ^= c_mask
                            affected.append(u)
                            if dom[u] == 0:
                                valid = False
                                break
                    
                    if valid:
                        if backtrack(assigned_mask | (1 << v)):
                            return True
                    
                    # Undo
                    for u in affected:
                        dom[u] |= c_mask
            
            return False

        # Assign first vertex color 0
        colors[first_v] = 1
        nbrs = adj[first_v] & comp_mask
        while nbrs:
            lsb = nbrs & -nbrs
            u = lsb.bit_length() - 1
            nbrs &= nbrs - 1
            dom[u] &= ~(1 << 0)
            if dom[u] == 0:
                return False
                
        return backtrack(1 << first_v)

    for comp in components:
        if not solve_component(comp):
            print("NO")
            return
            
    print("YES")
    print(*(colors[i] for i in range(n)))

if __name__ == '__main__':
    solve()