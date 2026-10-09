import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    for i in range(1, n + 1):
        adj[i] |= 1 << i
    
    full = (1 << (n + 1)) - 1
    mask_all = (1 << (n + 1)) - 2
    
    if k == 0:
        print("YES")
        print()
        return
    
    memo = {}
    
    def max_independent_set(available):
        if available == 0:
            return 0, 0
        if available in memo:
            return memo[available]
        
        v = (available & -available).bit_length() - 1
        
        size_with, set_with = max_independent_set(available & ~adj[v])
        size_with += 1
        set_with |= 1 << v
        
        size_without, set_without = max_independent_set(available & ~(1 << v))
        
        if size_with >= size_without:
            result = (size_with, set_with)
        else:
            result = (size_without, set_without)
        
        memo[available] = result
        return result
    
    max_size, chosen_set = max_independent_set(mask_all)
    
    if max_size >= k:
        selected = []
        for i in range(1, n + 1):
            if chosen_set & (1 << i):
                selected.append(i)
                if len(selected) == k:
                    break
        print("YES")
        print(' '.join(map(str, selected)))
    else:
        print("NO")

solve()