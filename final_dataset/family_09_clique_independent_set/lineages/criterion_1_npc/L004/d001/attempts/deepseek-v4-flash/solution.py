import sys
from collections import defaultdict

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
    n1 = n // 2
    n2 = n - n1
    left_vertices = list(range(n1))
    right_vertices = list(range(n1, n))
    
    # Enumerate all subsets of left half
    left_subsets = []  # list of (size, mask, is_independent)
    for mask in range(1 << n1):
        size = bin(mask).count('1')
        # check independence
        ok = True
        for i in range(n1):
            if mask >> i & 1:
                # check edges to other selected in left
                if adj[left_vertices[i]] & mask & ~(1 << i):
                    ok = False
                    break
        if ok:
            left_subsets.append((size, mask))
    
    # Enumerate all subsets of right half
    right_subsets = []  # list of (size, mask, forbidden_left_mask)
    for mask in range(1 << n2):
        size = bin(mask).count('1')
        ok = True
        forbidden = 0
        for j in range(n2):
            if mask >> j & 1:
                v = right_vertices[j]
                # check edges to other selected in right
                if adj[v] & (mask << n1) & ~(1 << (n1 + j)):
                    ok = False
                    break
                # collect left neighbors
                forbidden |= (adj[v] & ((1 << n1) - 1))
        if ok:
            right_subsets.append((size, mask, forbidden))
    
    # Group right subsets by size and forbidden mask
    right_map = defaultdict(list)  # (size, forbidden) -> list of right masks
    for size, mask, forbidden in right_subsets:
        right_map[(size, forbidden)].append(mask)
    
    # Try to combine
    for lsize, lmask in left_subsets:
        rsize = k - lsize
        if rsize < 0 or rsize > n2:
            continue
        # For this left subset, we need right subset with no edges to it
        # That means forbidden mask of right subset must not intersect lmask
        # So we need right subsets with forbidden & lmask == 0
        # We'll iterate over all right subsets of size rsize and check
        for rsize2, rmask, rforbidden in right_subsets:
            if rsize2 != rsize:
                continue
            if rforbidden & lmask:
                continue
            # Found
            ans = []
            for i in range(n1):
                if lmask >> i & 1:
                    ans.append(i + 1)
            for j in range(n2):
                if rmask >> j & 1:
                    ans.append(n1 + j + 1)
            print("YES")
            print(" ".join(map(str, ans)))
            return
    
    print("NO")

if __name__ == "__main__":
    solve()