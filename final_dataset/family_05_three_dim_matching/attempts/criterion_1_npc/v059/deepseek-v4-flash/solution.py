import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    catalog = [[] for _ in range(k)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        catalog[x-1].append((y-1, z-1))
    
    full_mask = (1 << k) - 1
    dp = [[False] * (1 << k) for _ in range(1 << k)]
    parent = [[None] * (1 << k) for _ in range(1 << k)]
    
    dp[0][0] = True
    
    for chassis in range(k):
        new_dp = [[False] * (1 << k) for _ in range(1 << k)]
        for pmask in range(1 << k):
            for lmask in range(1 << k):
                if not dp[pmask][lmask]:
                    continue
                used = bin(pmask).count("1")
                if used != chassis:
                    continue
                for y, z in catalog[chassis]:
                    if not (pmask & (1 << y)) and not (lmask & (1 << z)):
                        npmask = pmask | (1 << y)
                        nlmask = lmask | (1 << z)
                        if not new_dp[npmask][nlmask]:
                            new_dp[npmask][nlmask] = True
                            parent[npmask][nlmask] = (pmask, lmask, y, z)
        dp = new_dp
    
    if not dp[full_mask][full_mask]:
        print("NO")
        return
    
    print("YES")
    # Reconstruct
    pmask = full_mask
    lmask = full_mask
    result = []
    for chassis in range(k-1, -1, -1):
        p_prev, l_prev, y, z = parent[pmask][lmask]
        result.append((chassis+1, y+1, z+1))
        pmask, lmask = p_prev, l_prev
    
    for x, y, z in reversed(result):
        print(x, y, z)

if __name__ == "__main__":
    solve()