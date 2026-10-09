import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    allowed = [[] for _ in range(k)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        allowed[x-1].append((y-1, z-1))
    
    full_mask = (1 << k) - 1
    # dp: dict mapping (maskY, maskZ) -> (prev_maskY, prev_maskZ, x, y, z)
    dp = {(0, 0): None}
    
    for x in range(k):
        new_dp = {}
        for (maskY, maskZ), prev in dp.items():
            for y, z in allowed[x]:
                if not (maskY >> y) & 1 and not (maskZ >> z) & 1:
                    new_maskY = maskY | (1 << y)
                    new_maskZ = maskZ | (1 << z)
                    if (new_maskY, new_maskZ) not in new_dp:
                        new_dp[(new_maskY, new_maskZ)] = (maskY, maskZ, x, y, z)
        dp = new_dp
        if not dp:
            print("NO")
            return
    
    if (full_mask, full_mask) not in dp:
        print("NO")
        return
    
    # Reconstruct
    state = (full_mask, full_mask)
    crews = []
    while state != (0, 0):
        prev_maskY, prev_maskZ, x, y, z = dp[state]
        crews.append((x+1, y+1, z+1))
        state = (prev_maskY, prev_maskZ)
    
    print("YES")
    for crew in reversed(crews):
        print(*crew)

if __name__ == "__main__":
    solve()