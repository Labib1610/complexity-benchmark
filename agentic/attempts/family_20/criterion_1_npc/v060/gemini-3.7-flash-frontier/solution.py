import sys

# Increase recursion depth just in case
sys.setrecursionlimit(20000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    u_of = [0] * m
    v_of = [0] * m
    adj_edges = [[] for _ in range(n + 1)]

    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        u_of[i] = u
        v_of[i] = v
        adj_edges[u].append(i)
        adj_edges[v].append(i)

    # Precomputed tables for 3-bit masks (0..7)
    # Bits 0, 1, 2 correspond to colors 1, 2, 3
    popcnt = [0, 1, 1, 2, 1, 2, 2, 3]
    first_col = [-1, 1, 2, 1, 3, 1, 2, 1]

    used_mask = [0] * (n + 1)
    color_of = [-1] * m
    unassigned = set(range(m))

    def backtrack():
        if not unassigned:
            return True

        # Find the most constrained edge and check for dead ends / forced choices
        forced = []
        best_edge = -1
        min_choices = 4

        # Check all unassigned edges
        # Prioritize 0 choices (immediate failure) and 1 choice (forced)
        for e in unassigned:
            u, v = u_of[e], v_of[e]
            mask = 7 & ~(used_mask[u] | used_mask[v])
            cnt = popcnt[mask]
            if cnt == 0:
                return False
            if cnt == 1:
                forced.append((e, first_col[mask]))
            elif cnt < min_choices:
                min_choices = cnt
                best_edge = e

        # Process forced assignments
        if forced:
            applied = []
            possible = True
            for e, col in forced:
                if color_of[e] != -1:
                    continue
                u, v = u_of[e], v_of[e]
                c_bit = 1 << (col - 1)
                if (used_mask[u] & c_bit) or (used_mask[v] & c_bit):
                    possible = False
                    break
                used_mask[u] |= c_bit
                used_mask[v] |= c_bit
                color_of[e] = col
                unassigned.remove(e)
                applied.append((e, col))

            if possible and backtrack():
                return True

            for e, col in reversed(applied):
                u, v = u_of[e], v_of[e]
                c_bit = 1 << (col - 1)
                used_mask[u] &= ~c_bit
                used_mask[v] &= ~c_bit
                color_of[e] = -1
                unassigned.add(e)

            return False

        # Branch on best_edge
        e = best_edge
        u, v = u_of[e], v_of[e]
        mask = 7 & ~(used_mask[u] | used_mask[v])
        unassigned.remove(e)

        for col in (1, 2, 3):
            c_bit = 1 << (col - 1)
            if mask & c_bit:
                used_mask[u] |= c_bit
                used_mask[v] |= c_bit
                color_of[e] = col

                if backtrack():
                    return True

                used_mask[u] &= ~c_bit
                used_mask[v] &= ~c_bit
                color_of[e] = -1

        unassigned.add(e)
        return False

    if backtrack():
        print("YES")
        print(*(color_of[i] for i in range(m)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()