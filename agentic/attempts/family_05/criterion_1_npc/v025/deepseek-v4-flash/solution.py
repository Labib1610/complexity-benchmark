import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    # Store viable combinations per source
    combos = [[] for _ in range(k)]
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        combos[x].append((y, z))
    
    # Sort combos for deterministic behavior
    for i in range(k):
        combos[i].sort()
    
    used_ref = [False] * k
    used_det = [False] * k
    chosen = [None] * k
    
    # Precompute for pruning: for each source, list of possible (ref, det) pairs
    # We'll do backtracking
    
    def backtrack(src_idx):
        if src_idx == k:
            return True
        for y, z in combos[src_idx]:
            if not used_ref[y] and not used_det[z]:
                used_ref[y] = True
                used_det[z] = True
                chosen[src_idx] = (src_idx + 1, y + 1, z + 1)
                if backtrack(src_idx + 1):
                    return True
                used_ref[y] = False
                used_det[z] = False
        return False
    
    if backtrack(0):
        print("YES")
        for x, y, z in chosen:
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()