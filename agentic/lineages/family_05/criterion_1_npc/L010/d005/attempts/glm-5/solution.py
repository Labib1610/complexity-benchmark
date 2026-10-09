import sys
from functools import lru_cache

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    relays = []
    for _ in range(t):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        c = int(input_data[idx]); idx += 1
        relays.append((a, b, c))
    
    # Group relays by a-value
    by_a = [[] for _ in range(k + 1)]
    for r in relays:
        by_a[r[0]].append(r)
    
    # Check if all a-values 1..k have at least one relay
    for i in range(1, k + 1):
        if not by_a[i]:
            print("NO")
            return
    
    # DFS: pick one relay for each a-value from 1 to k
    # State: (a_index, used_b_mask, used_c_mask)
    # We need to find a path to a_index = k+1
    
    import sys
    sys.setrecursionlimit(10000)
    
    memo = {}
    chosen = []
    
    def dfs(a_idx, used_b, used_c):
        if a_idx > k:
            return True
        key = (a_idx, used_b, used_c)
        if key in memo:
            return memo[key]
        
        for r in by_a[a_idx]:
            b, c = r[1], r[2]
            bbit = 1 << (b - 1)
            cbit = 1 << (c - 1)
            if (used_b & bbit) == 0 and (used_c & cbit) == 0:
                chosen.append(r)
                if dfs(a_idx + 1, used_b | bbit, used_c | cbit):
                    memo[key] = True
                    return True
                chosen.pop()
        
        memo[key] = False
        return False
    
    if dfs(1, 0, 0):
        print("YES")
        for r in chosen:
            print(f"{r[0]} {r[1]} {r[2]}")
    else:
        print("NO")

solve()