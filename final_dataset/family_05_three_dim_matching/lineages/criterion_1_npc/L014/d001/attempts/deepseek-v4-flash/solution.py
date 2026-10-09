import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    reactions = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        reactions.append((x-1, y-1, z-1))
    
    # dp[maskX][maskY] = (possible, parent_reaction_index)
    # We'll store parent to reconstruct
    size = 1 << k
    dp = [[None] * size for _ in range(size)]
    dp[0][0] = (-1, -1)  # (prev_reaction_index, prev_maskX, prev_maskY) but we'll store differently
    
    # We'll store as: dp[maskX][maskY] = (prev_maskX, prev_maskY, reaction_index)
    dp[0][0] = (0, 0, -1)
    
    for idx, (x, y, z) in enumerate(reactions):
        bitX = 1 << x
        bitY = 1 << y
        # We need to iterate masks in reverse to avoid using same reaction multiple times
        for maskX in range(size-1, -1, -1):
            if maskX & bitX:
                continue
            new_maskX = maskX | bitX
            for maskY in range(size-1, -1, -1):
                if maskY & bitY:
                    continue
                if dp[maskX][maskY] is None:
                    continue
                new_maskY = maskY | bitY
                if dp[new_maskX][new_maskY] is None:
                    dp[new_maskX][new_maskY] = (maskX, maskY, idx)
    
    full_mask = size - 1
    if dp[full_mask][full_mask] is None:
        print("NO")
        return
    
    # Reconstruct
    chosen = []
    maskX, maskY = full_mask, full_mask
    while maskX != 0 or maskY != 0:
        prevX, prevY, ridx = dp[maskX][maskY]
        chosen.append(reactions[ridx])
        maskX, maskY = prevX, prevY
    
    print("YES")
    for x, y, z in chosen:
        print(x+1, y+1, z+1)

if __name__ == "__main__":
    solve()