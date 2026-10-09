import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    allowed = [[0] * k for _ in range(k)]  # allowed[f][m] bitmask of demographics
    for _ in range(t):
        d, f, m = map(int, input().split())
        d -= 1
        f -= 1
        m -= 1
        allowed[f][m] |= (1 << d)

    full_mask = (1 << k) - 1
    # dp[mask_f][mask_m] = mask_d or -1 if impossible
    dp = [[-1] * (1 << k) for _ in range(1 << k)]
    dp[0][0] = 0

    # Iterate over all combinations of f and m masks
    for mask_f in range(1 << k):
        for mask_m in range(1 << k):
            if dp[mask_f][mask_m] == -1:
                continue
            # Try to add a new arm
            # pick next unused formulation
            for f in range(k):
                if mask_f & (1 << f):
                    continue
                # pick next unused facility
                for m in range(k):
                    if mask_m & (1 << m):
                        continue
                    # pick a demographic from allowed[f][m] not used yet
                    avail_d = allowed[f][m] & ~dp[mask_f][mask_m]
                    while avail_d:
                        d_bit = avail_d & -avail_d
                        avail_d -= d_bit
                        new_mask_f = mask_f | (1 << f)
                        new_mask_m = mask_m | (1 << m)
                        new_mask_d = dp[mask_f][mask_m] | d_bit
                        if dp[new_mask_f][new_mask_m] == -1:
                            dp[new_mask_f][new_mask_m] = new_mask_d
                # after trying all facilities for this f, break to avoid duplicate work
                break

    if dp[full_mask][full_mask] == -1:
        print("NO")
        return

    # Reconstruct
    mask_f = full_mask
    mask_m = full_mask
    mask_d = dp[full_mask][full_mask]
    arms = []
    while mask_f:
        # find one used f
        f = (mask_f & -mask_f).bit_length() - 1
        # find one used m
        m = (mask_m & -mask_m).bit_length() - 1
        # find one used d
        d = (mask_d & -mask_d).bit_length() - 1
        arms.append((d + 1, f + 1, m + 1))
        # remove them
        mask_f ^= (1 << f)
        mask_m ^= (1 << m)
        mask_d ^= (1 << d)

    print("YES")
    for d, f, m in arms:
        print(d, f, m)

if __name__ == "__main__":
    solve()