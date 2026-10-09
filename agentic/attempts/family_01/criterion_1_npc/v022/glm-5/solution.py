import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        if u != v:
            adj[u].add(v)
            adj[v].add(u)
    
    # adjacency as bitmasks
    adj_mask = [0] * n
    for u in range(n):
        for v in adj[u]:
            adj_mask[u] |= (1 << v)
    
    color = [-1] * n  # 0, 1, 2
    
    # DSATUR backtracking
    # For each uncolored vertex, track set of colors used by neighbors (as bitmask).
    # sat[v] = bitmask of colors used among colored neighbors.
    sat = [0] * n
    deg = [len(adj[u]) for u in range(n)]
    
    # Symmetry breaking: max color used so far; a new color c can only be used if c <= max_used + 1.
    # Also fix vertex 0's color to 0? That's valid by symmetry.
    
    import sys
    sys.setrecursionlimit(10000)
    
    def solve():
        # find uncolored vertex with max saturation, tie-break by degree
        best = -1
        best_sat = -1
        best_deg = -1
        max_used = -1
        for v in range(n):
            if color[v] == -1:
                s = bin(sat[v]).count('1')
                if s > best_sat or (s == best_sat and deg[v] > best_deg):
                    best = v
                    best_sat = s
                    best_deg = deg[v]
        if best == -1:
            return True
        v = best
        # determine max color used so far
        # track globally instead
        for c in range(3):
            if not (sat[v] >> c) & 1:
                if c > max_color_used + 1:
                    break  # symmetry breaking: can't introduce color beyond max+1
                color[v] = c
                # update neighbors
                changed = []
                for u in adj[v]:
                    if color[u] == -1:
                        if not (sat[u] >> c) & 1:
                            sat[u] |= (1 << c)
                            changed.append(u)
                        # else already set
                # hmm, need to track which neighbors got the bit added for undo
                prev_max = max_color_used[0]
                if c > prev_max:
                    max_color_used[0] = c
                if solve():
                    return True
                max_color_used[0] = prev_max
                for u in changed:
                    sat[u] &= ~(1 << c)
                color[v] = -1
        return False
    ...