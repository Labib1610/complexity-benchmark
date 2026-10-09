import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    configs = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        configs.append((a, b, c))
    
    n = 3 * q
    max_sum = 9 * q - 3
    max_prod = 27 * q * q * q
    
    # Filter stable configurations
    stable = []
    for a, b, c in configs:
        if c - a >= 2 and a + b + c <= max_sum and a * b * c < max_prod:
            stable.append((a, b, c))
    
    # Build adjacency list: gear -> list of config indices
    gear_to_configs = [[] for _ in range(n + 1)]
    for idx, (a, b, c) in enumerate(stable):
        gear_to_configs[a].append(idx)
        gear_to_configs[b].append(idx)
        gear_to_configs[c].append(idx)
    
    # Track which gears are used
    used = [False] * (n + 1)
    result = []
    
    def backtrack(count):
        if count == q:
            return True
        
        # Find first unused gear
        first = 1
        while first <= n and used[first]:
            first += 1
        
        if first > n:
            return False
        
        # Try all stable configs containing 'first'
        for cfg_idx in gear_to_configs[first]:
            a, b, c = stable[cfg_idx]
            if not used[a] and not used[b] and not used[c]:
                used[a] = used[b] = used[c] = True
                result.append((a, b, c))
                if backtrack(count + 1):
                    return True
                result.pop()
                used[a] = used[b] = used[c] = False
        
        return False
    
    if backtrack(0):
        print("YES")
        for a, b, c in result:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()