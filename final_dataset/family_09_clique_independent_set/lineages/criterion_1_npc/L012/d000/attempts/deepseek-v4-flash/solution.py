import sys
from itertools import combinations

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # Split vertices into two halves
    half = n // 2
    left = list(range(half))
    right = list(range(half, n))

    # Precompute independent sets for left half
    left_sets = {}  # size -> list of (mask, vertices)
    for mask in range(1 << len(left)):
        ok = True
        for i in range(len(left)):
            if mask >> i & 1:
                # check conflicts within left
                for j in range(i+1, len(left)):
                    if (mask >> j & 1) and (adj[left[i]] >> left[j] & 1):
                        ok = False
                        break
                if not ok:
                    break
        if ok:
            size = bin(mask).count("1")
            verts = tuple(left[i] for i in range(len(left)) if mask >> i & 1)
            left_sets.setdefault(size, []).append((mask, verts))

    # Precompute independent sets for right half
    right_sets = {}
    for mask in range(1 << len(right)):
        ok = True
        for i in range(len(right)):
            if mask >> i & 1:
                for j in range(i+1, len(right)):
                    if (mask >> j & 1) and (adj[right[i]] >> right[j] & 1):
                        ok = False
                        break
                if not ok:
                    break
        if ok:
            size = bin(mask).count("1")
            verts = tuple(right[i] for i in range(len(right)) if mask >> i & 1)
            right_sets.setdefault(size, []).append((mask, verts))

    # For each left size, store masks and their vertex lists
    left_by_size = {}
    for size, lst in left_sets.items():
        left_by_size[size] = lst

    right_by_size = {}
    for size, lst in right_sets.items():
        right_by_size[size] = lst

    # Try to combine
    for lsize in range(k + 1):
        rsize = k - lsize
        if lsize not in left_by_size or rsize not in right_by_size:
            continue
        for lmask, lverts in left_by_size[lsize]:
            # Build conflict mask from left to right
            conflict_mask = 0
            for i in range(len(left)):
                if lmask >> i & 1:
                    conflict_mask |= adj[left[i]]
            # Only keep right vertices not conflicting
            allowed_right_mask = 0
            for i in range(len(right)):
                if not (conflict_mask >> right[i] & 1):
                    allowed_right_mask |= (1 << i)
            for rmask, rverts in right_by_size[rsize]:
                if (rmask & ~allowed_right_mask) == 0:
                    # Found
                    ans = list(lverts) + list(rverts)
                    print("YES")
                    print(" ".join(str(x+1) for x in ans))
                    return

    print("NO")

if __name__ == "__main__":
    solve()