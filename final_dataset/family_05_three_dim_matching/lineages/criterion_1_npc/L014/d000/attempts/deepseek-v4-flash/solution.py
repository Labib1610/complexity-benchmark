import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    reactions = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        reactions.append((x-1, y-1, z-1))  # 0-index

    # Group reactions by x
    by_x = [[] for _ in range(k)]
    for idx, (x, y, z) in enumerate(reactions):
        by_x[x].append((y, z, idx))

    # Sort each group by degree (number of options) to try most constrained first
    for i in range(k):
        by_x[i].sort(key=lambda yz: len(by_x[i]))  # not really helpful, but okay

    used_y = 0
    used_z = 0
    chosen = [None] * k
    full_mask = (1 << k) - 1

    # Precompute for each x, the list of (y,z) pairs
    # We'll do recursive backtracking with forward checking

    # To speed up, we can order x by number of options (most constrained first)
    order = sorted(range(k), key=lambda x: len(by_x[x]))

    def backtrack(pos):
        nonlocal used_y, used_z
        if pos == k:
            return True
        x = order[pos]
        for y, z, idx in by_x[x]:
            if (used_y >> y) & 1:
                continue
            if (used_z >> z) & 1:
                continue
            # Forward check: can we still cover remaining y and z?
            # Simple check: count remaining y and z vs remaining slots
            # We'll do a quick check: number of unused y must be >= remaining slots, same for z
            remaining = k - pos - 1
            unused_y_count = k - bin(used_y).count("1")
            unused_z_count = k - bin(used_z).count("1")
            if unused_y_count - 1 < remaining or unused_z_count - 1 < remaining:
                continue
            # Also check if any remaining x has no valid y/z left
            # This is more expensive but can prune a lot
            # We'll do a simple check: for each remaining x, at least one option with unused y,z
            possible = True
            for j in range(pos+1, k):
                x2 = order[j]
                found = False
                for y2, z2, _ in by_x[x2]:
                    if not ((used_y >> y2) & 1) and not ((used_z >> z2) & 1):
                        found = True
                        break
                if not found:
                    possible = False
                    break
            if not possible:
                continue

            # Choose
            used_y |= (1 << y)
            used_z |= (1 << z)
            chosen[x] = (x+1, y+1, z+1)
            if backtrack(pos+1):
                return True
            # Undo
            used_y ^= (1 << y)
            used_z ^= (1 << z)
        return False

    if backtrack(0):
        print("YES")
        for x in range(k):
            print(*chosen[x])
    else:
        print("NO")

if __name__ == "__main__":
    solve()