import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    relays = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        relays.append((a, b, c))
    
    # Pre-filter: each relay must have all values <= k (given) and we need each coordinate to be a permutation.
    # We'll do DFS.
    
    # Sort relays maybe by some heuristic: e.g., by sum of values or by rarity.
    # We'll just keep original order.
    
    full_mask = (1 << k) - 1
    chosen = []
    
    # We'll use recursion with bitmasks.
    # To speed up, we can precompute for each relay the bit for each coordinate.
    relay_bits = []
    for a, b, c in relays:
        if 1 <= a <= k and 1 <= b <= k and 1 <= c <= k:
            relay_bits.append((1 << (a-1), 1 << (b-1), 1 << (c-1), (a,b,c)))
        # else skip? But constraints say all <= k, so no skip needed.
    
    # We'll do DFS with pruning: if remaining relays < needed, fail.
    # Also, we can check if for each coordinate, the number of unused values equals number of remaining relays.
    
    def dfs(mask_a, mask_b, mask_c, start_idx, chosen_list):
        if len(chosen_list) == k:
            return True
        # Prune: if not enough relays left
        if start_idx >= len(relay_bits):
            return False
        # Prune: if any coordinate has more unused values than remaining slots
        remaining = k - len(chosen_list)
        if bin(mask_a).count("1") != remaining or bin(mask_b).count("1") != remaining or bin(mask_c).count("1") != remaining:
            return False
        
        for i in range(start_idx, len(relay_bits)):
            ba, bb, bc, triple = relay_bits[i]
            if (mask_a & ba) == 0 and (mask_b & bb) == 0 and (mask_c & bc) == 0:
                chosen_list.append(triple)
                if dfs(mask_a | ba, mask_b | bb, mask_c | bc, i+1, chosen_list):
                    return True
                chosen_list.pop()
        return False
    
    if dfs(0, 0, 0, 0, chosen):
        print("YES")
        for a,b,c in chosen:
            print(a,b,c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()