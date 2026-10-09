import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u != v:
            adj[u] |= 1 << v
            adj[v] |= 1 << u

    # Check for self-loops
    # Problem statement says distinct pairs, but if u == v was possible, it's not 3-colorable.

    # 3-coloring using DSatur / MRV backtracking
    color = [-1] * n
    mask = [7] * n  # bitmask of available colors: 1 (color 0), 2 (color 1), 4 (color 2)
    assigned_count = 0

    # Precompute degrees for tie-breaking
    degree = [bin(adj[i]).count("1") for i in range(n)]

    def backtrack():
        nonlocal assigned_count
        if assigned_count == n:
            return True

        # Find unassigned vertex with minimum available colors (MRV)
        best_u = -1
        best_cnt = 4
        best_deg = -1

        for u in range(n):
            if color[u] == -1:
                cnt = bin(mask[u]).count("1")
                if cnt == 0:
                    return False
                if cnt < best_cnt or (cnt == best_cnt and degree[u] > best_deg):
                    best_cnt = cnt
                    best_deg = degree[u]
                    best_u = u
                    if cnt == 1:
                        break

        u = best_u
        u_mask = mask[u]

        # Try colors
        for c in (0, 1, 2):
            if (u_mask & (1 << c)) != 0:
                color[u] = c
                assigned_count += 1

                # Update neighbors
                changed = []
                conflict = False
                c_bit_inv = ~(1 << c)

                nbrs = adj[u]
                while nbrs:
                    lsb = nbrs & -nbrs
                    v = (lsb.bit_length() - 1)
                    nbrs ^= lsb

                    if color[v] == -1 and (mask[v] & (1 << c)):
                        mask[v] &= c_bit_inv
                        changed.append(v)
                        if mask[v] == 0:
                            conflict = True

                if not conflict:
                    if backtrack():
                        return True

                # Restore
                c_bit = 1 << c
                for v in changed:
                    mask[v] |= c_bit
                color[u] = -1
                assigned_count -= 1

        return False

    if backtrack():
        print("YES")
        print(*(color[i] + 1 for i in range(n)))
    else:
        print("NO")


if __name__ == "__main__":
    solve()