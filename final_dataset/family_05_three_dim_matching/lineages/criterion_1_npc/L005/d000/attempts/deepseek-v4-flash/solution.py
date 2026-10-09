import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    # comb[x][y] = bitmask of z values
    comb = [[0]*(k+1) for _ in range(k+1)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        comb[x][y] |= (1 << (z-1))
    
    full_mask = (1 << k) - 1
    # dp: dict mapping image_mask -> shard_mask
    dp = {0: 0}
    parent = {}
    
    for x in range(1, k+1):
        new_dp = {}
        for img_mask, shard_mask in dp.items():
            # try to assign an unused image
            for y in range(1, k+1):
                if img_mask & (1 << (y-1)):
                    continue
                # possible shards for this (x,y)
                possible = comb[x][y] & ~shard_mask
                # try each possible shard
                while possible:
                    bit = possible & -possible
                    z = bit.bit_length()  # 1-based
                    new_img_mask = img_mask | (1 << (y-1))
                    new_shard_mask = shard_mask | bit
                    if new_img_mask not in new_dp or new_shard_mask > new_dp[new_img_mask]:
                        new_dp[new_img_mask] = new_shard_mask
                        parent[(x, new_img_mask)] = (y, z, img_mask, shard_mask)
                    possible -= bit
        dp = new_dp
        if not dp:
            print("NO")
            return
    
    if full_mask in dp:
        print("YES")
        # reconstruct
        img_mask = full_mask
        shard_mask = dp[full_mask]
        assignment = []
        for x in range(k, 0, -1):
            y, z, prev_img_mask, prev_shard_mask = parent[(x, img_mask)]
            assignment.append((x, y, z))
            img_mask = prev_img_mask
            shard_mask = prev_shard_mask
        for x, y, z in reversed(assignment):
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()