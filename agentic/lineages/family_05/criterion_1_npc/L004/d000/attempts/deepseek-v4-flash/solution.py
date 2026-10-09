import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    triples = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        triples.append((a-1, b-1, c-1))  # 0-indexed

    # Sort triples to help pruning
    triples.sort()

    # Precompute adjacency: for each (p1, p2) pair, list of p3
    from collections import defaultdict
    pair_to_p3 = defaultdict(list)
    for a, b, c in triples:
        pair_to_p3[(a, b)].append(c)

    full_mask = (1 << k) - 1
    chosen = []

    # Backtracking
    def dfs(mask1, mask2, mask3, start_idx):
        if mask1 == full_mask and mask2 == full_mask and mask3 == full_mask:
            return True
        # Find first unused value in mask1
        # We can iterate over triples from start_idx
        for i in range(start_idx, len(triples)):
            a, b, c = triples[i]
            if (mask1 >> a) & 1:
                continue
            if (mask2 >> b) & 1:
                continue
            if (mask3 >> c) & 1:
                continue
            chosen.append((a+1, b+1, c+1))
            if dfs(mask1 | (1 << a), mask2 | (1 << b), mask3 | (1 << c), i+1):
                return True
            chosen.pop()
        return False

    if dfs(0, 0, 0, 0):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()