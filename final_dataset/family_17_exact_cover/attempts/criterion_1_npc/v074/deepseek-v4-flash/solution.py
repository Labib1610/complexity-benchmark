import sys

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    n = 3 * q
    triples = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        triples.append((a-1, b-1, c-1))
    
    # We'll use bitmask to represent covered items
    full_mask = (1 << n) - 1
    # Precompute mask for each triple
    masks = []
    for a, b, c in triples:
        masks.append((1 << a) | (1 << b) | (1 << c))
    
    # Sort triples by some heuristic (e.g., by number of uncovered items)
    # But simple backtracking with pruning should work for n <= 600, t <= 20000
    # We'll use recursion with memoization on (index, mask) but mask is huge.
    # Instead, we'll do DFS with pruning: pick the first uncovered item and try triples containing it.
    
    # Build adjacency: for each item, list of triple indices that contain it
    item_to_triples = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(triples):
        item_to_triples[a].append(idx)
        item_to_triples[b].append(idx)
        item_to_triples[c].append(idx)
    
    chosen = []
    
    def dfs(mask):
        if mask == full_mask:
            return True
        # Find first uncovered item
        # Use bit trick to find lowest zero bit
        # We'll iterate over items
        for i in range(n):
            if not (mask >> i) & 1:
                break
        # Try triples containing item i
        for idx in item_to_triples[i]:
            m = masks[idx]
            if mask & m == 0:  # no overlap
                chosen.append(idx)
                if dfs(mask | m):
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