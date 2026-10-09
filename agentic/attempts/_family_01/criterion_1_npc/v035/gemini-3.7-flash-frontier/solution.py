import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        if u != v:
            adj[u] |= 1 << v
            adj[v] |= 1 << u

    # Check for self-loops
    # Problem says u v conflicting pair, usually simple graph, but if self loop, impossible
    # In 0-indexed, if u == v, handled? 3-coloring a self-loop is impossible.

    assignment = [-1] * n
    # mask of available colors for each vertex: bit 0: color 0, bit 1: color 1, bit 2: color 2
    # initially 7 (binary 111) for all vertices
    available = [7] * n

    popcount_table = [0, 1, 1, 2, 1, 2, 2, 3]

    def get_unassigned_degree(u):
        # count unassigned neighbors
        deg = 0
        mask = adj[u]
        while mask > 0:
            v = (mask & -mask).bit_length() - 1
            if assignment[v] == -1:
                deg += 1
            mask &= mask - 1
        return deg

    def backtrack(assigned_count):
        if assigned_count == n:
            return True

        # Pick vertex with minimum available colors > 0
        # If any unassigned has 0 available colors, fail immediately.
        best_u = -1
        min_colors = 4
        max_deg = -1

        for u in range(n):
            if assignment[u] == -1:
                cnt = popcount_table[available[u]]
                if cnt == 0:
                    return False
                if cnt < min_colors:
                    min_colors = cnt
                    max_deg = get_unassigned_degree(u)
                    best_u = u
                    if cnt == 1:
                        # Cannot do better than 1
                        break
                elif cnt == min_colors:
                    deg = get_unassigned_degree(u)
                    if deg > max_deg:
                        max_deg = deg
                        best_u = u

        u = best_u
        u_avail = available[u]

        # Try colors for u
        for c in range(3):
            if (u_avail & (1 << c)) != 0:
                assignment[u] = c
                # Update neighbors and keep track of changes to revert
                color_mask = 1 << c
                changed_neighbors = []
                mask = adj[u]
                while mask > 0:
                    v = (mask & -mask).bit_length() - 1
                    if assignment[v] == -1 and (available[v] & color_mask) != 0:
                        available[v] ^= color_mask
                        changed_neighbors.append(v)
                    mask &= mask - 1

                if backtrack(assigned_count + 1):
                    return True

                # Revert
                for v in changed_neighbors:
                    available[v] |= color_mask
                assignment[u] = -1

        return False

    if backtrack(0):
        print("YES")
        print(*(assignment[i] + 1 for i in range(n)))
    else:
        print("NO")


if __name__ == "__main__":
    solve()