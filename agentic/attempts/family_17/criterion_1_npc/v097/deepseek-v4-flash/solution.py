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
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))
    
    n = 3 * q
    # For each element, list of triple indices
    elem_to_triples = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(triples):
        elem_to_triples[a].append(idx)
        elem_to_triples[b].append(idx)
        elem_to_triples[c].append(idx)
    
    # Precompute bitmask for each triple
    triple_mask = []
    for a, b, c in triples:
        mask = (1 << a) | (1 << b) | (1 << c)
        triple_mask.append(mask)
    
    full_mask = (1 << n) - 1
    
    chosen = []
    
    # Recursive backtracking
    def dfs(mask):
        if mask == full_mask:
            return True
        # Find first uncovered element
        # We can find the lowest zero bit
        # Python trick: ~mask & full_mask gives uncovered bits
        uncovered = (~mask) & full_mask
        # lowest set bit
        low = uncovered & -uncovered
        elem = low.bit_length() - 1
        # Try each triple containing elem
        for idx in elem_to_triples[elem]:
            if mask & triple_mask[idx] == 0:
                chosen.append(idx)
                if dfs(mask | triple_mask[idx]):
                    return True
                chosen.pop()
        return False
    
    if dfs(0):
        print("YES")
        for idx in chosen:
            a, b, c = triples[idx]
            print(a+1, b+1, c+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()