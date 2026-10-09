import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    triads = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        mask = (1 << a) | (1 << b) | (1 << c)
        triads.append((mask, (a+1, b+1, c+1)))
    
    n = 3 * q
    full_mask = (1 << n) - 1
    # Sort triads maybe by number of bits (lowest common) for pruning
    triads.sort(key=lambda x: x[0].bit_count())
    
    chosen_masks = []
    chosen_list = []
    
    # Quick pruning: total coverage can't exceed items
    # Basic backtracking
    def backtrack(start, covered):
        if covered == full_mask:
            return True
        # Choose next uncovered artifact
        for i in range(n):
            if not (covered >> i) & 1:
                first_uncovered = i
                break
        else:
            return False
        
        # Try triads containing this artifact
        for idx in range(t):
            mask, triad = triads[idx]
            if (mask >> first_uncovered) & 1 and (mask & covered) == 0:
                chosen_masks.append(mask)
                chosen_list.append(triad)
                if backtrack(idx+1, covered | mask):
                    return True
                chosen_masks.pop()
                chosen_list.pop()
        return False
    
    if backtrack(0, 0):
        print("YES")
        for triad in chosen_list:
            print(*triad)
    else:
        print("NO")

if __name__ == "__main__":
    solve()