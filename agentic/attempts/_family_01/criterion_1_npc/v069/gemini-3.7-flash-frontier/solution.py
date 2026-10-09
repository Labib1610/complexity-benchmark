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
    deg = [0] * n
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        if u != v:
            if not (adj[u] & (1 << v)):
                adj[u] |= 1 << v
                adj[v] |= 1 << u
                deg[u] += 1
                deg[v] += 1

    color = [-1] * n
    mask = [7] * n  # bits 0, 1, 2 represent colors 1, 2, 3

    # Fast bit count for numbers 0..7
    bit_count = [0, 1, 1, 2, 1, 2, 2, 3]

    uncolored = (1 << n) - 1

    def backtrack(curr_uncolored):
        if curr_uncolored == 0:
            return True

        # Find uncolored vertex with minimum available colors, tie-break by highest degree
        best_u = -1
        best_cnt = 4
        best_deg = -1

        temp = curr_uncolored
        while temp:
            u = (temp & -temp).bit_length() - 1
            temp &= temp - 1

            cnt = bit_count[mask[u]]
            if cnt < best_cnt:
                best_cnt = cnt
                best_deg = deg[u]
                best_u = u
                if cnt <= 1:
                    break
            elif cnt == best_cnt:
                if deg[u] > best_deg:
                    best_deg = deg[u]
                    best_u = u

        if best_cnt == 0:
            return False

        u = best_u
        u_bit = 1 << u
        u_adj = adj[u] & curr_uncolored

        # Try each available color
        u_mask = mask[u]
        for c in (0, 1, 2):
            c_bit = 1 << c
            if u_mask & c_bit:
                color[u] = c + 1
                # Forward checking: remove c_bit from neighbors
                affected = []
                temp_adj = u_adj
                valid = True
                while temp_adj:
                    v = (temp_adj & -temp_adj).bit_length() - 1
                    temp_adj &= temp_adj - 1
                    if mask[v] & c_bit:
                        mask[v] ^= c_bit
                        affected.append(v)
                        if mask[v] == 0:
                            valid = False

                if valid and backtrack(curr_uncolored ^ u_bit):
                    return True

                # Undo forward checking
                for v in affected:
                    mask[v] |= c_bit
                color[u] = -1

        return False

    if backtrack(uncolored):
        print("YES")
        print(*(color[i] for i in range(n)))
    else:
        print("NO")


if __name__ == "__main__":
    solve()