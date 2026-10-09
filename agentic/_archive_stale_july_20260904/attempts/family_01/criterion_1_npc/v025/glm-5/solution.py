import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Precompute connected components
    visited = [False] * (n + 1)
    components = []
    for i in range(1, n + 1):
        if not visited[i]:
            comp = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                mask = adj[u]
                while mask:
                    lsb = mask & -mask
                    v = lsb.bit_length() - 1
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
                    mask ^= lsb
            components.append(comp)

    # For each component, find all valid 3-colorings
    comp_colorings = []
    for comp in components:
        k = len(comp)
        colorings = []
        for state in range(3 ** k):
            valid = True
            for idx in range(k):
                u = comp[idx]
                cu = (state // (3 ** idx)) % 3
                mask = adj[u]
                while mask:
                    lsb = mask & -mask
                    v = lsb.bit_length() - 1
                    # Find v's index in comp
                    # Since comp is small (<=40), linear search is fine
                    # But we can precompute index map
                    # For efficiency, precompute outside
                    pass
                    mask ^= lsb
            # Better approach: precompute index map
            break
        # Let's redo with index map
        idx_map = {u: i for i, u in enumerate(comp)}
        colorings = []
        for state in range(3 ** k):
            valid = True
            for idx in range(k):
                u = comp[idx]
                cu = (state // (3 ** idx)) % 3
                mask = adj[u]
                while mask:
                    lsb = mask & -mask
                    v = lsb.bit_length() - 1
                    if v in idx_map:
                        vi = idx_map[v]
                        if vi > idx:  # check each edge once
                            cv = (state / (3 ** vi)) % 3
                            if cu == cv:
                                valid = False
                                break
                    mask ^= lsb
                if not valid:
                    break
            if valid:
                coloring = [0] * n
                for idx in range(k):
                    coloring[comp[idx] - 1] = (state // (3 ** idx)) % 3 + 1
                colorings.append(coloring)
        if not colorings:
            print("NO")
            return
        comp_colorings.append(colorings)

    # Merge components to find lexicographically smallest
    # Start with first component's colorings, then merge
    # We need to find the combination that gives lex smallest overall
    # Since components are independent, we can process them in order of their smallest vertex
    # But for lex smallest, we need to consider all combinations
    
    # Sort components by their minimum vertex for processing
    comp_colorings.sort(key=lambda x: min(np.nonzero(x[0])[0]) if x else 0)
    
    # Actually, let's just merge all and find lex smallest
    # But number of combinations could be large. Need smarter approach.
    
    # Since we want lex smallest, we can do a greedy approach with backtracking
    # But let's think: for each position from 1 to n, try to assign smallest color
    # that is consistent with some valid coloring of all components
    
    # Alternative: since components are independent, for each component we can find
    # the lex smallest coloring when considered alone, but that might not give
    # global lex smallest because of interaction between components
    
    # Actually, components are independent, so the global lex smallest is obtained
    # by making each component's coloring lex smallest in the order of their vertices
    
    # Wait, no. Consider two components: one with vertices {1, 3}, another with {2}
    # If we make {1,3} lex smallest, we get 1,1. Then {2} gets 1. Result: 1,1,1
    # But if {1,3} gets 1,2, then {2} gets 1. Result: 1,1,2 which is lex smaller? No, 1,1,1 < 1,1,2
    # So making each component lex smallest independently gives global lex smallest
    
    # But wait, the order matters. If component A has vertex 1 and component B has vertex 2,
    # and A's lex smallest is [1,2] (for vertices 1,3) and B's is [1] (for vertex 2),
    # then global is 1,1,2. But if A uses [1,1], then global is 1,1,1 which is smaller.
    # So we need A to be lex smallest, which is [1,1] if valid.
    
    # So the approach is: process vertices in order 1 to n. For each vertex, try colors 1,2,3.
    # For each color, check if there exists a valid completion. This is standard backtracking
    # with forward checking.
    
    # Given n <= 40 and 3 colors, backtracking with forward checking should work
    # especially since the graph is guaranteed to be 3-colorable or we detect NO early
    
    # Let's implement backtracking
    assignment = [0] * (n + 1)
    possible = [7] * (n + 1)  # bitmask of possible colors, bits 0,1,2 for colors 1,2,3
    
    def backtrack(pos):
        if pos > n:
            return True
        # Find the vertex to assign (we go in order 1 to n for lex smallest)
        u = pos
        if assignment[u] != 0:
            return backtrack(pos + 1)
        for c in range(3):
            if possible[u] & (1 << c):
                # Try color c+1
                # Save state
                saved_possible = {}
                assignment[u] = c + 1
                # Update neighbors
                mask = adj[u]
                ok = True
                while mask:
                    lsb = mask & -mask
                    v = lsb.bit_length() - 1
                    if assignment[v] == 0:
                        if possible[v] & (1 << c):
                            saved_possible[v] = possible[v]
                            possible[v] &= ~(1 << c)
                            if possible[v] == 0:
                                ok = False
                                break
                    mask ^= lsb
                if ok:
                    if backtrack(pos + 1):
                        return True
                # Restore
                assignment[u] = 0
                for v, p in saved_possible.items():
                    possible[v] = p
        return False
    
    # Initialize possible based on nothing (all colors possible)
    if backtrack(1):
        print("YES")
        print(' '.join(str(assignment[i]) for i in range(1, n + 1)))
    else:
        print("NO")

solve()