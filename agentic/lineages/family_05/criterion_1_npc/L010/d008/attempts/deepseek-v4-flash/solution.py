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
    
    # If t < k, impossible
    if t < k:
        print("NO")
        return
    
    # We'll try to pick k relays
    # Use bitmasks for each coordinate to track used values
    full_mask = (1 << k) - 1
    chosen = []
    
    # Sort relays maybe helps? Not necessary but can prune
    # We'll do backtracking with pruning
    
    def backtrack(idx, mask_a, mask_b, mask_c, chosen_list):
        if len(chosen_list) == k:
            return True
        if idx == t:
            return False
        # Prune: if remaining relays < needed
        if t - idx < k - len(chosen_list):
            return False
        
        a, b, c = relays[idx]
        bit_a = 1 << (a - 1)
        bit_b = 1 << (b - 1)
        bit_c = 1 << (c - 1)
        
        # Try taking this relay if possible
        if not (mask_a & bit_a) and not (mask_b & bit_b) and not (mask_c & bit_c):
            chosen_list.append((a, b, c))
            if backtrack(idx + 1, mask_a | bit_a, mask_b | bit_b, mask_c | bit_c, chosen_list):
                return True
            chosen_list.pop()
        
        # Try skipping this relay
        if backtrack(idx + 1, mask_a, mask_b, mask_c, chosen_list):
            return True
        
        return False
    
    if backtrack(0, 0, 0, 0, chosen):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()