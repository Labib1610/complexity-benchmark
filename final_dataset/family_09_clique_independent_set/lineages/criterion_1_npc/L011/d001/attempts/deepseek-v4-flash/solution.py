import sys

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

    # Split into two halves
    n1 = n // 2
    n2 = n - n1
    left = list(range(n1))
    right = list(range(n1, n))

    # Precompute adjacency masks for each half
    adj_left = [0] * n1
    adj_right = [0] * n2
    for i in range(n1):
        mask = 0
        for j in range(n1):
            if (adj[left[i]] >> left[j]) & 1:
                mask |= (1 << j)
        adj_left[i] = mask
    for i in range(n2):
        mask = 0
        for j in range(n2):
            if (adj[right[i]] >> right[j]) & 1:
                mask |= (1 << j)
        adj_right[i] = mask

    # Cross edges between halves: for each left vertex, mask of right vertices it connects to
    cross_left_to_right = [0] * n1
    for i in range(n1):
        mask = 0
        for j in range(n2):
            if (adj[left[i]] >> right[j]) & 1:
                mask |= (1 << j)
        cross_left_to_right[i] = mask

    # Enumerate all independent sets in left half
    left_sets = []  # list of (mask, size)
    for mask in range(1 << n1):
        ok = True
        for i in range(n1):
            if (mask >> i) & 1:
                if (adj_left[i] & mask) != 0:
                    ok = False
                    break
        if ok:
            left_sets.append((mask, bin(mask).count('1')))

    # Enumerate all independent sets in right half
    right_sets = []  # list of (mask, size)
    for mask in range(1 << n2):
        ok = True
        for i in range(n2):
            if (mask >> i) & 1:
                if (adj_right[i] & mask) != 0:
                    ok = False
                    break
        if ok:
            right_sets.append((mask, bin(mask).count('1')))

    # Group right sets by size
    right_by_size = {}
    for mask, sz in right_sets:
        right_by_size.setdefault(sz, []).append(mask)

    # Try to combine
    for lmask, lsz in left_sets:
        need = k - lsz
        if need < 0 or need > n2:
            continue
        if need not in right_by_size:
            continue
        # For this left set, compute forbidden right vertices (connected to any left vertex in set)
        forbidden = 0
        for i in range(n1):
            if (lmask >> i) & 1:
                forbidden |= cross_left_to_right[i]
        # Need a right independent set of size 'need' that does not intersect forbidden
        for rmask in right_by_size[need]:
            if (rmask & forbidden) == 0:
                # Found solution
                panel = []
                for i in range(n1):
                    if (lmask >> i) & 1:
                        panel.append(left[i] + 1)
                for j in range(n2):
                    if (rmask >> j) & 1:
                        panel.append(right[j] + 1)
                print("YES")
                print(" ".join(map(str, panel)))
                return

    print("NO")

if __name__ == "__main__":
    solve()