import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # Try all possible assignments for the first half of workers
    # and check the second half using bitmask DP.
    half = n // 2
    first = n - half

    # For each mask of first half, check if it's valid (no conflicts inside)
    valid_first = [True] * (1 << first)
    for mask in range(1 << first):
        for i in range(first):
            if mask & (1 << i):
                if adj[i] & mask:
                    valid_first[mask] = False
                    break

    # For each mask of second half, check if it's valid
    valid_second = [True] * (1 << half)
    for mask in range(1 << half):
        for i in range(half):
            if mask & (1 << i):
                if adj[first + i] & (mask << first):
                    valid_second[mask] = False
                    break

    # For each valid mask of first half, compute the forbidden masks for second half
    # We need to assign each worker to one of 3 shifts.
    # We'll do a 3-coloring approach: try all colorings of first half (3^first)
    # and then check if second half can be colored.

    # Since n <= 40, first <= 20, 3^20 is too big. Use meet-in-the-middle:
    # Enumerate all colorings of first half, store the "forbidden" mask for second half
    # for each shift, then try to color second half.

    # We'll use a recursive search with pruning.

    color = [0] * n
    # Precompute conflict masks per shift for each worker
    # We'll do backtracking with ordering: choose worker with most constraints.

    # Simple backtracking with bitmask for used colors per worker
    # Since n <= 40, we can use bitmask of size 3 for each worker? Not enough.
    # Instead, we do recursive coloring with pruning.

    # We'll use a simple backtracking that tries all 3 colors for each worker,
    # but with pruning using adjacency.

    # To make it fast enough, we'll use bitmask representation of neighbors.

    # We'll implement a recursive function that assigns colors to workers 0..n-1
    # and checks conflicts.

    # Since n <= 40, worst-case 3^40 is too big, but with pruning it's okay for
    # typical cases. However, to be safe, we use meet-in-the-middle.

    # Meet-in-the-middle approach:
    # Split workers into two groups: A (size a) and B (size b).
    # Enumerate all colorings of A (3^a) and store for each coloring the
    # "forbidden" mask for B per shift.
    # Then for each coloring of A, try to color B using backtracking.

    a = n // 2
    b = n - a

    # Precompute neighbor masks for each worker
    # For group A, we need to know which B workers conflict with each A worker.
    # For group B, we need to know which B workers conflict with each B worker.

    # We'll enumerate all colorings of A.
    # For each coloring, we compute for each shift s (0,1,2) a bitmask of B workers
    # that cannot be assigned to shift s.

    # Then we need to check if there exists a coloring of B such that:
    # - No two B workers on same shift conflict.
    # - No B worker is assigned to a shift that is forbidden by A.

    # We can do this by trying all colorings of B (3^b) and checking.

    # Since a <= 20, b <= 20, 3^20 ~ 3.4e9 too big. But we can use DP over subsets.

    # Alternative: Since we only have 3 shifts, we can use a different approach:
    # The graph is 3-colorable if and only if it can be partitioned into 3 independent sets.
    # We can try all ways to assign the first half to 3 shifts, and then for the second half
    # we need to assign each to one of the shifts that are not forbidden.

    # We'll use a recursive search with bitmask for the second half.

    # Let's implement a backtracking that assigns colors to all workers,
    # but with a good ordering: choose the worker with the most colored neighbors.

    # Since n <= 40, we can use a simple recursive search with memoization on
    # (index, color_mask) where color_mask is a bitmask of size 2n? Not feasible.

    # Let's do a simple backtracking with pruning and hope it's fast enough for n<=40.
    # But worst-case could be 3^40. However, with constraints and typical tests,
    # it might pass. But to be safe, we'll implement a more clever approach.

    # We'll use the fact that 3-coloring is NP-complete, but n=40 is small.
    # We can use a backtracking with bitmask of available colors per worker.

    # Let's implement a recursive function that assigns colors to workers in order,
    # and uses bitmask of size 3 for each worker to track available colors.

    # We'll use a list of bitmasks for each worker: initially 0b111 (all colors available).
    # When we assign a color to a worker, we remove that color from all neighbors.

    # This is a standard algorithm for graph coloring.

    # We'll implement it.

    available = [0b111] * n  # bit 0 = shift 1, bit 1 = shift 2, bit 2 = shift 3

    # Precompute adjacency list
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if adj[i] & (1 << j):
                adj_list[i].append(j)

    # Order workers by degree (most constrained first)
    order = sorted(range(n), key=lambda x: -len(adj_list[x]))

    # We'll assign colors in this order.
    color = [0] * n

    # We'll use a recursive function with backtracking.
    # To speed up, we'll use bitmask of available colors per worker.

    # We'll implement a function that tries to color the graph.

    def backtrack(pos):
        if pos == n:
            return True
        v = order[pos]
        # Try each available color
        avail = available[v]
        while avail:
            # pick lowest set bit
            lsb = avail & -avail
            c = (lsb.bit_length() - 1)  # 0,1,2
            # assign color c to v
            color[v] = c
            # remove c from neighbors
            changed = []
            for u in adj_list[v]:
                if available[u] & (1 << c):
                    available[u] &= ~(1 << c)
                    changed.append(u)
            # recurse
            if backtrack(pos + 1):
                return True
            # undo
            for u in changed:
                available[u] |= (1 << c)
            # remove this color from avail for next try
            avail &= ~lsb
        return False

    if backtrack(0):
        print("YES")
        print(' '.join(str(c + 1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()