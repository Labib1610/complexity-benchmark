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
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    color = [0] * n
    allowed = [14] * n  # Bits 1, 2, 3 set (binary 1110)

    def backtrack(uncolored_mask):
        if uncolored_mask == 0:
            return True

        best_v = -1
        best_cand_count = 4
        best_deg = -1

        temp = uncolored_mask
        while temp:
            v = (temp & -temp).bit_length() - 1
            temp &= temp - 1

            cands = allowed[v]
            cnt = (cands >> 1 & 1) + (cands >> 2 & 1) + (cands >> 3 & 1)
            if cnt == 0:
                return False
            if cnt < best_cand_count:
                best_cand_count = cnt
                best_v = v
                best_deg = (adj[v] & uncolored_mask).bit_count()
            elif cnt == best_cand_count:
                deg = (adj[v] & uncolored_mask).bit_count()
                if deg > best_deg:
                    best_v = v
                    best_deg = deg

        v = best_v
        cands = allowed[v]
        rem_mask = uncolored_mask ^ (1 << v)

        for c in (1, 2, 3):
            if (cands >> c) & 1:
                color[v] = c
                mask_c = 1 << c
                affected = []
                nbrs = adj[v] & rem_mask
                dead_end = False

                while nbrs:
                    u = (nbrs & -nbrs).bit_length() - 1
                    nbrs &= nbrs - 1
                    if allowed[u] & mask_c:
                        allowed[u] ^= mask_c
                        affected.append(u)
                        if allowed[u] == 0:
                            dead_end = True

                if not dead_end and backtrack(rem_mask):
                    return True

                for u in affected:
                    allowed[u] |= mask_c
                color[v] = 0

        return False

    if backtrack((1 << n) - 1):
        print("YES")
        print(*(color[i] for i in range(n)))
    else:
        print("NO")


if __name__ == "__main__":
    solve()