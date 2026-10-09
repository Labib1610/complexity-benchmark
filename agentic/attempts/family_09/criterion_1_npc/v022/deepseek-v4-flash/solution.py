import sys
sys.setrecursionlimit(1000000)

def solve():
    n, m, k = map(int, sys.stdin.readline().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # If k is 0, empty set is valid (but k >= 1 per constraints)
    if k == 0:
        print("YES")
        print()
        return

    # Split vertices into two halves
    left_n = n // 2
    right_n = n - left_n

    left_adj = [0] * left_n
    right_adj = [0] * right_n
    for i in range(left_n):
        left_adj[i] = adj[i] & ((1 << left_n) - 1)
    for i in range(right_n):
        right_adj[i] = (adj[left_n + i] >> left_n) & ((1 << right_n) - 1)

    # Precompute all independent sets in the right half
    right_sets = {}
    for mask in range(1 << right_n):
        ok = True
        for i in range(right_n):
            if mask & (1 << i):
                if mask & right_adj[i]:
                    ok = False
                    break
        if ok:
            cnt = bin(mask).count("1")
            if cnt not in right_sets or bin(mask).count("1") > bin(right_sets[cnt]).count("1"):
                # store the one with more bits for same count? Actually we want max bits for each count
                pass
            # We'll store the mask with max count for each size
            if cnt not in right_sets:
                right_sets[cnt] = mask
            else:
                # keep the one with more bits? Actually same count, so keep any
                pass

    # But we need for each size the mask with the most bits? No, we need exact size.
    # So we store any mask for each size.
    right_by_size = {}
    for mask in range(1 << right_n):
        ok = True
        for i in range(right_n):
            if mask & (1 << i):
                if mask & right_adj[i]:
                    ok = False
                    break
        if ok:
            cnt = bin(mask).count("1")
            if cnt not in right_by_size:
                right_by_size[cnt] = mask

    # Enumerate left independent sets and combine
    for lmask in range(1 << left_n):
        ok = True
        for i in range(left_n):
            if lmask & (1 << i):
                if lmask & left_adj[i]:
                    ok = False
                    break
        if not ok:
            continue
        lcnt = bin(lmask).count("1")
        if lcnt > k:
            continue
        need = k - lcnt
        if need < 0 or need > right_n:
            continue
        if need not in right_by_size:
            continue
        rmask = right_by_size[need]
        # Check cross edges between left and right
        cross_ok = True
        for i in range(left_n):
            if lmask & (1 << i):
                # right part of adj[i]
                cross = (adj[i] >> left_n) & ((1 << right_n) - 1)
                if cross & rmask:
                    cross_ok = False
                    break
        if cross_ok:
            # Found solution
            chosen = []
            for i in range(left_n):
                if lmask & (1 << i):
                    chosen.append(i + 1)
            for j in range(right_n):
                if rmask & (1 << j):
                    chosen.append(left_n + j + 1)
            print("YES")
            print(" ".join(map(str, chosen)))
            return

    print("NO")

if __name__ == "__main__":
    solve()