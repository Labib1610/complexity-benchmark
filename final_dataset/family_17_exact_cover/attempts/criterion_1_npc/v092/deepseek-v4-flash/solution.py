import sys

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    n = 3 * q
    triples = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        triples.append((a - 1, b - 1, c - 1))
    
    # Build adjacency: for each sample, list of triple indices containing it
    adj = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(triples):
        adj[a].append(idx)
        adj[b].append(idx)
        adj[c].append(idx)
    
    used = [False] * t
    chosen = []
    full_mask = (1 << n) - 1
    # We'll use bitmask for covered samples
    covered = 0
    
    # Precompute mask for each triple
    masks = []
    for a, b, c in triples:
        masks.append((1 << a) | (1 << b) | (1 << c))
    
    # Sort triples by size of adjacency to improve pruning? Not necessary but can help.
    
    def backtrack(covered, count):
        if count == q:
            return covered == full_mask
        if covered == full_mask:
            return count == q
        
        # Find first uncovered sample
        # Use bit trick to find lowest zero bit
        # covered has 1s for covered samples
        inv = (~covered) & full_mask
        if inv == 0:
            return False
        # lowest set bit
        lsb = inv & -inv
        sample = (lsb.bit_length() - 1)
        
        # Try each triple containing this sample
        for idx in adj[sample]:
            if used[idx]:
                continue
            mask = masks[idx]
            if mask & covered:
                continue
            used[idx] = True
            chosen.append(triples[idx])
            if backtrack(covered | mask, count + 1):
                return True
            chosen.pop()
            used[idx] = False
        return False
    
    if backtrack(0, 0):
        print("YES")
        for a, b, c in chosen:
            print(a + 1, b + 1, c + 1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()