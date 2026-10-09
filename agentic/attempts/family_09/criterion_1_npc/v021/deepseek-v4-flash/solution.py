import sys
sys.setrecursionlimit(10000)

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [0]*n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Precompute degree for ordering
    deg = [bin(adj[i]).count('1') for i in range(n)]

    # We'll use a recursive search
    # candidates: bitmask of vertices that can still be added (not adjacent to chosen)
    # chosen_mask: bitmask of chosen vertices
    # chosen_size: number of chosen

    # Upper bound: greedy coloring
    def upper_bound(cand):
        # color vertices in cand
        # We'll iterate over bits
        color = 0
        remaining = cand
        while remaining:
            # pick a vertex (maybe lowest bit)
            # assign a color, remove it and all vertices that conflict with it? Actually for coloring bound,
            # we need to color the graph induced by cand. Greedy: pick vertex, assign smallest color not used by neighbors already colored.
            # But we can do a simpler bound: size of maximum independent set <= number of vertices in a greedy coloring.
            # We'll implement greedy coloring:
            # We'll maintain color assignment as list of ints for vertices in cand? But cand changes.
            # Simpler: use a known bound: repeatedly pick a vertex, remove it and its neighbors, count picks.
            # That gives a maximal independent set, not an upper bound. Actually that gives a lower bound.
            # For upper bound, we can use: max independent set <= number of vertices in a greedy coloring.
            # Let's implement greedy coloring:
            # We'll iterate over vertices in cand in some order (e.g., by degree).
            # For each vertex, assign the smallest color not used by its neighbors already colored.
            # The number of colors used is an upper bound.
            # We'll do this with bitmasks: for each color, we have a bitmask of vertices assigned that color.
            # But we need to know which vertices are already colored.
            # Let's do:
            # colored = 0
            # colors_used = 0
            # while cand & ~colored:
            #     pick a vertex v from cand & ~colored (maybe lowest bit)
            #     # find smallest color not used by neighbors of v that are already colored
            #     # We'll maintain for each color a bitmask of vertices with that color
            #     # But we can just try colors 0..colors_used-1
            #     # For each color c, check if (color_masks[c] & adj[v]) == 0
            #     # If yes, assign v to that color; else new color.
            #     # This is O(colors * n) per vertex, but n=46, fine.
            #     # However, we need to do this for many calls, so we need it fast.
            #     # We can precompute for each vertex its neighbors, but we already have adj.
            #     # Let's implement with a list of color masks.
            #     color_masks = []
            #     for c in range(colors_used):
            #         if (color_masks[c] & adj[v]) == 0:
            #             color_masks[c] |= (1<<v)
            #             break
            #     else:
            #         color_masks.append(1<<v)
            #         colors_used += 1
            #     colored |= (1<<v)
            # return colors_used
            pass
        # But this is O(n^2) per call, might be okay if calls are limited.
        # We'll implement it.

    # Actually, we can use a simpler bound: the size of a maximum independent set in a graph is at most the number of vertices in a greedy coloring. We'll implement that.

    # But we need to be careful: the bound must be an upper bound on the maximum independent set size in the induced subgraph on candidates.
    # Greedy coloring gives an upper bound because each color class is an independent set, and the number of colors is at least the chromatic number, which is >= the size of the maximum independent set? Actually, the chromatic number is at least the size of the maximum clique, not independent set. Wait, for independent set, the bound is: maximum independent set size <= number of vertices in a greedy coloring? No, that's not correct. The size of a maximum independent set is at most the number of colors in any proper coloring? Actually, in a proper coloring, each color class is an independent set, so the maximum independent set can be larger than the number of colors? No, each color class is an independent set, but the maximum independent set could be larger than the number of colors? Example: a star graph with center connected to 3 leaves. Proper coloring: center color 1, leaves color 2 (all leaves can share color 2 because they are not adjacent). So 2 colors. Maximum independent set: all 3 leaves, size 3 > 2. So number of colors is NOT an upper bound on independent set size. So that bound is wrong.

    # The correct bound: maximum independent set size <= number of vertices - size of maximum matching? Not simple.

    # A common bound for maximum independent set in branch and bound is: use a greedy coloring of the *complement* graph? Actually, maximum independent set in G is maximum clique in complement. For maximum clique, a common bound is the number of colors in a greedy coloring of the graph (since each color class is an independent set, and a clique can have at most one vertex per color). So for maximum independent set, we can apply that to the complement graph: color the complement graph, the number of colors is an upper bound on the size of a maximum independent set in the original graph. Because in the complement, each color class is a clique in the complement? Wait, in complement, a color class is an independent set in complement, which is a clique in original. So a clique in original can have at most one vertex per color in a proper coloring of complement. So the number of colors in a proper coloring of complement is an upper bound on the maximum clique in original, which is the maximum independent set in original. Yes! So we need to color the complement graph.

    # So for candidates, we need to color the complement of the induced subgraph on candidates. That is, two vertices are adjacent in complement if they are NOT adjacent in original. So we need to build complement adjacency.

    # Let's precompute comp_adj[i] = bitmask of vertices not adjacent to i (excluding i).

    # Then upper_bound(cand) = number of colors in greedy coloring of complement graph induced by cand.

    # We'll implement that.

    comp_adj = [0]*n
    for i in range(n):
        comp_adj[i] = ((1<<n)-1) ^ (1<<i) ^ adj[i]

    def upper_bound(cand):
        # Greedy coloring of complement graph on vertices in cand
        # We'll iterate over vertices in cand, assign smallest color not used by neighbors in complement already colored.
        # We'll maintain color_masks list.
        color_masks = []
        colored = 0
        remaining = cand
        while remaining:
            # pick a vertex (lowest bit)
            v = (remaining & -remaining).bit_length() - 1
            remaining &= remaining - 1
            # find smallest color
            assigned = False
            for c, mask in enumerate(color_masks):
                if (mask & comp_adj[v]) == 0:
                    color_masks[c] |= (1<<v)
                    assigned = True
                    break
            if not assigned:
                color_masks.append(1<<v)
        return len(color_masks)

    # Now recursive search
    # We'll order vertices by degree (maybe descending) to improve pruning.
    order = sorted(range(n), key=lambda i: deg[i], reverse=True)
    # But we'll use bitmask, so we can just pick lowest bit in candidates.

    # We'll also precompute for each vertex its neighbors in the order? Not needed.

    # We'll use a global found solution
    solution = None

    def dfs(cand, chosen_size, chosen_mask):
        nonlocal solution
        if solution is not None:
            return
        if chosen_size == k:
            solution = chosen_mask
            return
        if cand == 0:
            return
        # Bound
        if chosen_size + upper_bound(cand) < k:
            return
        # Choose a vertex with smallest degree in cand? Or just lowest bit.
        # We'll pick the vertex with smallest degree in the induced subgraph? That might help.
        # But computing degrees in cand each time is O(n). n=46, fine.
        # Let's pick the vertex with smallest degree in cand (in original graph) to branch on.
        # Actually, for independent set, picking a vertex with high degree is often better for pruning when including it (removes many candidates).
        # We'll pick the vertex with highest degree in cand.
        best_v = -1
        best_deg = -1
        temp = cand
        while temp:
            v = (temp & -temp).bit_length() - 1
            d = (adj[v] & cand).bit_count()
            if d > best_deg:
                best_deg = d
                best_v = v
            temp &= temp - 1
        v = best_v
        # Option 1: include v
        new_cand = cand & ~adj[v] & ~(1<<v)
        dfs(new_cand, chosen_size+1, chosen_mask | (1<<v))
        # Option 2: exclude v
        dfs(cand & ~(1<<v), chosen_size, chosen_mask)

    # Start with all vertices as candidates
    dfs((1<<n)-1, 0, 0)

    if solution is None:
        print("NO")
    else:
        print("YES")
        pins = [str(i+1) for i in range(n) if (solution>>i)&1]
        print(" ".join(pins))

if __name__ == "__main__":
    solve()