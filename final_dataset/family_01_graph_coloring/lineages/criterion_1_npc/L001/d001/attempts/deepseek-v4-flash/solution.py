import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n

    # Try to 3-color the graph with backtracking, using symmetry breaking.
    # n <= 40, but the graph may be dense. We use DSATUR-style heuristic ordering.
 
    # Precompute conflict sets as bitmasks for speed.
    conflict_mask = [0] * n
    for i in range(n):
        mask = 0
        for j in adj[i]:
            mask |= 1 << j
        conflict_mask[i] = mask

    # We will use recursive backtracking with dynamic ordering:
    # choose an uncolored vertex with the most constraints (saturation degree, then degree).
    # To keep it simple and fast enough for n<=40, we implement a recursive function
    # that picks the next vertex using these heuristics.

    assigned = [False] * n
    # For each vertex, available colors bitmask (3 bits)
    avail = [0b111] * n

    # We'll store colors in 'color' array.

    def dfs(count):
        if count == n:
            return True
        # Choose uncolored vertex with smallest number of available colors, tie by degree.
 
        best_v = -1
        best_avail_count = 10
        best_degree = -1
        for v in range(n):
            if not assigned[v]:
                ac = bin(avail[v]).count("1")
                if ac < best_avail_count or (ac == best_avail_count and len(adj[v]) > best_degree):
                    best_avail_count = ac
                    best_degree = len(adj[v])
                    best_v = v
                    if ac == 1:
                        break
        v = best_v
        # Try colors that are available
        mask = avail[v]
        # Try colors in a fixed order; symmetry breaking: for first vertex, only color 0.

        # We can also break symmetry: if no vertex colored yet, only try color 0.
        # But our heuristic will pick first vertex anyway; we can enforce:
        if count == 0:
            # only try color 0 for the first chosen vertex
            colors_to_try = [0]
        else:
            colors_to_try = [c for c in range(3) if mask >> c & ]

        for c in colors_to_try:
 
            # Check if color c is actually available (should be)
            if not (mask >> c) & 1:
                continue
 
            # Assign
            color[v] = c
            assigned[v] = True
 
            # Save avail states for neighbors
            changed = []
            for nb in adj[v]:
                if not assigned[nb]:
                    if (avail[nb] >> c) & 1:
                        avail[nb] &= ~(1 << c)
                        changed.append(nb)
 
            if dfs(count + 1):
                return True
 
            # Undo
            for nb in changed:
                avail[nb] |= (1 << c)
            assigned[v] = False
            color[v] = -1
 
        return False

    if dfs(0):
        # Convert colors 0,1,2 to zones 1,2,3
        ans = [str(color[i] + 1) for i in range(n)]
        sys.stdout.write("YES\n" + " ".join(ans) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()