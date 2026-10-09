import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q
    
    resonators = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        mask = (1 << a) | (1 << b) | (1 << c)
        resonators.append((mask, (a+1, b+1, c+1)))
    
    # For each band, list of resonator indices that cover it
    band_to_res = [[] for _ in range(n)]
    for idx, (mask, _) in enumerate(resonators):
        for band in range(n):
            if mask & (1 << band):
                band_to_res[band].append(idx)
    
    # Remove resonators that are duplicates? Not needed, but we can keep all.
    
    used = [False] * t
    chosen = []
    full_mask = (1 << n) - 1
    
    # Precompute mask for each resonator
    masks = [r[0] for r in resonators]
    
    def backtrack(covered_mask):
        if covered_mask == full_mask:
            return True
        # Find band with fewest available resonators
        best_band = -1
        best_options = None
        for band in range(n):
            if not (covered_mask & (1 << band)):
                options = [idx for idx in band_to_res[band] if not used[idx] and (masks[idx] & covered_mask) == 0]
                if best_band == -1 or len(options) < len(best_options):
                    best_band = band
                    best_options = options
                    if len(options) == 0:
                        return False
                    if len(options) == 1:
                        break
        # Try each option
        for idx in best_options:
            mask = masks[idx]
            used[idx] = True
            chosen.append(resonators[idx][1])
            if backtrack(covered_mask | mask):
                return True
            chosen.pop()
            used[idx] = False
        return False
    
    if backtrack(0):
        print("YES")
        for triple in chosen:
            print(*triple)
    else:
        print("NO")

if __name__ == "__main__":
    solve()