import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q
    triples = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))

    # Precompute bitmask for each triple
    masks = []
    for a, b, c in triples:
        masks.append((1 << a) | (1 << b) | (1 << c))

    full_mask = (1 << n) - 1

    # Sort triples by number of remaining possibilities? We'll just backtrack.
    # Use memoization: state = (mask, idx) but mask alone is enough if we iterate over all triples each time.
    # But we can do better: choose the first uncovered item and try triples containing it.

    # Build list of triples per item
    by_item = [[] for _ in range(n)]
    for i, (a, b, c) in enumerate(triples):
        by_item[a].append(i)
        by_item[b].append(i)
        by_item[c].append(i)

    chosen = []
    used = [False] * t

    def backtrack(mask):
        if mask == full_mask:
            return True
        # Find first uncovered item
        # Find lowest zero bit
        inv = (~mask) & full_mask
        if inv == 0:
            return True
        # lowest set bit
        item = (inv & -inv).bit_length() - 1
        for idx in by_item[item]:
            if used[idx]:
                continue
            m = masks[idx]
            if mask & m:
                continue
            used[idx] = True
            chosen.append(idx)
            if backtrack(mask | m):
                return True
            chosen.pop()
            used[idx] = False
        return False

    if backtrack(0):
        print("YES")
        for idx in chosen:
            a, b, c = triples[idx]
            print(a + 1, b + 1, c + 1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()