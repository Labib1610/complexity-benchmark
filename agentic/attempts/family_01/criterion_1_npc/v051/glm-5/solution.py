import sys
def main():
    input_data = sys.stdin.buffer.read().split()
    n = int(...); m = int(...)
    edges...
    adj = [0]*n (bitmask), adjlist
    # self-loop check: if u==v → print NO? Hmm. Let me think: self-interference means the instrument can't be with itself → impossible → NO. I'll handle: if u==v: possible_self = True → answer NO.
    # Actually also multi-edges: fine.
    
    # components
    comp = [-1]*n; label via BFS using adjlist.
    
    result = [0]*n
    for each component:
        verts = list of vertices
        # peel
        deg = {v: popcount(adj[v] within comp)} 
        # careful: adj[v] includes only actual neighbors (all in same component by definition) ✓
        removed_order = []
        deg_copy; queue of vertices with deg ≤ 2
        remaining = set of comp verts
        while queue: pop v (if already removed skip); remove from remaining; append to removed_order; for u in adj[v] ∩ remaining: deg[u] -= 1; if deg[u] ≤ 2: push u
        core = remaining
        if core empty: color all comp verts greedily in reverse removed_order (each ≤ 2 colored neighbors... wait, if core empty, ALL vertices get removed; reverse order coloring works: each vi has ≤ 2 neighbors in {v_{i+1}..vt} ∪ core(∅) ✓).
        else:
            K4 check on core → if found: print NO; return
            DSATUR on core (relabeled 0..k-1):
                if fails: print NO; return
            extend: color core per DSATUR; then reverse removed_order.
    print YES and colors (c_i + 1)