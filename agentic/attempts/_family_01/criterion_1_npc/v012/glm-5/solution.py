import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Precompute connected components of the complement graph.
    comp = [-1] * n
    cid = 0
    for i in range(n):
        if comp[i] == -1:
            comp[i] = cid
            stack = [i]
            while stack:
                x = stack.pop()
                # Neighbors in complement: not x, not adjacent, and unvisited
                forbidden = adj[x] | (1 << x)
                # Iterate over all vertices not in forbidden
                # We can compute available = all_mask & ~forbidden
                # But we need unvisited ones
                avail = (~forbidden) & ((1 << n) - 1)
                # Remove already visited (comp != -1)
                # We'll iterate bits
                while avail:
                    b = avail & -avail
                    j = b.bit_length() - 1
                    if comp[j] == -1:
                        comp[j] = cid
                        stack.append(j)
                    avail ^= b
            cid += 1

    # For each complement component, collect its vertices and build complement adjacency.
    comp_vertices = [[] for _ in range(cid)]
    for i in range(n):
        comp_vertices[comp[i]].append(i)

    # Build complement adjacency lists for each component.
    comp_adj = []
    for verts in comp_vertices:
        k = len(verts)
        idx_map = {v: i for i, v in enumerate(verts)}
        cadj = [0] * k
        for i, v in enumerate(verts):
            forbidden = adj[v] | (1 << v)
            for j, w in enumerate(verts):
                if v != w and not (forbidden & (1 << w)):
                    cadj[i] |= 1 << j
        comp_adj.append(cadj)

    # For each component, find all maximal independent sets (which are cliques in original graph).
    # We need to assign each component a clique in original graph, and these cliques must be pairwise disjoint.
    # Since original graph cliques within a component are exactly the maximal independent sets of complement.

    # We'll compute maximal independent sets for each component using Bron-Kerbosch with pivoting.
    def bron_kerbosch(adj_list, k):
        if k == 0:
            return [0]
        results = []
        # R = 0, P = all, X = 0
        def bk(R, P, X):
            if P == 0 and X == 0:
                results.append(R)
                return
            # Pivot
            # Choose pivot from P | X with max degree
            # For simplicity, pick any
            pivot = (P | X).bit_length() - 1
            # Candidates: P \ N(pivot)
            # But we need neighbors of pivot
            npivot = adj_list[pivot]
            candidates = P & ~npivot
            while candidates:
                v = candidates & -candidates
                candidates ^= v
                nv = adj_list[v.bit_length() - 1]
                bk(R | v, P & ~nv, X & ~nv)
                P ^= v
                X |= v
        bk(0, (1 << k) - 1, 0)
        return results

    comp_cliques = []
    for idx, cadj in enumerate(comp_adj):
        k = len(comp_vertices[idx])
        cliques = bron_kerbosch(cadj, k)
        # Convert local bitmasks to global vertex bitmasks
        verts = comp_vertices[idx]
        global_cliques = []
        for c in cliques:
            g = 0
            temp = c
            while temp:
                b = temp & -temp
                local_idx = b.bit_length() - 1
                g |= 1 << verts[local_idx]
                temp ^= b
            global_cliques.append(g)
        comp_cliques.append(global_cliques)

    # Now we need to select one clique from each component such that they are pairwise disjoint.
    # This is exact cover / set packing. We can do DP over components with bitmask of used vertices.
    # n <= 40, but number of components could be up to 40. However, if many components, each is small.
    # We can do DP with dictionary of used mask -> assignment.
    # But 2^40 is too large. However, we can use the fact that components are independent and we only
    # need to track which vertices are used. But if there are many components, each has few vertices,
    # and the total combinations might be manageable if we prune.

    # Alternative: Since we need to partition vertices into 3 cliques, and each component must be
    # entirely within one clique, we can think of it as 3-coloring the components where each component
    # is assigned to a color, but with the constraint that the selected cliques are disjoint.
    # Actually, the selected cliques must be disjoint and cover all vertices. Since each component
    # is covered by exactly one clique, and cliques from different components must be disjoint,
    # this is equivalent to: for each component, choose a maximal independent set (clique in original),
    # and these chosen sets must be pairwise disjoint.

    # We can do backtracking with memoization on the remaining components and used mask.
    # But used mask can be large. However, we can observe that if we process components in order
    # and maintain used mask, we can prune if a component has no valid clique disjoint from used.
    # Given n <= 40, and each component's cliques are limited, this might be fast enough.

    # Let's try backtracking with bitmask.
    # To optimize, we can sort components by number of cliques (ascending) to fail early.

    comp_order = sorted(range(cid), key=lambda i: len(comp_cliques[i]))
    sorted_cliques = [comp_cliques[i] for i in comp_order]

    # Precompute for each component the list of cliques as integers.
    # We'll do DFS.
    assignment = [0] * cid  # which clique index chosen for each component in sorted order
    used = 0

    # Memoization: (comp_index, used) -> bool
    # But used can be up to 2^40, too large for dict. We'll rely on pruning.
    # However, we can use the fact that if we process in order, the used mask only grows.
    # We can use a set of visited (index, used) to avoid recomputation.
    memo = set()

    def dfs(idx, used):
        if idx == len(sorted_cliques):
            return True
        key = (idx, used)
        if key in memo:
            return False
        for c in sorted_cliques[idx]:
            if (used & c) == 0:
                if dfs(idx + 1, used | c):
                    assignment[idx] = c
                    return True
        memo.add(key)
        return False

    if not dfs(0, 0):
        print("NO")
        return

    # Reconstruct coloring
    color = [0] * n
    # We have 3 cliques: the chosen ones for each component. But we need to assign colors 1,2,3 to the three cliques.
    # Actually, the three cliques are the three groups. But we have many components, each assigned to one of three cliques.
    # Wait, the assignment above selects one clique per component, and they are disjoint. The union of all selected cliques
    # is all vertices. But we need to partition into exactly 3 cliques. The selected cliques from all components are many,
    # but they must be groupable into 3 sets such that each set is a clique. However, since components are disconnected in
    # complement graph, there are no edges between components in complement, meaning in original graph, all edges between
    # components exist. So any two vertices from different components are adjacent in original graph. Thus, if we take
    # the union of selected cliques from multiple components, it's still a clique in original graph (since all cross edges exist).
    # So we can merge the selected cliques into 3 groups arbitrarily? No, we need exactly 3 cliques that partition all vertices.
    # But we have many selected cliques (one per component). We can merge them into 3 groups because any union of cliques from
    # different components is a clique. So we can just assign each component's selected clique to one of 3 colors, but we must
    # ensure that the 3 resulting groups are cliques. Since any two vertices from different components are adjacent, any
    # grouping works. So we can just assign the components to 3 colors arbitrarily? No, we need to ensure that within each
    # color, the vertices form a clique. Since each component's selected clique is a clique, and cross-component edges are all
    # present, any union of selected cliques is a clique. So we can partition the components into 3 groups arbitrarily.
    # But we need to output a coloring where each color class is a clique. So we can just assign each component to one of 3 colors.
    # However, we must use all 3 colors? The problem says "exactly three isolated power buses", but instruments can be assigned
    # to any of the three. It doesn't require all three to be used. So we can assign all components to color 1, but then color 1
    # must be a clique. Since all vertices are in color 1, the whole graph must be a clique, which is not true in general.
    # Wait, no: the selected cliques are disjoint and cover all vertices. If we assign all to color 1, then color 1 is the whole
    # vertex set, which is a clique only if the graph is complete. So we cannot arbitrarily assign components to colors.
    # We need to partition the selected cliques into 3 groups such that each group is a clique. Since cross-component edges are
    # all present, any group that is a union of selected cliques is a clique. So we can partition the selected cliques into 3
    # groups arbitrarily. But we need to output a coloring. So we can assign each component's selected clique to one of 3 colors,
    # and since any union is a clique, it's valid. But we must ensure that the three color classes are cliques. Since each color
    # class is a union of some selected cliques, and cross edges exist, it's a clique. So we can assign components to colors
    # arbitrarily. But we need to output a specific coloring. We can just assign the first component to color 1, second to 2, etc.,
    # but we might run out of colors if we have more than 3 components. We can cycle through colors 1,2,3.
    # However, we must ensure that each color class is a clique. Since any union of selected cliques is a clique, we can assign
    # components to colors in any way. So we can just assign color = (idx % 3) + 1 for each component in sorted order.
    # But wait: the selected cliques are disjoint and cover all vertices. If we assign each component to a color, the color class
    # is the union of selected cliques of components with that color. Since cross edges exist, it's a clique. So yes.
    # But we need to output the color for each vertex. So for each component, we assign a color, and all vertices in its selected
    # clique get that color.
    # We can just assign colors 1,2,3 cyclically to components in sorted order.
    # But we must ensure that we don't have more than 3 components? No, we can have more than 3 components, and we can assign
    # multiple components to the same color. The color class will be a clique because cross edges exist.
    # So this is valid.

    # Reconstruct the selected clique for each component in original order.
    selected = [0] * cid
    for idx in range(len(sorted_cliques)):
        comp_id = comp_order[idx]
        selected[comp_id] = assignment[idx]

    # Assign colors: we can just assign each component a color. Since any union is a clique, we can use 3 colors.
    # To be safe, we can assign colors such that we use at most 3 colors. We can just assign color = (comp_id % 3) + 1.
    # But we need to ensure that the color classes are cliques. Since cross edges exist, any grouping works.
    # So we can assign color = (comp_id % 3) + 1.
    # However, we must ensure that the selected clique for each component is assigned a single color. So all vertices in a
    # component's selected clique get the same color.
    # Let's do that.
    for comp_id in range(cid):
        c = selected[comp_id]
        color_val = (comp_id % 3) + 1
        temp = c
        while temp:
            b = temp & -temp
            v = b.bit_length() - 1
            color[v] = color_val
            temp ^= b

    print("YES")
    print(" ".join(str(color[i]) for i in range(n)))

solve()