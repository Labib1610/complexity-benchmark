import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    modules_by_freq = [[] for _ in range(k + 1)]
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        modules_by_freq[x].append((y, z))
        
    dp = [0] * (1 << k)
    dp[0] = -1
    
    for mask in range(1 << k):
        if dp[mask] == 0:
            continue
        i = bin(mask).count('1') + 1
        if i > k:
            continue
        for y, z in modules_by_freq[i]:
            if (mask >> (y - 1)) & 1:
                continue
            if (mask >> (k + z - 1)) & 1:
                continue
            new_mask = mask | (1 << (y - 1)) | (1 << (k + z - 1))
            if dp[new_mask] == 0:
                dp[new_mask] = mask
                
    full_mask = (1 << (2 * k)) - 1
    if dp[full_mask] == 0:
        print("NO")
        return
        
    print("YES")
    curr = full_mask
    res = []
    while curr != -1:
        prev = dp[curr]
        if prev == -1:
            break
        diff = curr ^ prev
        y = (diff & ((1 << k) - 1)).bit_length()
        z = (diff >> k).bit_length()
        i = bin(prev).count('1') + 1
        res.append(f"{i} {y} {z}")
        curr = prev
        
    print('\n'.join(res))

if __name__ == '__main__':
    solve()