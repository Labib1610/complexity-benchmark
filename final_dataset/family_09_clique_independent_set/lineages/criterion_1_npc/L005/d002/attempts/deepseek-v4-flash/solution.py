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

    # Split vertices into two halves
    left_n = n // 2
    right_n = n - left_n

    left_adj = [0] * left_n
    right_adj = [0] * right_n
    for i in range(left_n):
        mask = 0
        for j in range(n):
            if (adj[i] >> j) & 1:
                if j < left_n:
                    mask |= (1 << j)
                else:
                    mask |= (1 << (j - left_n + left_n))  # not used
        left_adj[i] = adj[i] & ((1 << left_n) - 1)

    for i in range(right_n):
        orig = i + left_n
        mask = 0
        for j in range(n):
            if (adj[orig] >> j) & 1:
                if j >= left_n:
                    mask |= (1 << (j - left_n))
        right_adj[i] = mask

    # Generate all independent sets in left half
    left_sets = {}  # size -> bitmask
    for mask in range(1 << left_n):
        ok = True
        for i in range(left_n):
            if (mask >> i) & 1:
                if (left_adj[i] & mask) != 0:
                    ok = False
                    break
        if ok:
            sz = bin(mask).count("1")
            if sz not in left_sets:
                left_sets[sz] = mask
            else:
                # keep any, we just need existence
                pass

    # Generate all independent sets in right half
    right_sets = {}
    for mask in range(1 << right_n):
        ok = True
        for i in range(right_n):
            if (mask >> i) & 1:
                if (right_adj[i] & mask) != 0:
                    ok = False
                    break
        if ok:
            sz = bin(mask).count("1")
            if sz not in right_sets:
                right_sets[sz] = mask

    # Try to combine
    for lsz, lmask in left_sets.items():
        rsz = k - lsz
        if rsz < 0 or rsz > right_n:
            continue
        if rsz not in right_sets:
            continue
        rmask = right_sets[rsz]

        # Check cross edges
        ok = True
        for i in range(left_n):
            if (lmask >> i) & 1:
                # check edges to right half
                cross = adj[i] >> left_n
                if cross & rmask:
                    ok = False
                    break
        if ok:
            # Found
            res = []
            for i in range(left_n):
                if (lmask >> i) & 1:
                    res.append(i + 1)
            for i in range(right_n):
                if (rmask >> i) & 1:
                    res.append(left_n + i + 1)
            print("YES")
            print(" ".join(map(str, res)))
            return

    print("NO")

if __name__ == "__main__":
    solve()