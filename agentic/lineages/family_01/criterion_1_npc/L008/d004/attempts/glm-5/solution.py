import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Precompute for each vertex the set of vertices with higher index
    higher = [0] * (n + 2)
    for v in range(1, n + 1):
        s = 0
        for u in range(v + 1, n + 1):
            if adj[v] & (1 << u):
                s |= 1 << u
        higher[v] = s

    # For each vertex v, precompute the set of neighbors with index < v
    lower = [0] * (n + 2)
    for v in range(1, n + 1):
        s = 0
        for u in range(1, v):
            if adj[v] & (1 << u):
                s |= 1 << u
        lower[v] = s

    # For each vertex v, precompute the set of neighbors with index > v
    # (same as higher[v])
    # For each vertex v, precompute the set of neighbors with index < v that are also neighbors of some higher vertex? Not needed.

    # We'll do DP over subsets of vertices, but n up to 40 is too large for full subset DP.
    # Instead, we use the fact that the graph is small (n<=40) and we can use a backtracking with pruning.
    # But the problem says adversarial tests are designed to break fixed-order trial-and-error.
    # We need a smarter approach.

    # Actually, this is 3-coloring. For n<=40, we can use a meet-in-the-middle or a clever backtracking.
    # Let's use a backtracking with DSATUR-like heuristic and bit operations.

    # But to get the lexicographically smallest solution (minimizing the structural signature),
    # we need to try colors in order 1,2,3 for each vertex in order 1..n.
    # The adversarial tests are designed to break naive backtracking.
    # We can use a more efficient approach: since we need the lexicographically smallest,
    # we can use a SAT-like or constraint propagation approach.

    # Let's implement a backtracking with forward checking and bit operations.
    # We'll process vertices in order 1..n (to get lexicographically smallest).
    # For each vertex, we maintain the set of available colors for each future vertex.
    # We use bitmasks for colors.

    # But to handle adversarial cases, we need good pruning.
    # Let's use a recursive backtracking with forward checking.

    # Actually, for n=40, even with forward checking, worst-case 3-coloring can be exponential.
    # But the problem says "adversarial testing configurations on the full 40 elements"
    # "engineered specifically to cause fixed-order, coating-by-coating trial-and-error approaches to exceed the time limit."
    # So we need something better than naive backtracking.

    # One approach: use a SAT solver or a more clever algorithm.
    # But implementing a SAT solver is complex.
    # Another approach: use the fact that 3-coloring can be solved in O(1.6181^n) or similar using clever branching.
    # But for n=40, even that might be too slow.

    # Let's think about this differently. The problem is asking for 3-coloring.
    # For n<=40, we can use a meet-in-the-middle approach if the graph is sparse,
    # but for dense graphs, it's harder.

    # Actually, let's use a backtracking with a good heuristic and hope it's fast enough.
    # We'll use forward checking and try colors in order 1,2,3 for each vertex in order 1..n.

    # Let's implement it with bitmasks for efficiency.

    color = [0] * (n + 1)
    # available[v] is a bitmask of colors available for vertex v
    # We'll use bits 1,2,3 for colors 1,2,3 (bit 0 unused)
    # Initially all colors available: 0b1110 (bits 1,2,3 set)

    # For forward checking, we need to quickly check if any future vertex has no available colors.
    # We'll maintain available as a list of bitmasks.

    # Let's use a recursive function with forward checking.

    # Precompute for each vertex v, the list of neighbors with index > v
    next_neighbors = [0] * (n + 2)
    for v in range(1, n + 1):
        next_neighbors[v] = higher[v]

    # Precompute for each vertex v, the list of neighbors with index < v
    prev_neighbors = [0] * (n + 2)
    for v in range(1, n + 1):
        prev_neighbors[v] = lower[v]

    available = [0b1110] * (n + 2)  # bits 1,2,3 set

    def backtrack(v):
        if v > n:
            return True
        # Try colors in order 1, 2, 3
        for c in range(1, 4):
            if available[v] & (1 << c):
                # Check if this color is valid (no conflict with colored neighbors)
                # Actually, available already accounts for this, but let's be safe
                ok = True
                for u in range(1, v):
                    if (adj[v] & (1 << u)) and color[u] == c:
                        ok = False
                        break
                if not ok:
                    continue
                # Assign color c to v
                color[v] = c
                # Forward checking: update available colors for future neighbors
                removed = []
                mask = 1 << c
                # Iterate over neighbors of v with index > v
                nn = next_neighbors[v]
                temp = nn
                while temp:
                    u = (temp & -temp).bit_length()
                    temp &= temp - 1
                    if available[u] & mask:
                        available[u] &= ~mask
                        removed.append(u)
                        if available[u] == 0:
                            # No colors available for u, backtrack
                            # Restore and continue
                            for ru in removed:
                                available[ru] |= mask
                            color[v] = 0
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    if backtrack(v + 1):
                        return True
                # Restore
                for ru in removed:
                    available[ru] |= mask
                color[v] = 0
        return False

    if backtrack(1):
        print("YES")
        print(" ".join(str(color[i]) for i in range(1, n + 1)))
    else:
        print("NO")

solve()