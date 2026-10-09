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
        
    # Check degree invariant
    for u in range(1, n + 1):
        if len(adj[u]) != 3:
            print("NO")
            return

    # Edge domain: bitmask of available colors (1: color 0, 2: color 1, 4: color 2)
    # Total colors: 3 (0, 1, 2 -> mapped to 1, 2, 3 at output)
    edge_domain = [7] * m
    assigned = [-1] * m
    
    # Precompute vertex incident edges
    v_edges = [adj[u] for u in range(1, n + 1)]
    
    # We will implement a backtracking solver with forward checking and unit propagation.
    # Trail-based undo for efficient backtracking.
    
    trail = []  # will store (edge, old_domain)
    
    def set_edge_domain(e, new_mask):
        if edge_domain[e] != new_mask:
            trail.append((e, edge_domain[e]))
            edge_domain[e] = new_mask
            if new_mask == 0:
                return False
        return True

    def propagate():
        # Repeatedly apply unit propagation
        changed = True
        while changed:
            changed = False
            
            # 1. Edges with domain size 1 that are not processed
            # 2. For each vertex and each color, check available edges
            for u in range(n):
                e0, e1, e2 = v_edges[u]
                d0, d1, d2 = edge_domain[e0], edge_domain[e1], edge_domain[e2]
                
                # Check for each color c in (0, 1, 2)
                for c in range(3):
                    bit = 1 << c
                    c0 = (d0 & bit) != 0
                    c1 = (d1 & bit) != 0
                    c2 = (d2 & bit) != 0
                    cnt = c0 + c1 + c2
                    if cnt == 0:
                        return False  # No edge can take color c
                    elif cnt == 1:
                        # Force that edge to have color c
                        if c0 and d0 != bit:
                            if not set_edge_domain(e0, bit): return False
                            changed = True
                        elif c1 and d1 != bit:
                            if not set_edge_domain(e1, bit): return False
                            changed = True
                        elif c2 and d2 != bit:
                            if not set_edge_domain(e2, bit): return False
                            changed = True

            # Also, if an edge has a single color, eliminate it from other incident edges
            for e in range(m):
                d = edge_domain[e]
                if d == 0:
                    return False
                if (d & (d - 1)) == 0:  # Power of 2 (single color)
                    u, v = edges[e]
                    mask = 7 ^ d
                    for e_other in adj[u]:
                        if e_other != e and (edge_domain[e_other] & d):
                            if not set_edge_domain(e_other, edge_domain[e_other] & mask):
                                return False
                            changed = True
                    for e_other in adj[v]:
                        if e_other != e and (edge_domain[e_other] & d):
                            if not set_edge_domain(e_other, edge_domain[e_other] & mask):
                                return False
                            changed = True
        return True

    # Break symmetry by fixing the colors of the first vertex's incident edges
    first_u_edges = v_edges[0]
    set_edge_domain(first_u_edges[0], 1)
    set_edge_domain(first_u_edges[1], 2)
    set_edge_domain(first_u_edges[2], 4)

    if not propagate():
        print("NO")
        return

    def backtrack():
        # Pick unassigned edge with smallest domain > 1
        best_e = -1
        best_sz = 4
        
        for e in range(m):
            d = edge_domain[e]
            sz = (d & 1) + ((d >> 1) & 1) + ((d >> 2) & 1)
            if sz > 1 and sz < best_sz:
                best_sz = sz
                best_e = e
                if sz == 2:
                    break
        
        if best_e == -1:
            # All edges assigned!
            return True

        d = edge_domain[best_e]
        choices = []
        for c in range(3):
            if d & (1 << c):
                choices.append(1 << c)
                
        for choice in choices:
            checkpoint = len(trail)
            if set_edge_domain(best_e, choice) and propagate():
                if backtrack():
                    return True
            # Undo
            while len(trail) > checkpoint:
                e, old_d = trail.pop()
                edge_domain[e] = old_d

        return False

    if backtrack():
        res = []
        for e in range(m):
            d = edge_domain[e]
            if d == 1:
                res.append(1)
            elif d == 2:
                res.append(2)
            elif d == 4:
                res.append(3)
        print("YES")
        print(*(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()