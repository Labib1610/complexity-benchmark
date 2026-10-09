import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q
    triads = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        triads.append((a, b, c))
    
    # Build adjacency: for each person, list of triad indices containing them
    person_to_triads = [[] for _ in range(n + 1)]
    for idx, (a, b, c) in enumerate(triads):
        person_to_triads[a].append(idx)
        person_to_triads[b].append(idx)
        person_to_triads[c].append(idx)
    
    used = [False] * t
    assigned = [False] * (n + 1)
    chosen = []
    
    # Precompute bitmask for each triad for fast overlap check
    triad_mask = []
    for a, b, c in triads:
        mask = (1 << (a - 1)) | (1 << (b - 1)) | (1 << (c - 1))
        triad_mask.append(mask)
    
    full_mask = (1 << n) - 1
    
    # Backtracking with pruning: always pick the smallest unassigned person
    def backtrack(mask):
        if mask == full_mask:
            return True
        # find first unassigned person
        # use bit trick to find lowest zero bit
        inv = (~mask) & full_mask
        # lowest set bit
        low = inv & -inv
        person = low.bit_length()  # 1-indexed
        for tidx in person_to_triads[person]:
            if used[tidx]:
                continue
            tm = triad_mask[tidx]
            if mask & tm:
                continue
            used[tidx] = True
            chosen.append(tidx)
            if backtrack(mask | tm):
                return True
            chosen.pop()
            used[tidx] = False
        return False
    
    if backtrack(0):
        print("YES")
        for idx in chosen:
            a, b, c = triads[idx]
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()