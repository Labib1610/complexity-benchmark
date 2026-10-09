import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        triples.append((a-1, b-1, c-1))  # 0-indexed

    n = 3 * q
    full_mask = (1 << n) - 1

    # Precompute bitmask for each triple
    triple_masks = []
    for a, b, c in triples:
        mask = (1 << a) | (1 << b) | (1 << c)
        triple_masks.append(mask)

    # We'll do backtracking with pruning
    used = [False] * t
    chosen = []
    # For faster pruning, sort triples by size? They are all size 3.
    # We'll try to pick the first uncovered module and try triples containing it.

    # Build adjacency: for each module, list of triple indices containing it
    adj = [[] for _ in range(n)]
    for i, (a, b, c) in enumerate(triples):
        adj[a].append(i)
        adj[b].append(i)
        adj[c].append(i)

    # Recursive search
    def backtrack(mask):
        if mask == full_mask:
            return True
        # Find first uncovered module
        # Use bit trick to find lowest zero bit
        inv = (~mask) & full_mask
        # lowest set bit
        first = (inv & -inv).bit_length() - 1
        # Try triples containing this module
        for idx in adj[first]:
            if used[idx]:
                continue
            m = triple_masks[idx]
            if mask & m:
                continue  # overlap
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
            print(a+1, b+1, c+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()