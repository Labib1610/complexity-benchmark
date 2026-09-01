import sys

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
        
    # dp[mask] = bitmask of available colors for the unassigned vertices
    # 1: color 1, 2: color 2, 4: color 3
    dp = [7] * (1 << n)
    dp[0] = (1 << n) - 1
    
    for mask in range(1 << n):
        if dp[mask] == 0:
            continue
        for i in range(n):
            if not (mask & (1 << i)):
                nxt = mask | (1 << i)
                # available colors for i: those not used by assigned neighbors
                avail = dp[mask] & (~(adj[i] & mask))
                if avail > dp[nxt]:
                    dp[nxt] = avail
                    
    if dp[-1] == 0:
        print("NO")
        return
        
    print("YES")
    ans = [0] * n
    mask = (1 << n) - 1
    for i in range(n - 1, -1, -1):
        avail = dp[mask] & (~(adj[i] & mask))
        # choose the smallest available color (1, 2, then 3)
        if avail & 1:
            ans[i] = 1
        elif avail & 2:
            ans[i] = 2
        else:
            ans[i] = 3
        mask ^= 1 << i
        
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    solve()