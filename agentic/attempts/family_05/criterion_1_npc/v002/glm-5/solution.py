import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(k+1)]
    for _ in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        adj[x].append((y-1, z-1))
    
    k1 = k // 2
    k2 = k - k1
    
    X1 = list(range(1, k1+1))
    X2 = list(range(k1+1, k+1))
    
    def enumerate_half(X_list):
        n = len(X_list)
        if n == 0:
            return {(0, 0): []}
        results = defaultdict(list)
        size = 1 << n
        dp = [None] * size
        dp[0] = [(0, 0, [])]
        for mask in range(size):
            if dp[mask] is None:
                continue
            for i in range(n):
                if mask & (1 << i):
                    continue
            for i in range(n):
                if mask & (1 << i):
                    continue
                new_mask = mask | (1 << i)
                x = X_list[i]
                for y, z in adj[x]:
                    for ymask, zmask, assigns in dp[mask]:
                        if ymask & (1 << y):
                            continue
                        if zmask & (1 << z):
                            continue
                        new_assigns = assigns + [(x, y+1, z+1)]
                        if dp[new_mask] is None:
                            dp[new_mask] = []
                        dp[new_mask].append((ymask | (1 << y), zmask | (1 << z), new_assigns))
        full = size - 1
        if dp[full] is None:
            return {}
        for ymask, zmask, assigns in dp[full]:
            results[(ymask, zmask)].append(assigns)
        return results
    
    R1 = enumerate_half(X1)
    if X1 and not R1:
        print("NO")
        return
    
    R2 = enumerate_half(X2)
    if X2 and not R2:
        print("NO")
        return
    
    full_mask = (1 << k) - 1
    
    if not X1:
        for key, assigns_list in R2.items():
            if key == (full_mask, full_mask):
                print("YES")
                for a in assigns_list[0]:
                    print(f"{a[0]} {a[1]} {a[2]}")
                return
        print("NO")
        return
    
    if not X2:
        for key, assigns_list in R1.items():
            if key == (full_mask, full_mask):
                print("YES")
                for a in assigns_list[0]:
                    print(f"{a[0]} {a[1]} {a[2]}")
                return
        print("NO")
        return
    
    small, big = (R1, R2) if len(R1) <= len(R2) else (R2, R1)
    
    for (y1, z1), assigns1 in small.items():
        y2 = full_mask & ~y1
        z2 = full_mask & ~z1
        if (y2, z2) in big:
            a1 = assigns1[0]
            a2 = big[(y2, z2)][0]
            print("YES")
            for a in a1 + a2:
                print(f"{a[0]} {a[1]} {a[2]}")
            return
    
    print("NO")

solve()