import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    triples = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        triples.append((a, b, c))
    
    n = 3 * q
    # Build column indices: 0..n-1 for each person
    # We'll use Algorithm X with bitmasks for speed
    # Since n <= 600, we can use Python integers as bitmasks
    
    # Precompute bitmask for each triple
    masks = []
    for a, b, c in triples:
        mask = (1 << (a-1)) | (1 << (b-1)) | (1 << (c-1))
        masks.append(mask)
    
    full_mask = (1 << n) - 1
    
    # We'll do recursive backtracking with pruning
    # Keep track of used mask and chosen indices
    chosen = []
    
    # For pruning: sort triples by number of remaining uncovered elements? 
    # But we can just try in order with recursion.
    
    # We'll use a simple recursion with bitmask.
    # To speed up, we can precompute for each mask the list of triples that are subsets.
    # But n=600, t=20000, so we can just iterate.
    
    # We'll use recursion with memoization on (mask) -> bool
    from functools import lru_cache
    
    # But we also need to reconstruct solution, so we'll do iterative backtracking.
    
    # We'll sort triples by mask bit count descending? Actually we want to pick triples that cover many uncovered.
    # But simple DFS with pruning works if we pick the triple with smallest number of available options.
    
    # Let's implement recursive search with heuristic: choose the uncovered element with fewest triples covering it.
    
    # Precompute for each element the list of triple indices that contain it
    elem_to_triples = [[] for _ in range(n)]
    for idx, (a,b,c) in enumerate(triples):
        elem_to_triples[a-1].append(idx)
        elem_to_triples[b-1].append(idx)
        elem_to_triples[c-1].append(idx)
    
    # We'll use recursion with bitmask
    def search(mask, depth):
        if mask == full_mask:
            return True
        if depth == q:
            return False
        # Find uncovered element with fewest candidate triples
        best_elem = -1
        best_count = 10**9
        for i in range(n):
            if not (mask >> i) & 1:
                cnt = 0
                for idx in elem_to_triples[i]:
                    if (masks[idx] & mask) == 0:  # triple doesn't overlap with used
                        cnt += 1
                if cnt < best_count:
                    best_count = cnt
                    best_elem = i
                    if cnt == 0:
                        break
        if best_count == 0:
            return False
        # Try triples covering best_elem
        for idx in elem_to_triples[best_elem]:
            if (masks[idx] & mask) == 0:
                chosen.append(idx)
                if search(mask | masks[idx], depth+1):
                    return True
                chosen.pop()
        return False
    
    if search(0, 0):
        print("YES")
        for idx in chosen:
            print(*triples[idx])
    else:
        print("NO")

if __name__ == "__main__":
    solve()