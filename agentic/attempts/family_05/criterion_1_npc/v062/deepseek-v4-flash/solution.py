import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    edges = [[] for _ in range(k)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        x -= 1
        y -= 1
        z -= 1
        edges[x].append((y, z))
    
    # dp[mask_t][mask_d] = True if possible to assign first i sources
    # We'll do iterative over sources.
    # Since k <= 22, mask size up to 2^22 ~ 4M, too big for 2D.
    # Instead, we do DP over sources with state (mask_t, mask_d) but only store reachable states.
    
    # We'll use dictionary for each source step.
    # dp: dict mapping (mask_t, mask_d) -> parent info
    dp = {(0, 0): None}
    
    for i in range(k):
        new_dp = {}
        for (mask_t, mask_d), parent in dp.items():
            for y, z in edges[i]:
                if not (mask_t >> y) & 1 and not (mask_d >> z) & 1:
                    new_mask_t = mask_t | (1 << y)
                    new_mask_d = mask_d | (1 << z)
                    if (new_mask_t, new_mask_d) not in new_dp:
                        new_dp[(new_mask_t, new_mask_d)] = (i, y, z, (mask_t, mask_d))
        dp = new_dp
        if not dp:
            print("NO")
            return
    
    # Check if full mask is reached
    full_mask = (1 << k) - 1
    if (full_mask, full_mask) in dp:
        print("YES")
        # reconstruct
        state = (full_mask, full_mask)
        result = []
        while dp[state] is not None:
            i, y, z, prev_state = dp[state]
            result.append((i+1, y+1, z+1))
            state = prev_state
        result.reverse()
        for x, y, z in result:
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()