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
        mask = (1 << a) | (1 << b) | (1 << c)
        triples.append((mask, (a + 1, b + 1, c + 1)))

    # For each vial, list indices of triples containing it
    vial_to_triples = [[] for _ in range(n)]
    for idx, (mask, _) in enumerate(triples):
        for v in range(n):
            if mask & (1 << v):
                vial_to_triples[v].append(idx)

    full_mask = (1 << n) - 1
    chosen = []
    used_triples = [False] * t

    # Precompute masks for each triple index
    masks = [m for m, _ in triples]

    # Recursive search
    def dfs(covered_mask):
        if covered_mask == full_mask:
            return True
        # Find first uncovered vial
        # We can find the least significant zero bit
        # Use bit trick: ~covered_mask & full_mask gives uncovered bits
        uncovered = (~covered_mask) & full_mask
        # pick the first uncovered vial
        v = (uncovered & -uncovered).bit_length() - 1
        # Try triples containing v
        for idx in vial_to_triples[v]:
            if used_triples[idx]:
                continue
            m = masks[idx]
            if m & covered_mask:
                continue
            # choose
            used_triples[idx] = True
            chosen.append(triples[idx][1])
            if dfs(covered_mask | m):
                return True
            chosen.pop()
            used_triples[idx] = False
        return False

    if dfs(0):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()