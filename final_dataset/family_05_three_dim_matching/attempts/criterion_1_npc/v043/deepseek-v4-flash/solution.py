import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    commands = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        commands.append((x-1, y-1, z-1))  # 0-indexed

    # We'll try to match using backtracking with bitmask for A and B, and a set for C.
    # Since k <= 22, we can use bitmasks for A and B.
    # We'll sort commands to help pruning.

    # Build adjacency: for each (x,y) pair, list of z's
    from collections import defaultdict
    pair_to_z = defaultdict(list)
    for x, y, z in commands:
        pair_to_z[(x, y)].append(z)

    # We'll try to select k commands with distinct x, distinct y, distinct z.
    # This is equivalent to finding a perfect matching in a 3-partite hypergraph.

    # Use recursion with bitmasks for x and y, and a boolean array for z.
    used_z = [False] * k
    selected = []

    # Precompute list of pairs sorted by number of z options (smallest first)
    pairs = list(pair_to_z.keys())
    pairs.sort(key=lambda p: len(pair_to_z[p]))

    def backtrack(idx, mask_x, mask_y, count):
        if count == k:
            return True
        if idx == len(pairs):
            return False
        x, y = pairs[idx]
        # Prune: if x or y already used, skip this pair
        if (mask_x >> x) & 1 or (mask_y >> y) & 1:
            return backtrack(idx+1, mask_x, mask_y, count)
        # Try each z for this pair
        for z in pair_to_z[(x, y)]:
            if not used_z[z]:
                used_z[z] = True
                selected.append((x+1, y+1, z+1))
                if backtrack(idx+1, mask_x | (1<<x), mask_y | (1<<y), count+1):
                    return True
                selected.pop()
                used_z[z] = False
        # Also try skipping this pair entirely
        return backtrack(idx+1, mask_x, mask_y, count)

    if backtrack(0, 0, 0, 0):
        print("YES")
        for x, y, z in selected:
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()