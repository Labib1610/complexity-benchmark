import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    triples = []
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x, y, z))
    
    # Sort by some heuristic: e.g., by number of remaining options
    # We'll just sort by (x, y, z) for determinism
    triples.sort()
    
    used_x = 0
    used_y = 0
    used_z = 0
    chosen = []
    
    # Precompute for each triple a bitmask for x, y, z
    triples = [(1 << x, 1 << y, 1 << z, x, y, z) for (x, y, z) in triples]
    
    full_mask = (1 << k) - 1
    
    # Backtracking with pruning
    def backtrack(idx, used_x, used_y, used_z, chosen):
        if len(chosen) == k:
            return True
        # Prune: if remaining triples not enough
        if idx >= len(triples):
            return False
        # Try to pick next triple
        for i in range(idx, len(triples)):
            mx, my, mz, x, y, z = triples[i]
            if (used_x & mx) == 0 and (used_y & my) == 0 and (used_z & mz) == 0:
                chosen.append((x, y, z))
                if backtrack(i + 1, used_x | mx, used_y | my, used_z | mz, chosen):
                    return True
                chosen.pop()
        return False
    
    if backtrack(0, 0, 0, 0, chosen):
        print("YES")
        for x, y, z in chosen:
            print(x + 1, y + 1, z + 1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()