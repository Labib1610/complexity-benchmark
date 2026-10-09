import sys
sys.setrecursionlimit(1000000)

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    configs = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        configs.append((x-1, y-1, z-1))  # 0-indexed

    full_mask = (1 << k) - 1
    # Group configs by x
    by_x = [[] for _ in range(k)]
    for idx, (x, y, z) in enumerate(configs):
        by_x[x].append((y, z, idx))

    memo = {}
    chosen = []

    def dfs(mask_x, mask_y, mask_z):
        if mask_x == full_mask and mask_y == full_mask and mask_z == full_mask:
            return True
        if mask_x == full_mask:
            return False
        # pick smallest missing x
        # find first zero bit in mask_x
        # use bit trick
        inv = (~mask_x) & full_mask
        if inv == 0:
            return False
        x = (inv & -inv).bit_length() - 1
        key = (mask_x, mask_y, mask_z)
        if key in memo:
            return False  # already failed
        for y, z, idx in by_x[x]:
            if (mask_y >> y) & 1:
                continue
            if (mask_z >> z) & 1:
                continue
            chosen.append(idx)
            if dfs(mask_x | (1 << x), mask_y | (1 << y), mask_z | (1 << z)):
                return True
            chosen.pop()
        memo[key] = False
        return False

    if dfs(0, 0, 0):
        print("YES")
        for idx in chosen:
            x, y, z = configs[idx]
            print(x+1, y+1, z+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()