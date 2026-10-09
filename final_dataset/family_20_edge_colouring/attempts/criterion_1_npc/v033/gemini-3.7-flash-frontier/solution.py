import sys

# Increase recursion depth just in case
sys.setrecursionlimit(20000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
        
    # edge_color: -1 if uncolored, 0, 1, 2 for colors 1, 2, 3
    edge_color = [-1] * m
    # vertex_used_colors[v] = bitmask of used colors (bits 0, 1, 2)
    vertex_mask = [0] * (n + 1)
    
    # We will use backtracking with MRV and forward checking
    # Precompute edge neighbors (edges sharing a vertex)
    edge_adj = [[] for _ in range(m)]
    for u in range(1, n + 1):
        inc = adj[u]
        for e1 in inc:
            for e2 in inc:
                if e1 != e2:
                    edge_adj[e1].append(e2)
    for i in range(m):
        edge_adj[i] = list(set(edge_adj[i]))

    # For each edge, maintain available colors as a bitmask (111_2 = 7 initially)
    avail = [7] * m
    
    # Count of unassigned edges
    unassigned = m
    
    # Unit propagation / forward checking stack for backtracking
    trail = []
    
    def assign(e, c):
        nonlocal unassigned
        edge_color[e] = c
        unassigned -= 1
        mask_c = 1 << c
        
        # Propagate to adjacent edges
        changes = []
        for nxt in edge_adj[e]:
            if edge_color[nxt] == -1 and (avail[nxt] & mask_c):
                avail[nxt] &= ~mask_c
                changes.append(nxt)
                if avail[nxt] == 0:
                    # Conflict!
                    # Rollback changes made in this assign
                    for ch in changes:
                        avail[ch] |= mask_c
                    edge_color[e] = -1
                    unassigned += 1
                    return False, None
        return True, changes

    def unassign(e, c, changes):
        nonlocal unassigned
        mask_c = 1 << c
        for ch in changes:
            avail[ch] |= mask_c
        edge_color[e] = -1
        unassigned += 1

    # Deterministic unit propagation loop
    def unit_propagate():
        forced = []
        # Find any unassigned edge with exactly 1 available color
        while True:
            found = False
            for e in range(m):
                if edge_color[e] == -1:
                    av = avail[e]
                    if av == 0:
                        return False, forced
                    if (av & (av - 1)) == 0: # single bit set
                        c = (av & -av).bit_length() - 1
                        ok, changes = assign(e, c)
                        if not ok:
                            return False, forced
                        forced.append((e, c, changes))
                        found = True
                        break
            if not found:
                break
        return True, forced

    def backtrack():
        if unassigned == 0:
            return True
        
        # Select unassigned edge with minimum available colors
        best_e = -1
        min_c = 4
        for e in range(m):
            if edge_color[e] == -1:
                cnt = bin(avail[e]).count('1')
                if cnt < min_c:
                    min_c = cnt
                    best_e = e
                    if min_c == 1:
                        break
        
        if best_e == -1 or min_c == 0:
            return False
            
        av = avail[best_e]
        for c in range(3):
            if av & (1 << c):
                ok, changes = assign(best_e, c)
                if not ok:
                    continue
                
                # Unit propagate
                prop_ok, forced = unit_propagate()
                if prop_ok:
                    if backtrack():
                        return True
                
                # Undo forced
                for fe, fc, fch in reversed(forced):
                    unassign(fe, fc, fch)
                
                unassign(best_e, c, changes)
                
        return False

    if backtrack():
        print("YES")
        print(*(c + 1 for c in edge_color))
    else:
        print("NO")

if __name__ == '__main__':
    solve()